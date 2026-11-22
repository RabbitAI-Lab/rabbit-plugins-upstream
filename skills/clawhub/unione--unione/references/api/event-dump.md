# UniOne API: Event-dump

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /event-dump/create.json

This asynchronous method initiates the preparation of data dump in CSV format. The number of dump files created or stored is limited to 10; to order more files, you have to delete one of the previous ones or wait until they will be deleted automatically. A newly created dump file is kept for 8 hours. If the request period is more than a day or there are too many events then several files will be generated and each file will contain no more than 100,000 events. File contains columns with the following information - 'event_time', 'job_id', 'from_email', 'email', 'status', 'delivery_status', 'metadata', 'destination_response', 'user_agent', 'url', 'ip', 'tags' and 'project_id' (for accounts with projects enabled). You can change the fields and include 'subject' field using 'dump_fileds' parameter.

Request body (application/json):

- `start_time` (string, required) — Date and time in YYYY-MM-DD hh:mm:ss format, specifying period start time. Data is stored for up to 32 days, depending on your tariff.
- `end_time` (string) — Date and time in YYYY-MM-DD hh:mm:ss format, specifying period end time (non-inclusive).
- `limit` (integer) — Maximum number of events returned (default is 50). If this value is over 100 000, several files will be created, each having 100 000 events maximum.
- `all_projects` (boolean, default: False) — For accounts with projects enabled, the value all_projects=true allows to fetch data for all existing projects.
- `filter` (object) — An object with the properties of the event dump filter.
  - `job_id` (string) — Job identifier returned earlier by [email/send](https://docs.unione.io/en/web-api-ref#email-send) method.
  - `status` (string, enum: sent, delivered, opened, clicked, unsubscribed, subscribed, soft_bounced, hard_bounced, spam) — Email status. Possible values are:   __accepted__ — the message has been accepted, but not sent yet.  __sent__ — the message has been sent, but not delivered yet.  __delivered__ — the message has been delivered.  __opened__ — the message has been delivered and read.  __clicked__ — the message has been delivered, read, and at least one of the links in email has been clicked.  __unsubscribed__ — the message has been delivered to the recipient and read, but then the recipient unsubscribed.  __subscribed__ — the message has been delivered to the recipient and read, but then the recipient unsubscribed and subscribed again.  __soft_bounced__ — temporary delivery failure. UniOne will try to deliver the message during 48 hours.  __hard_bounced__ — failed to deliver the message, there will be no delivery attempts.  __spam__ — the message has been delivered, but it was reported as spam by the recipient.
  - `delivery_status` (string) — UniOne internal detailed delivery status, you can pass several values at once, comma-separated. Some possible values are:    __err_user_unknown__ -- email address doesn't exist;   __err_user_inactive__ -- email address isn't used anymore;   __err_will_retry__ -- email was temporary rejected, delivery will be retried later;   __err_mailbox_discarded__ -- email address was active earlier, but now it's deleted;   __err_mailbox_full__ -- mailbox is full;   __err_spam_rejected__ -- email was rejected as a spam;   __err_blacklisted__ -- email was rejected because sender IP or sender domain is found in a black list;   __err_too_large__ -- email size is over limit, according to recipient's server;   __err_unsubscribed__ -- email was unsubscribed;   __err_unreachable__ -- numerous delivery failures lead to mark this email address as permanently unavailable;   __err_skip_letter__ -- sending has been canceled because the email address is temporarily unavailable;   __err_domain_inactive__ -- the domain does not accept mail or does not exist;   __err_destination_misconfigured__ -- the domain does not accept mail due to incorrect settings on the recipient’s side, and the server’s response contains information about a cause that can be fixed (for example, an inoperative blacklist is used, etc.);   __err_delivery_failed__ -- delivery failed due to other reasons;   __err_spam_skipped__ -- sending has been canceled because the campaign has been blocked as a spam;   __err_lost__ -- the message was not sent due to inconsistency of its parts or it has been lost because of the failure on our side. The sender needs to re-send the letter on his own, since the original has not been saved;    We reserve the right to change or add internal delivery statuses as we need, so the following list is provided as an example only, without any description: ok_sent, ok_delivered, ok_read, ok_link_visited, ok_unsubscribed, ok_resubscribed, ok_spam_folder, ok_fbl, not_sent, skip_dup_unreachable, skip_dup_temp_unreachable, skip_dup_mailbox_full, err_spam_removed, err_resend, err_unknown, err_retry_letter, err_src_invalid, err_dest_invalid, err_not_available, err_internal, err_no_dns, err_no_smtp, err_giveup.
  - `email` (string) — Recipient email address
  - `email_from` (string) — Sender email address
  - `domain` (string) — Recipient domain
  - `campaign_id` (string) — Campaign identifier, unsigned decimal integer or UUID up to 128-bit, passed in metadata with name "campaign_id" (name is configurable thru support).
- `dump_fields` (array of string) — An array of strings containing the names of columns you need in your report, in your preferred order. If the 'dump_fields' array is missing or empty, a default field list and order will be applied. Allowed values, in their default order, are - 'project_id', 'event_time', 'job_id', 'from_email', 'email', 'status', 'delivery_status', 'metadata', 'destination_response', 'user_agent', 'url', 'ip', 'tags'. For maximum security, the 'subject' field is not included by default, but you can add it by explicitly including in the 'dump_fields' array.
- `aggregate` (string) — Allows you to obtain aggregated statistics for a given time period. The two allowed values are:<ul><li>__day_status__ - fetch aggregated statistics (the filter value must be missing or empty, as filters are not allowed with this option); <li>__an empty string__ - used by default, event_dump/create works as if the aggregate parameter is omitted.
- `delimiter` (string) — Field delimiter, can be set to either  ',' or ';', defaults to  ','.
- `format` (string, default: csv) — File format, either “csv” (default) or “csv_gzip”.

Response 200: Method call has succeeded.

- `status` (string, required; enum: success) — "success" string
- `dump_id` (string, required) — Dump identifier, used to call the [event-dump/get](https://docs.unione.io/en/web-api-ref#event-dump-get) method.

Response default: Error occured.

## POST /event-dump/get.json

Returns dump properties for a given identifier

Request body (application/json):

- `dump_id` (string, required) — Dump identifier received by the method [event-dump/create](https://docs.unione.io/en/web-api-ref#event-dump-create).

Response 200: Dump information returned successfully.

- `status` (string, required; enum: success) — "success" string
- `event_dump` (object, required) — An object with the properties of the event dump.
  - `dump_id` (string, required) — Dump ID received by the method [event-dump/create](https://docs.unione.io/en/web-api-ref#event-dump-create).
  - `dump_status` (string, required) — Task status, possible values are:<ul><li>__queued__ - the task is in the queue, processing is not started yet;<li>__in_process__ - the request is being processed;<li>__ready__ - the task is finished, dump file is ready for download;<li>__failed__ -  processing failed due to an internal error.</ul>
  - `files` (array of object) — An array of objects, each representing a file, ready for download. You may start downloading everything listed in “files” even if "dump_status" is still "in_process". If there are no events, according to the specified parameters, an empty array will be returned.
    - `url` (string, required) — Use this unique URL to download the requested dump file (either .csv or .csv.gz, depending on your request).
    - `size` (integer, required) — File size.

Response default: Error occured.

## POST /event-dump/list.json

This method does not require any parameters; returns the full list of existing dumps.

Request body (application/json):


Response 200: List returned successfully.

- `status` (string, required; enum: success) — "success" string
- `event_dumps` (array of object, required) — An array of objects describing event dumps. Each object is similar to 'event_dump' object returned by the [event-dump/get](https://docs.unione.io/en/web-api-ref#event-dump-get) method.
  - `dump_id` (string, required) — Dump ID received by the method [event-dump/create](https://docs.unione.io/en/web-api-ref#event-dump-create).
  - `dump_status` (string, required) — Task status, possible values are:<ul><li>__queued__ - the task is in the queue, processing is not started yet;<li>__in_process__ - the request is being processed;<li>__ready__ - the task is finished, dump file is ready for download;<li>__failed__ -  processing failed due to an internal error.</ul>
  - `files` (array of object) — An array of objects, each representing a file, ready for download. You may start downloading everything listed in “files” even if "dump_status" is still "in_process". If there are no events, according to the specified parameters, an empty array will be returned.
    - `url` (string, required) — Use this unique URL to download the requested dump file (either .csv or .csv.gz, depending on your request).
    - `size` (integer, required) — File size.

Response default: Error occured.

## POST /event-dump/delete.json

Removes dump from queue or storage.

Request body (application/json):

- `dump_id` (string, required) — Dump identifier, obtained via the [event-dump/create](https://docs.unione.io/en/web-api-ref#event-dump-create) method.

Response 200: Dump deleted successfully.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
