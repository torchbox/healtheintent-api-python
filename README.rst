===========================
HealthEIntent APIs (Python)
===========================

A collection of simple Python API wrappers to aid interaction with Cerner's various HealthEIntent REST APIs (https://docs.healtheintent.com).

Based on the Python requests library (http://docs.python-requests.org).

Currently, only the ``Personnel`` API wrapper is implemented (https://docs.healtheintent.com/api/v1/personnel/)


Quick start guide
=================

1.  Install the package using pip: 

    .. code-block:: console

        pip install git+ssh://git@bitbucket.org/rkhleics/healtheintent-api-python.git@v1

2.  Create a client instance, providing a valid ``api_domain`` and ``bearer_token``. e.g.:

    .. code-block:: console

        >>> from healtheintent_api import PersonnelAPIClient
        >>> client = PersonnelAPIClient(
                api_domain="https://cernerdemo.api.us.healtheintent.com/',
                bearer_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9."
            )

3.  Use the various methods client methods to interact with Personnel data. e.g.:

    .. code-block:: console

        >>> client.get_personnel()
        {
          "items": [
            {
              "id": "f89fa3dd-0000-494b-1111-4640ccc081e3",
              "birthDate": "1970-11-15",
              "gender": "FEMALE",
              "name": {
                "prefix": "Dr.",
                "given": "Jane",
                "middle": "Elizabeth",
                "family": "Smith",
                "suffix": "MD",
                "formatted": "Dr. Jane Elizabeth Smith MD"
              },
              "addresses": [
                {
                  "use": "WORK",
                  "text": "2800 Rockcreek Pkwy\\nSuite 1, Kansas City, MO, USA, 64117",
                  "lines": [
                    "2800 Rockcreek Pkwy",
                    "Suite 1"
                  ],
                  "city": "Kansas City",
                  "state": "MO",
                  "postalCode": "64117",
                  "country": "USA"
                }
              ],
              "aliases": [
                {
                  "value": "123.456.7890",
                  "system": "5ecaf544-01d5-01kf-95hj-8e2bcec12006",
                  "type": "SPI"
                }
              ],
              "telecoms": [
                {
                  "system": "PHONE",
                  "value": "816-201-0001"
                },
                {
                  "system": "EMAIL",
                  "value": "jane.smith@cerner.com"
                }
              ],
              "languages": [
                "en",
                "hi",
                "fr"
              ],
              "qualifications": [
                {
                  "code": "BFA",
                  "issuer": "University of Missouri - Kansas City",
                  "start": "2010-01-05T00:00:00Z",
                  "end": "2050-01-05T00:00:00Z"
                }
              ],
              "createdAt": "2016-09-02T02:35:10Z",
              "updatedAt": "2018-01-23T14:42:49Z"
            },
            {
              "id": "hgjfut83-0000-h9g2-1111-4640cjd97de3",
              "birthDate": "1975-09-30",
              "gender": "UNKNOWN",
              "name": {
                "prefix": "Dr.",
                "given": "John",
                "middle": "Michael",
                "family": "Doe",
                "suffix": "III",
                "formatted": "Dr. John Michael Doe III"
              },
              "addresses": [
                {
                  "use": "WORK",
                  "text": "2800 Rockcreek Pkwy\\nSuite 1, Kansas City, MO, USA, 64117",
                  "lines": [
                    "2800 Rockcreek Pkwy",
                    "Suite 1"
                  ],
                  "city": "Kansas City",
                  "state": "MO",
                  "postalCode": "64117",
                  "country": "USA"
                }
              ],
              "aliases": [
                {
                  "value": "0193.421321.31543",
                  "system": "5echdj54-15a9-01jf-8110-8e202jf72006",
                  "type": "SPI"
                }
              ],
              "telecoms": [
                {
                  "system": "PHONE",
                  "value": "816-201-0001"
                },
                {
                  "system": "EMAIL",
                  "value": "john.doe@cerner.com"
                }
              ],
              "languages": [
                "en",
                "fr",
                "es"
              ],
              "qualifications": [
                {
                  "code": "BFA",
                  "issuer": "University of Kansas",
                  "start": "2010-01-05T00:00:00Z",
                  "end": "2050-01-05T00:00:00Z"
                }
              ],
              "createdAt": "2017-10-02T02:05:10Z",
              "updatedAt": "2018-01-23T14:42:49Z"
            }
          ],
          "totalResults": 2,
          "firstLink": "https://cernerdemo.api.us.healtheintent.com/personnel/v1/personnel?formattedName=Dr&orderBy=givenName&offset=0&limit=2",
          "lastLink": "https://cernerdemo.api.us.healtheintent.com/personnel/v1/personnel?formattedName=Dr&orderBy=givenName&offset=2&limit=2"
        }

        >>> client.get_person("f89fa3dd-0000-494b-1111-4640ccc081e3")
        {
              "id": "f89fa3dd-0000-494b-1111-4640ccc081e3",
              "birthDate": "1970-11-15",
              "gender": "FEMALE",
              "name": {
                "prefix": "Dr.",
                "given": "Jane",
                "middle": "Elizabeth",
                "family": "Smith",
                "suffix": "Jr",
                "formatted": "Dr. Jane Elizabeth Smith Jr"
              },
              "addresses": [
                {
                  "use": "WORK",
                  "text": "2800 Rockcreek Pkwy\\nSuite 1, Kansas City, MO, USA, 64117",
                  "lines": [
                    "2800 Rockcreek Pkwy",
                    "Suite 1"
                  ],
                  "city": "Kansas City",
                  "state": "MO",
                  "postalCode": "64117",
                  "country": "USA"
                }
              ],
              "aliases": [
                {
                  "value": "123.456.7890",
                  "system": "5ecaf544-01d5-01kf-95hj-8e2bcec12006",
                  "type": "EXTERNAL"
                }
              ],
              "telecoms": [
                {
                  "system": "EMAIL",
                  "value": "jane.smith@rockhurst.edu"
                }
              ],
              "languages": [
                "en",
                "fr"
              ],
              "qualifications": [
                {
                  "issuer": "Rockhurst University",
                  "code": "MD"
                }
              ],
              "sourceIdentifiers": [
                {
                  "id": "10924.21321042.4vda1",
                  "dataPartitionId": "d1fb6eba-0f56-44fe-8680-b67985533184"
                }
              ],
              "createdAt": "2018-01-10T15:48:32Z",
              "updatedAt": "2018-01-10T15:48:32Z"
            }

4.  Use the various methods client methods to interact with Personnel Group data. e.g.:

    .. code-block:: console

        >>> client.get_groups()
        {
          "items": [
            {
              "id": "1b69dc47-6358-4221-bb61-8618323d18a2",
              "name": "Analytics Data Authors",
              "mnemonic": "analytics_data_authors",
              "aliases": [
                {
                  "value": "8cbbffdc-acfe-11e7-abc4-cec278b6b50c",
                  "system": "2.16.840.1.113883.4.6",
                  "type": "EXTERNAL"
                }
              ],
              "createdAt": "2018-01-21T16:41:24Z",
              "updatedAt": "2018-02-21T16:41:44Z"
            },
            {
              "id": "15d2635d-1264-4b36-9474-4ce28ffc4978",
              "name": "Analytics Data Model Consumers",
              "mnemonic": "analytics_data_model_consumers",
              "aliases": [
                {
                  "value": "9acerner-acfe-11e7-abc4-cec278b6b50c",
                  "system": "3.16.840.1.113883.4.6",
                  "type": "EXTERNAL"
                }
              ],
              "createdAt": "2018-01-11T16:12:24Z",
              "updatedAt": "2018-01-21T13:41:14Z"
            }
          ],
          "totalResults": 2,
          "firstLink": "https://cernerdemo.api.us.healtheintent.com/personnel/v1/personnel-groups?name=analytics data&orderBy=mnemonic&offset=0&limit=20",
          "lastLink": "https://cernerdemo.api.us.healtheintent.com/personnel/v1/personnel-groups?name=analytics data&orderBy=mnemonic&offset=0&limit=20"
        }

        >>> client.get_group("1928bad5-11d2-4028-af95-d7ae3c578567")
        {
          "id": "1928bad5-11d2-4028-af95-d7ae3c578567",
          "name": "Person Management",
          "mnemonic": "mpm_whitelist",
          "aliases": [
            {
              "value": "123.456.7890",
              "system": "5ecaf544-01d5-01kf-95hj-8e2bcec12006",
              "type": "EXTERNAL"
            }
          ],
          "createdAt": "2018-01-10T12:23:12Z",
          "updatedAt": "2018-05-12T15:48:32Z"
        }

5.  For listing methods (``get_personnel()`` and ``get_groups()``), you can use the ``auto_paginate`` option to automatically fetch and return all results. When used, these methods will return a generator instead of the JSON response from the server. e.g.

    .. code-block:: console

        >>> client.get_groups(auto_paginate=True)
        generator object HealthEIntentAPIClient._get_all_entities at 0x10ed5dd00>

        >>> for result in client.get_groups(auto_paginate=True):
               print(result)
        {
          "id": "1b69dc47-6358-4221-bb61-8618323d18a2",
          "name": "Analytics Data Authors",
          "mnemonic": "analytics_data_authors",
          "aliases": [
            {
              "value": "8cbbffdc-acfe-11e7-abc4-cec278b6b50c",
              "system": "2.16.840.1.113883.4.6",
              "type": "EXTERNAL"
            }
          ],
          "createdAt": "2018-01-21T16:41:24Z",
          "updatedAt": "2018-02-21T16:41:44Z"
        }
        {
          "id": "15d2635d-1264-4b36-9474-4ce28ffc4978",
          "name": "Analytics Data Model Consumers",
          "mnemonic": "analytics_data_model_consumers",
          "aliases": [
            {
              "value": "9acerner-acfe-11e7-abc4-cec278b6b50c",
              "system": "3.16.840.1.113883.4.6",
              "type": "EXTERNAL"
            }
          ],
          "createdAt": "2018-01-11T16:12:24Z",
          "updatedAt": "2018-01-21T13:41:14Z"
        }
