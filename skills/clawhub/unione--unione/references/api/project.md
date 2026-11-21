# UniOne API: Project

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /project/create.json

Creates a new project.

Request body (application/json):

- `project` (object, required) — Object with project properties.
  - `name` (string, required) — Project name, unique for user account.
  - `country` (string) — ISO-3166 alpha-2 country code. If set, UniOne treats project personal data according to country laws, e.g. GDPR for european countries.
  - `send_enabled` (boolean, default: True) — Whether email sending is enabled for this project or not.
  - `custom_unsubscribe_url_enabled` (boolean) — If it's false then UniOne adds default unsubscribe footer to each email sent with API key of the project. If it's true then appending default unsubscribe footer for this project is avoided and sending with custom unsubscribe url or even without unsubscribe url is permitted for the project. Please note that custom_unsubscribe_url_enabled=true is available only if removing unsubscribe link is approved for the user account by support. More on this [here](https://docs.unione.io/en/unsubscribe-link). When custom_unsubscribe_url_enabled is skipped on creating a project, it's value is taken from user
  - `backend_domain_id` (integer) — A unique domain identifier which will determine the [tracking domain](https://docs.unione.io/en/tracking-domains) or [dedicated IP](https://docs.unione.io/en/dedicated-ip) pool to be used by default. If the value is not specified, a default backend domain will be assigned for your account or project instead.
  - `unsubscribe_page_id` (integer) — A unique identifier that defines the default unsubscribe page. If absent, the account/project will be assigned the system default unsubscribe page.

Response 200: Project created successfully.

- `status` (string, required; enum: success) — "success" string
- `project_id` (string, required) — Unqiue project identifier, ASCII string up to 36 characters long.
- `project_api_key` (string, required) — API key of the project. You can use it instead of the user API key parameter in all methods except project/* methods.

Response default: Error occured.

## POST /project/update.json

Updates a project.

Request body (application/json):

- `project_id` (string) — Unique project identifier. You should identify project to update either with project_id or with project_api_key field. But we recommend usage of project_id as a more secure option.
- `project_api_key` (string) — Optional project API key. You should identify project to update either with project_id or with project_api_key field. But we recommend usage of project_id as a more secure option.
- `project` (object, required) — Object with project properties.
  - `name` (string, required) — Project name, unique for user account.
  - `country` (string) — ISO-3166 alpha-2 country code. If set, UniOne treats project personal data according to country laws, e.g. GDPR for european countries.
  - `send_enabled` (boolean, default: True) — Whether email sending is enabled for this project or not.
  - `custom_unsubscribe_url_enabled` (boolean) — If it's false then UniOne adds default unsubscribe footer to each email sent with API key of the project. If it's true then appending default unsubscribe footer for this project is avoided and sending with custom unsubscribe url or even without unsubscribe url is permitted for the project. Please note that custom_unsubscribe_url_enabled=true is available only if removing unsubscribe link is approved for the user account by support. More on this [here](https://docs.unione.io/en/unsubscribe-link). When custom_unsubscribe_url_enabled is skipped on creating a project, it's value is taken from user
  - `backend_domain_id` (integer) — A unique domain identifier which will determine the [tracking domain](https://docs.unione.io/en/tracking-domains) or [dedicated IP](https://docs.unione.io/en/dedicated-ip) pool to be used by default. If the value is not specified, a default backend domain will be assigned for your account or project instead.
  - `unsubscribe_page_id` (integer) — A unique identifier that defines the default unsubscribe page. If absent, the account/project will be assigned the system default unsubscribe page.
  - `email_counter` (integer) — Project's email counter value. 0 value only is accepted (which means resetting the counter to zero), or refreshes automatically depending on the counter mode set with the 'email_counter_mode' parameter. If the request doesn't contain the field or contains null, the limit value doesn't change.
  - `email_counter_limit` (integer, default: 0) — Allows you to limit the number of emails sent by the project. The sending stops when the limit is reached. Any non-negative 64-bit integer is acceptable. Setting to 0 means no limit. If the request doesn't contain the field or contains null, the limit value doesn't change.
  - `email_counter_mode` (object, enum: default, permanent; default: default) — Sets the email counter mode. It allows you to choose whether the counter should reset automatically, or remain permanent. The following values are acceptable: 'default' - the counter resets to zero automatically at the beginning of each accounting period, 'permanent' - the counter never resets automatically. The reset can be done only manually by the user in the request with the passes 0 value in the email_counter field. If the request doesn't contain the field or contains a null value, the limit value doesn't change.

Response 200: Project updated successfully.

- `status` (string, required; enum: success) — "success" string
- `project_api_key` (string) — API key of the project. Returned only if the project to update was identified by project_api_key. Not returned in case of updating by project_id.

Response default: Error occured.

## POST /project/list.json

Lists projects.

Request body (application/json):

- `project_id` (string) — Optional possibility to specify project_id to include only this project to list.
- `project_api_key` (string) — Optional possibility to specify project_api_key to include only this project to list.

Response 200: Projects returned successfully.

- `status` (string, enum: success) — "success" string
- `projects` (array of object) — Array of objects where each object represents one project.
  - `id` (string, required) — Unqiue project identifier, ASCII string up to 36 characters long.
  - `api_key` (string, required) — API key of the project. You can use it instead of the user API key parameter in all methods except project/* methods.
  - `name` (string, required) — Project name, unique for user account.
  - `country` (string, required) — ISO-3166 alpha-2 country code. If set, UniOne treats project personal data according to country laws, e.g. GDPR for european countries.
  - `reg_time` (string, required) — Date and time of project creation in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.
  - `send_enabled` (boolean, required; default: True) — Whether email sending is enabled for this project or not.
  - `custom_unsubscribe_url_enabled` (boolean, required) — If it's false then UniOne adds default unsubscribe footer to each email sent with API key of the project. If it's true then appending default unsubscribe footer for this project is avoided and sending with custom unsubscribe url or even without unsubscribe url is permitted for the project. Please note that custom_unsubscribe_url_enabled=true is available only if removing unsubscribe link is approved for the user account by support. More on this [here](https://docs.unione.io/en/unsubscribe-link). When custom_unsubscribe_url_enabled is skipped on creating a project, it's value is taken from user
  - `backend_domain_id` (integer, required) — A unique domain identifier which will determine the [tracking domain](https://docs.unione.io/en/tracking-domains) or [dedicated IP](https://docs.unione.io/en/dedicated-ip) pool to be used by default. If the value is not specified, a default backend domain will be assigned for your account or project instead.
  - `email_counter` (integer, required) — Project's email counter value. It increases on every email sent.
  - `email_counter_limit` (integer, required) — Allows you to limit the number of emails sent by the project. The sending stops when the limit is reached. Any non-negative 64-bit integer is acceptable. 0 means no limit.
  - `email_counter_mode` (object, required; enum: default, permanent; default: default) — 'default' - the counter resets to zero automatically at the beginning of each accounting period. 'permanent' - the counter never resets automatically.
  - `unsubscribe_page_id` (integer, required) — A unique identifier that defines the default unsubscribe page. If absent, the account/project will be assigned the system default unsubscribe page.

Response default: Error occured.

## POST /project/delete.json

Deletes a project.

The project will be moved to the "trash bin" before being permanently deleted. You can restore the project by contacting support.

Request body (application/json):

- `project_id` (string) — Unique project identifier. You should identify project to delete either with project_id or with project_api_key field. We recommend usage of project_id as a more secure option.
- `project_api_key` (string) — Optional project API key. You should identify project to delete either with project_id or with project_api_key field. We recommend usage of project_id as a more secure option.

Response 200: Project deleted successfully.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
