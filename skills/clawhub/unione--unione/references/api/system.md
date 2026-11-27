# UniOne API: System

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /system/ping.json

Checks API key validity and returns user ID.

Request body (application/json):


Response 200: API key is valid.

- `status` (string, required; enum: success) — "success" string
- `user_id` (integer, required) — Unique user identifier.

Response default: Error occured.

## POST /system/info.json

Gets user or project info by API key.

Request body (application/json):


Response 200: User or project info successfully returned.

- `status` (string, required; enum: success) — "success" string
- `user_id` (integer, required) — Unique user identifier.
- `email` (string, required) — Email of the user.
- `project_id` (string) — Unqiue project identifier, ASCII string up to 36 characters long. Present only if the API key used for request is the project API key.
- `project_name` (string) — Project name, unique for user account. Present only if the API key used for request is the project API key.
- `project_accounting` (object) — Object with email counter properties. Present only if the API key used for request is the user API key.
  - `email_counter` (integer, required) — Project's email counter value. It increases on every email sent.
  - `email_counter_limit` (integer, required) — Allows you to limit the number of emails sent by the project. The sending stops when the limit is reached. Any non-negative 64-bit integer is acceptable. 0 means no limit.
  - `email_counter_mode` (object, required; enum: default, permanent; default: default) — 'default' - the counter resets to zero automatically at the beginning of each accounting period. 'permanent' - the counter never resets automatically.
- `accounting` (object) — Object with accounting period properties. Present only if the API key used for request is the user API key.
  - `period_start` (string, required) — Date and time of accounting period start in UTC in "YYYY-MM-DD hh:mm:ss" format.
  - `period_end` (string, required) — Date and time of accounting period end in UTC in "YYYY-MM-DD hh:mm:ss" format.
  - `emails_included` (integer, required) — Number of emails included into accounting period.
  - `emails_sent` (integer, required) — Number of emails sent during accounting period. Can be bigger than emails_included in case of overage.

Response default: Error occured.
