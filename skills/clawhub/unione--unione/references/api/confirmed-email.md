# UniOne API: Confirmed email

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /confirmed-email/create.json

Adds an email address and sends a confirmation link.

Request body (application/json):

- `email` (string, required) — Email address to add or delete.

Response 200: Confirmation email was sent.

- `status` (string, required; enum: success) — "success" string
- `confirmed_email` (object, required)
  - `email` (string, required)
  - `status` (string, required; enum: confirmed, unconfirmed) — Confirmation status of the email address.

Response default: Error occured.

## POST /confirmed-email/list.json

Lists confirmed and unconfirmed email addresses for the account.

Request body (application/json):


Response 200: Confirmed email list.

- `status` (string, required; enum: success) — "success" string
- `confirmed_emails` (array of object, required)
  - `email` (string, required)
  - `status` (string, required; enum: confirmed, unconfirmed) — Confirmation status of the email address.

Response default: Error occured.

## POST /confirmed-email/delete.json

Deletes an email address from the account's confirmed email list.

Request body (application/json):

- `email` (string, required) — Email address to add or delete.

Response 200: Confirmed email deleted.

- `status` (string, required; enum: success) — "success" string
- `message` (string, required)

Response default: Error occured.
