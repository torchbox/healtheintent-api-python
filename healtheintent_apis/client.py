import requests
from . import errors

ALIAS_TYPE_USER = 'USER'


class HealthEIntentAPIClient:

    api_base_name = None
    api_version = 1

    base_headers = {
        'Accept': 'application/json',
        'Content-type': 'application/json',
    }

    http_error_class_map = {
        400: errors.BadRequestError,
        401: errors.UnauthorizedError,
        403: errors.NotPermittedError,
        404: errors.ResourceNotFoundError,
        409: errors.ResourceConflictError,
    }
    http_error_class_default = errors.HealthEIntentHttpError

    def __init__(self, api_domain='https://cernerdemo.api.us.healtheintent.com',
                 bearer_token=None):
        self._api_domain = api_domain.rstrip('/')
        self._bearer_token = bearer_token
        self._base_api_url = '/'.join((
            self._api_domain,
            self.api_base_name.rstrip('/'),
            'v' + str(self.api_version),
        ))

    def get_headers(self):
        headers = dict(self.base_headers)
        headers['Authorization'] = "Bearer %s" % self._bearer_token
        return headers

    @classmethod
    def _get_specific_http_error_class(cls, http_error):
        status_code = http_error.response.status_code
        return cls.http_error_class_map.get(status_code, cls.http_error_class_default)

    @classmethod
    def _raise_for_status(cls, response):
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Raise a more specific (custom) HttpError
            new_class = cls._get_specific_http_error_class(e)
            new_exception = new_class(
                '{}. Response body:\n{}'.format(e, e.response.content)
            )
            new_exception.response = e.response
            raise new_exception from e
        return response

    def get_full_path(self, request_path):
        return '/'.join((self._base_api_url, request_path.lstrip('/')))

    def post(self, path, **data):
        request_path = self.get_full_path(path)
        resp = requests.post(request_path, json=data, headers=self.get_headers())
        return self._raise_for_status(resp).json()

    def put(self, path, **data):
        request_path = self.get_full_path(path)
        resp = requests.put(request_path, json=data, headers=self.get_headers())
        return self._raise_for_status(resp).json()

    def delete(self, path, **data):
        request_path = self.get_full_path(path)
        resp = requests.delete(request_path, json=data, headers=self.get_headers())
        return self._raise_for_status(resp).json()

    def get(self, path, url_encode=True, **params):
        if not url_encode:
            params = "&".join("%s=%s" % (k, v) for k, v in params.items())
        request_path = self.get_full_path(path)
        resp = requests.get(request_path, params=params, headers=self.get_headers())
        return self._raise_for_status(resp).json()

    def _get_all_entities(self, path, result_list_element_name='items',
                          items_per_page=100, **params):
        """
        A generator method that fetches all available pages of a paginated
        resource (e.g. personnel or personnel groups) and returns a dictionary
        representing each row. See 'get_all_personnel()' and
        'get_all_groups()' for working examples.
        """
        params['limit'] = items_per_page
        response = self.get(path, **params)
        for item in response.get(result_list_element_name, ()):
            yield item
        while response['nextLink']:
            response = self.get(response['nextLink'])
            for item in response.get(result_list_element_name, ()):
                yield item


class PersonnelAPIClient(HealthEIntentAPIClient):

    api_base_name = 'personnel'

    # -------------------------------------------------------------------------
    # Personnel
    # -------------------------------------------------------------------------

    def get_all_personnel(self, **params):
        return self._get_all_entities(path='personnel', **params)

    def get_person(self, person_id, suppress_errors=False):
        path = 'personnel/{}/'.format(person_id)
        return self.get(path)

    def get_person_from_alias(self, alias_value, alias_system=None, alias_type=ALIAS_TYPE_USER):
        params = {
            'aliasValue': alias_value,
            'aliasSystem': alias_system,
            'aliasType': alias_type
        }
        for item in self.get('personnel', **params)['items']:
            return item

    def create_person(self, first_name, last_name, **data):
        data["name"] = {
            "given": first_name,
            "family": last_name,
            "prefix": data.pop('name_prefix', None),
            "suffix": data.pop('name_suffix', None),
        }
        return self.post('personnel', **data)

    def create_person_with_alias(self, first_name, last_name, alias_value, alias_system,
                                 alias_type=ALIAS_TYPE_USER, **data):
        alias = {
            'type': alias_type,
            'system': alias_system,
            'value': alias_value,
        }
        data['aliases'] = [alias]
        return self.create_person(first_name, last_name, **data)

    # -------------------------------------------------------------------------
    # Personnel Groups
    # -------------------------------------------------------------------------

    def get_all_groups(self, **params):
        return self._get_all_entities(path='personnel-groups', **params)

    def get_group(self, group_id, suppress_errors=False):
        path = 'personnel-groups/{}/'.format(group_id)
        return self.get(path)

    def get_group_members(self, group_id, **params):
        path = 'personnel-groups/{}/members'.format(group_id)
        return self.get_all_entities(path=path, **params)

    def add_person_to_group(self, person_id, group_id):
        path = 'personnel-groups/{group_id}/members/{person_id}'.format(
            group_id=group_id,
            person_id=person_id,
        )
        return self.put(path)

    def remove_person_from_group(self, person_id, group_id):
        path = 'personnel-groups/{group_id}/members/{person_id}'.format(
            group_id=group_id,
            person_id=person_id,
        )
        return self.delete(path)
