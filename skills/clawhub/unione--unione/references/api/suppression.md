# UniOne API: Suppression

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /suppression/set.json

Adds an email address to the suppression list. You can always remove this address from the suppression list later using the [suppression/delete](https://docs.unione.io/en/web-api-ref#suppression-delete) method.

Request body (application/json):

- `email` (string, required) — Email to add in suppression list.
- `cause` (string, required) — Cause of email being suppressed. One of:<ul><li>__unsubscribed__ - email is unsubscribed;<li>__temporary_unavailable__ - the email address is unavailable. This means that over the next three days sending to this address will return an error. Email may be temporarily unavailable due to several reasons, e.g.:<ol><li>a previous email has been rejected by the recipient's server for spam;<li>the recipient's mailbox is full or is not used;<li>recipient's domain does not accept mail;<li>sending server was rejected due to blacklisting;</ol><li>__permanent_unavailable__ - the email address is permanently unavailable due to multiple hard bounces; <li>__complained__ -  the recipient reported spam in the previous emails;</ul>
- `created` (string) — When suppression was created, in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.

Response 200: Email has been added to the suppression list.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.

## POST /suppression/get.json

Gets a reason and date of email suppression.

Request body (application/json):

- `email` (string, required) — Email to get suppression details for.
- `all_projects` (boolean, default: False) — If a user has projects functionality enabled, he/she can pass all_projects=true to search in all projects' data.

Response 200: Method call has succeeded (but suppressions array can be empty if sending to email is not suppressed).

- `status` (string, required; enum: success) — "success" string
- `email` (string, required) — The email for which suppression details were requested.
- `suppressions` (array of object, required) — Array of suppression objects.
  - `project_id` (string) — Unqiue project identifier, ASCII string up to 36 characters long.
  - `cause` (string, required) — Cause of email being suppressed. One of:<ul><li>__unsubscribed__ - email is unsubscribed;<li>__temporary_unavailable__ - the email address is unavailable. This means that over the next three days sending to this address will return an error. Email may be temporarily unavailable due to several reasons, e.g.:<ol><li>a previous email has been rejected by the recipient's server for spam;<li>the recipient's mailbox is full or is not used;<li>recipient's domain does not accept mail;<li>sending server was rejected due to blacklisting;</ol><li>__permanent_unavailable__ - the email address is permanently unavailable due to multiple hard bounces; <li>__complained__ -  the recipient reported spam in the previous emails;<li>__blocked__ -  sending to the email is prohibited by administration of UniOne.</ul>We may add some new causes in the future.
  - `source` (string, required) — Source of email being suppressed. One of:<ul><li>__user__ - suppressed by user with    [suppression/set](https://docs.unione.io/en/web-api-ref#suppression-set);<li>__system__ - sending to the email is prohibited by system, for example due to multiple hard bounces;<li>__subscriber__ - the recipient reported spam or unsubscribed in the previous emails.</ul>
  - `is_deletable` (boolean, required) — Is it possible to delete this suppression by calling suppression/delete method.
  - `created` (string, required) — When suppression was created, in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.

Response default: Error occured.

## POST /suppression/list.json

Returns a suppression list since provided date.

Request body (application/json):

- `cause` (string) — Cause of email being suppressed. One of:<ul><li>__unsubscribed__ - email is unsubscribed;<li>__temporary_unavailable__ - the email address is unavailable. This means that over the next three days sending to this address will return an error. Email may be temporarily unavailable due to several reasons, e.g.:<ol><li>a previous email has been rejected by the recipient's server for spam;<li>the recipient's mailbox is full or is not used;<li>recipient's domain does not accept mail;<li>sending server was rejected due to blacklisting;</ol><li>__permanent_unavailable__ - the email address is permanently unavailable due to multiple hard bounces; <li>__complained__ -  the recipient reported spam in the previous emails;<li>__blocked__ -  sending to the email is prohibited by administration of UniOne.</ul>We may add some new causes in the future.
- `source` (string) — Source of email being suppressed. One of:<ul><li>__user__ - suppressed by user with    [suppression/set](https://docs.unione.io/en/web-api-ref#suppression-set);<li>__system__ - sending to the email is prohibited by system, for example due to multiple hard bounces;<li>__subscriber__ - the recipient reported spam or unsubscribed in the previous emails.</ul>
- `start_time` (string) — Date in the format YYYY-MM-DD hh:mm:ss to get suppression list from the "start_time" to the present day. Ignored if "cursor" is not empty.
- `cursor` (string) — The parameter indicates from which position the selection is to be started. Must be empty or omitted for the first data chunk. In order to get subsequent chunks, you must set the "cursor" parameter in your request, using the value received in response to the previous request.
- `limit` (integer) — Limits the number of records to be returned at one time, default is 50.

Response 200: Returns a suppression list since provided date.

- `status` (string, required; enum: success) — "success" string
- `suppressions` (array of object, required) — Array of suppression objects.
  - `email` (string) — Email to get suppression details for.
  - `cause` (string, required) — Cause of email being suppressed. One of:<ul><li>__unsubscribed__ - email is unsubscribed;<li>__temporary_unavailable__ - the email address is unavailable. This means that over the next three days sending to this address will return an error. Email may be temporarily unavailable due to several reasons, e.g.:<ol><li>a previous email has been rejected by the recipient's server for spam;<li>the recipient's mailbox is full or is not used;<li>recipient's domain does not accept mail;<li>sending server was rejected due to blacklisting;</ol><li>__permanent_unavailable__ - the email address is permanently unavailable due to multiple hard bounces; <li>__complained__ -  the recipient reported spam in the previous emails;<li>__blocked__ -  sending to the email is prohibited by administration of UniOne.</ul>We may add some new causes in the future.
  - `source` (string, required) — Source of email being suppressed. One of:<ul><li>__user__ - suppressed by user with    [suppression/set](https://docs.unione.io/en/web-api-ref#suppression-set);<li>__system__ - sending to the email is prohibited by system, for example due to multiple hard bounces;<li>__subscriber__ - the recipient reported spam or unsubscribed in the previous emails.</ul>
  - `is_deletable` (boolean, required) — Is it possible to delete this suppression by calling suppression/delete method.
  - `created` (string, required) — When suppression was created, in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.
- `cursor` (string, required) — The parameter indicates from which position the selection is to be started. Must be empty or omitted for the first data chunk. In order to get subsequent chunks, you must set the "cursor" parameter in your request, using the value received in response to the previous request.

Response default: Error occured.

## POST /suppression/delete.json

Deletes an email from suppression list (only records with is_deletable=true). If there are no entries of this email in the suppression list, API error 3003 is returned. If such entries exist but no one can be deleted, API error 3004 is returned. If daily limit of deletes exceeded, API error 906 is returned.

Request body (application/json):

- `email` (string, required) — An email to delete from suppression list.

Response 200: Email has been deleted from the suppression list.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
