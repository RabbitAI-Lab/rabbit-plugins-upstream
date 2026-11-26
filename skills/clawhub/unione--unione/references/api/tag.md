# UniOne API: Tag

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /tag/list.json

This method returns the full list of user-defined tags. Does not receive any parameters.

Request body (application/json):


Response 200: List returned successfully.

- `status` (string, required; enum: success) — "success" string
- `tags` (array of object, required) — An array of objects containing data for user-defined tags.
  - `tag_id` (integer, required) — Unique tag id.
  - `tag` (string, required) — Tag name.

Response default: Error occured.

## POST /tag/delete.json

Removes tag.

Request body (application/json):

- `tag_id` (integer, required) — Unique tag id.

Response 200: Tag deleted successfully.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
