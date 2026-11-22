# UniOne API: Email-validation

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /email-validation/single.json

A maximum of two concurrent requests are allowed; if you send more requests, an error will be returned. Since the verification process should be completed promptly, we've set a time limit on email check. If we encounter a slow email server that does not respond in 5 seconds, you may get an “unknown” status.

Request body (application/json):

- `email` (string, required) — Email address to be checked.

Response 200: Email check completed successfully.

- `status` (string, required; enum: success) — "success" string
- `email` (string, required) — Email address to be checked.
- `result` (string, required) — Possible statuses: <ul><li>"valid" - the address is valid, <li>"invalid" - the address is invalid, <li>"suspicious" - the address looks suspicious, <li>"unknown" - could not perform validation, the domain’s mail server has not responded within the time limit.</ul>
- `cause` (string, required) — Possible statuses: <ul><li>"no_mx_record" - no MX record found for the target domain, <li>"syntax_error" - the address syntax is invalid, <li>"possible_typo" - the address is likely to have a typo, <li>"mailbox_not_found" - the address does not exist, <li>"global_suppression" - the address has been marked as unreachable due to multiple previous delivery errors, <li>"disposable" - this is a disposable one-time email address which is usually valid for a few minutes only, <li>"role" - the address is not likely to belong to an actual person, but rather to a certain business staff role, <li>"abuse" - the address is known to be a source of a large number of complaints, sometimes issued automatically, <li>"spamtrap" - this email is a spam trap, it is published openly but never used for actual emails. Sending messages to such addresses has a huge negative impact on reputation score,  <li>"smtp_connection_failed" - the domain’s SMTP server does not respond; the address may contain a typo.</ul>
- `validity` (integer, required) — Validity score, from 0 to 100 (0 – invalid, 100 – valid).
- `local_part` (string, required) — Local part (everything preceding the @ sign).
- `domain` (string, required) — Domain name part.
- `mx_found` (boolean, required) — True if the address’ domain does have an MX record, false if does not.
- `mx_record` (string, required) — Preferred MX record for the domain.
- `did_you_mean` (string, required) — For addresses which are likely to have typing errors (cause=possible_typo), a suggested variant with a fixed typo.
- `processed_at` (string, required) — Email check date and time, YYYY-MM-DD hh:mm:ss UTC.

Response default: Error occured.
