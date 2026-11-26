# UniOne API: Webhook

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /webhook/set.json

Sets or edits a [webhook](https://docs.unione.io/en/web-api-ref#webhook), i.e. an event notification handler.

Request body (application/json):

- `url` (string, required) — URL that will receive the notification when an event occurs. The URL should be unique for a user or a project. Only ASCII characters are supported for now in URL, please convert to [Punycode](https://en.wikipedia.org/wiki/Punycode) if you need to use non-ASCII characters.
- `status` (string, enum: active, disabled, stopped; default: active) — Webhook status, "active" by default. "disabled" means that webhook has been disabled by the user, "stopped" means that webhook has been stopped by the system after 24h of failed calls (with minimum of 10 distinct events).
- `event_format` (string, enum: json_post, json_post_gzip; default: json_post) — Notification format. "json_post"(default) or "json_post_gzip".
- `delivery_info` (integer, enum: 0, 1; default: 0) — Shall detailed delivery info be returned(1) or not(0). When it's 1, the information about SMTP response and internal delivery status is returned for "hard_bounced" and "soft_bounced" email statuses; the user agent, recipient IP address, detected geo fields, device info detected from the user agent (device type and brand, OS name, browser or email client name) and traffic_type (human, machine, protected or unknown) are returned for "opened" and "clicked" statuses; URL is returned for "clicked" status. For "delivered", "soft_bounced" and "hard_bounced" statuses UniOne may also return sender_ip, the IP address of the SMTP server that sent the message, if available.
- `single_event` (integer, enum: 0, 1; default: 0) — 0=several event notifications can be reported in single webhook call, 1=only single event can be reported in one call (not recommended).
- `max_parallel` (integer, default: 10) — Maximum quantity of permitted parallel queries to your server. The more your server can handle - the better.
- `events` (object) — Object containing events to notify of.
  - `spam_block` (array of string) — If present then spam block events will be reported. Should contain single array element with "*" string.
  - `email_status` (array of string) — If present then email status change events will be reported. Contains names of statuses to notify of.

Response 200: Webhook set successfully.

- `status` (string, required; enum: success) — "success" string
- `object` (object, required) — Object with all the webhook properties.
  - `id` (integer, required) — Webhook unique identifier.
  - `url` (string, required) — Webhook URL.
  - `status` (string, required; enum: active, disabled, stopped; default: active) — Webhook status, "active" by default. "disabled" means that webhook has been disabled by the user, "stopped" means that webhook has been stopped by the system after 24h of failed calls (with minimum of 10 distinct events).
  - `event_format` (string, required; enum: json_post, json_post_gzip; default: json_post) — Notification format. "json_post"(default) or "json_post_gzip".
  - `delivery_info` (integer, required; enum: 0, 1; default: 0) — Shall detailed delivery info be returned(1) or not(0). When it's 1, the information about SMTP response and internal delivery status is returned for "hard_bounced" and "soft_bounced" email statuses; the user agent, recipient IP address, detected geo fields, device info detected from the user agent (device type and brand, OS name, browser or email client name) and traffic_type (human, machine, protected or unknown) are returned for "opened" and "clicked" statuses; URL is returned for "clicked" status. For "delivered", "soft_bounced" and "hard_bounced" statuses UniOne may also return sender_ip, the IP address of the SMTP server that sent the message, if available.
  - `single_event` (integer, required; enum: 0, 1; default: 0) — 0=several event notifications can be reported in single webhook call, 1=only single event can be reported in one call (not recommended).
  - `max_parallel` (integer, required; default: 10) — Maximum quantity of permitted parallel queries to your server. The more your server can handle - the better.
  - `updated_at` (string) — Webhook properties last update date and time in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.
  - `events` (object) — Object containing events to notify of.
    - `spam_block` (array of string) — If present then spam block events will be reported. Should contain single array element with "*" string.
    - `email_status` (array of string) — If present then email status change events will be reported. Contains names of statuses to notify of.

Response default: Error occured.

### Callback `callback-format`: POST to your URL

- `auth` (string, required) — MD5-hash of the message body, in which the value "auth" is replaced by api key of the user/project; with this field the recipient of the notification can both authenticate and verify the notification integrity
- `events_by_user` (array of object, required) — Array with only one element, containing events of a user/project.
  - `user_id` (integer, required) — Unique user identifier.
  - `project_id` (string) — Project identifier, present only if webhook was registered for the project using project API key.
  - `project_name` (string) — Project name, present only if webhook was registered for the project using project API key.
  - `events` (array of object, required) — Array of events reported by webhook.
    - `event_name` (string, enum: transactional_email_status, transactional_spam_block) — Type of event data contained in event_data field, either "transactional_email_status" or "transactional_spam_block".
    - `event_data` (object) — Object with different event properties depending on "event_name". Below you can see all the properties, "transactional_email_status"-related first and then "transactional_spam_block"-related.
      - `job_id` (string) — Job identifier returned earlier by [email/send](https://docs.unione.io/en/web-api-ref#email-send) method. Property exists only if event_name="transactional_email_status".
      - `metadata` (object) — Metadata passed in [email/send](https://docs.unione.io/en/web-api-ref#email-send) method in recipients.metadata or global_metadata properties. This property exists only if event_name="transactional_email_status".
      - `email` (string) — Recipient's email. This property exists only if event_name="transactional_email_status".
      - `status` (string, enum: sent, delivered, opened, clicked, unsubscribed, subscribed, soft_bounced, hard_bounced, spam) — Email delivery status. This property exists only if event_name="transactional_email_status". Possible values are:   __accepted__ — the message has been accepted, but not sent yet.  __sent__ — the message has been sent, but not delivered yet.  __delivered__ — the message has been delivered. It can be changed to “opened”, “clicked”, “unsubscribed”, “subscribed” or “spam”.  __opened__ — the message has been delivered and read. It can be changed to “clicked”, “unsubscribed”, “subscribed” or “spam”.  __clicked__ — the message has been delivered, read, and at least one of the links in email has been clicked. It can be changed to “unsubscribed”, “subscribed” or “spam”.  __unsubscribed__ — the message has been delivered to the recipient and read, but then the recipient unsubscribed. It can be changed to “subscribed”.  __subscribed__ — the message has been delivered to the recipient and read, but then the recipient unsubscribed and subscribed again. It can be changed to “unsubscribed”.  __soft_bounced__ — temporary delivery failure. UniOne will try to deliver the message during 48 hours. In case of success the status changes to “delivered”, in case of failure to deliver during 48 hours message status changes to “hard_bounced”.  __hard_bounced__ — failed to deliver the message, there will be no delivery attempts. It's a final status. There are a lot of possible reasons, you can use SMTP response from delivery_info.destination_response field or UniOne internal reason classification from delivery_info.delivery_status field to analyze the reason.  __spam__ — the message has been delivered, but it was reported as spam by the recipient. UniOne can receive and process the spam complaint from several domains, including msn.com, outlook.com, hotmail.com, live.com, ukr.net, yahoo.com, aol.com using [FBL](https://en.wikipedia.org/wiki/Feedback_loop_(email)).
      - `event_time` (string) — Event date & time in UTC time zone in "YYYY-MM-DD hh:mm:ss" format. This property exists only if event_name="transactional_email_status".
      - `url` (string) — URL for "opened" and "clicked" statuses. This property exists only if event_name="transactional_email_status".
      - `delivery_info` (object) — Object with detailed delivery info.Event date & time in UTC time zone in "YYYY-MM-DD hh:mm:ss" format. This property exists only if webhook has delivery_info proeprty set to 1 and event_name="transactional_email_status".
        - `delivery_status` (string) — UniOne internal detailed delivery status. Some possible values are:    __err_user_unknown__ -- email address doesn't exist;   __err_user_inactive__ -- email address isn't used anymore;   __err_will_retry__ -- email was temporary rejected, delivery will be retried later;   __err_mailbox_discarded__ -- email address was active earlier, but now it's deleted;   __err_mailbox_full__ -- mailbox is full;   __err_spam_rejected__ -- email was rejected as a spam;   __err_blacklisted__ -- email was rejected because sender IP or sender domain is found in a black list;   __err_too_large__ -- email size is over limit, according to recipient's server;   __err_unsubscribed__ -- email was unsubscribed;   __err_unreachable__ -- numerous delivery failures lead to mark this email address as permanently unavailable;   __err_skip_letter__ -- sending has been canceled because the email address is temporarily unavailable;   __err_domain_inactive__ -- the domain does not accept mail or does not exist;   __err_destination_misconfigured__ -- the domain does not accept mail due to incorrect settings on the recipient’s side, and the server’s response contains information about a cause that can be fixed (for example, an inoperative blacklist is used, etc.);   __err_delivery_failed__ -- delivery failed due to other reasons;   __err_spam_skipped__ -- sending has been canceled because the campaign has been blocked as a spam;   __err_lost__ -- the message was not sent due to inconsistency of its parts or it has been lost because of the failure on our side. The sender needs to re-send the letter on his own, since the original has not been saved;    We reserve the right to change or add internal delivery statuses as we need, so the following list is provided as an example only, without any description: ok_sent, ok_delivered, ok_read, ok_link_visited, ok_unsubscribed, ok_resubscribed, ok_spam_folder, ok_fbl, not_sent, skip_dup_unreachable, skip_dup_temp_unreachable, skip_dup_mailbox_full, err_spam_removed, err_resend, err_unknown, err_retry_letter, err_src_invalid, err_dest_invalid, err_not_available, err_internal, err_no_dns, err_no_smtp, err_giveup.
        - `destination_response` (string) — SMTP response.
        - `user_agent` (string) — User agent of recipient. Present only if detected for "clicked" and "opened" statuses.
        - `device_type` (string, enum: desktop, mobile, tablet, other, unknown) — Recipient's device type, detected from the user agent. Present for "clicked" and "opened" statuses; equals "unknown" if the device type couldn't be detected.
        - `device_brand` (string) — Recipient's device brand, detected from the user agent. Present for "clicked" and "opened" statuses if detected. For device_type "mobile" and "tablet" it's always present and equals "unknown" when the brand couldn't be detected.
        - `os_name` (string) — Name of the operating system of the recipient's device, detected from the user agent. Present for "clicked" and "opened" statuses; equals "unknown" if the OS couldn't be detected.
        - `browser_name` (string) — Name of the browser the email was opened in, detected from the user agent. Present for "clicked" and "opened" statuses only if a browser was detected, so it never comes together with email_client_name.
        - `email_client_name` (string) — Name of the email client application the email was opened in, detected from the user agent. Present for "clicked" and "opened" statuses only if an email client was detected, so it never comes together with browser_name.
        - `traffic_type` (string, enum: human, machine, protected, unknown) — Traffic quality for "opened" and "clicked" statuses. "human" means a recognized browser or email client without machine signs; "machine" means a bot, link scanner or security proxy; "protected" means a mailbox/OS privacy proxy where a human action cannot be confirmed (Apple Mail Privacy Protection / iCloud Private Relay, Gmail Image Proxy — Apple MPP is protected, not machine); "unknown" means the user agent is missing, broken or not recognized.
        - `ip` (string) — Recipient's IP address. Present only if detected for "clicked" and "opened" statuses.
        - `country_code` (string) — ISO 3166-1 alpha-2 country code detected from recipient IP. Present for "clicked" and "opened" statuses.
        - `country` (string) — Country detected from recipient IP. Present for "clicked" and "opened" statuses.
        - `city` (string) — City detected from recipient IP. Present for "clicked" and "opened" statuses.
        - `sender_ip` (string) — IP address of the SMTP server that sent the message. Present only for "delivered", "soft_bounced" and "hard_bounced" statuses, if available.
      - `block_time` (string) — Spam block date & time in UTC time zone in "YYYY-MM-DD hh:mm:ss" format. This property exists only if event_name="transactional_spam_block".
      - `block_type` (string, enum: one_smtp, all_smtp) — Spam block type, either single or multiple sending SMTP. For single sending SMTP block in common pool UniOne retries several other SMTPs. This property exists only if event_name="transactional_spam_block".
      - `domain` (string) — Domain that blocked sending. This property exists only if event_name="transactional_spam_block".
      - `SMTP_blocks_count` (integer) — Number of sending SMTPs blocked. This property exists only if event_name="transactional_spam_block".
      - `domain_status` (string, enum: blocked, unblocked) — Whether it's a block or unblock event. This property exists only if event_name="transactional_spam_block".

## POST /webhook/get.json

Gets properties of a [webhook](https://docs.unione.io/en/web-api-ref#webhook).

Request body (application/json):

- `url` (string, required) — Webhook URL.

Response 200: Webhook returned successfully.

- `status` (string, required; enum: success) — "success" string
- `object` (object, required) — Object with all the webhook properties.
  - `id` (integer, required) — Webhook unique identifier.
  - `url` (string, required) — Webhook URL.
  - `status` (string, required; enum: active, disabled, stopped; default: active) — Webhook status, "active" by default. "disabled" means that webhook has been disabled by the user, "stopped" means that webhook has been stopped by the system after 24h of failed calls (with minimum of 10 distinct events).
  - `event_format` (string, required; enum: json_post, json_post_gzip; default: json_post) — Notification format. "json_post"(default) or "json_post_gzip".
  - `delivery_info` (integer, required; enum: 0, 1; default: 0) — Shall detailed delivery info be returned(1) or not(0). When it's 1, the information about SMTP response and internal delivery status is returned for "hard_bounced" and "soft_bounced" email statuses; the user agent, recipient IP address, detected geo fields, device info detected from the user agent (device type and brand, OS name, browser or email client name) and traffic_type (human, machine, protected or unknown) are returned for "opened" and "clicked" statuses; URL is returned for "clicked" status. For "delivered", "soft_bounced" and "hard_bounced" statuses UniOne may also return sender_ip, the IP address of the SMTP server that sent the message, if available.
  - `single_event` (integer, required; enum: 0, 1; default: 0) — 0=several event notifications can be reported in single webhook call, 1=only single event can be reported in one call (not recommended).
  - `max_parallel` (integer, required; default: 10) — Maximum quantity of permitted parallel queries to your server. The more your server can handle - the better.
  - `updated_at` (string) — Webhook properties last update date and time in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.
  - `events` (object) — Object containing events to notify of.
    - `spam_block` (array of string) — If present then spam block events will be reported. Should contain single array element with "*" string.
    - `email_status` (array of string) — If present then email status change events will be reported. Contains names of statuses to notify of.

Response default: Error occured.

## POST /webhook/list.json

List all or some [webhooks](https://docs.unione.io/en/web-api-ref#webhook) (event notification handlers) of a user or a project.

Request body (application/json):

- `limit` (integer) — Limits the number of webhooks returned. 50 is recommended.
- `offset` (integer, default: 0) — Index of the first webhook in the list, starting with 0.

Response 200: Webhook list returned successfully.

- `status` (string, required; enum: success) — "success" string
- `objects` (array of object, required) — Array of webhooks objects.
  - `id` (integer, required) — Webhook unique identifier.
  - `url` (string, required) — Webhook URL.
  - `status` (string, required; enum: active, disabled, stopped; default: active) — Webhook status, "active" by default. "disabled" means that webhook has been disabled by the user, "stopped" means that webhook has been stopped by the system after 24h of failed calls (with minimum of 10 distinct events).
  - `event_format` (string, required; enum: json_post, json_post_gzip; default: json_post) — Notification format. "json_post"(default) or "json_post_gzip".
  - `delivery_info` (integer, required; enum: 0, 1; default: 0) — Shall detailed delivery info be returned(1) or not(0). When it's 1, the information about SMTP response and internal delivery status is returned for "hard_bounced" and "soft_bounced" email statuses; the user agent, recipient IP address, detected geo fields, device info detected from the user agent (device type and brand, OS name, browser or email client name) and traffic_type (human, machine, protected or unknown) are returned for "opened" and "clicked" statuses; URL is returned for "clicked" status. For "delivered", "soft_bounced" and "hard_bounced" statuses UniOne may also return sender_ip, the IP address of the SMTP server that sent the message, if available.
  - `single_event` (integer, required; enum: 0, 1; default: 0) — 0=several event notifications can be reported in single webhook call, 1=only single event can be reported in one call (not recommended).
  - `max_parallel` (integer, required; default: 10) — Maximum quantity of permitted parallel queries to your server. The more your server can handle - the better.
  - `updated_at` (string) — Webhook properties last update date and time in UTC timezone in "YYYY-MM-DD hh:mm:ss" format.
  - `events` (object) — Object containing events to notify of.
    - `spam_block` (array of string) — If present then spam block events will be reported. Should contain single array element with "*" string.
    - `email_status` (array of string) — If present then email status change events will be reported. Contains names of statuses to notify of.

Response default: Error occured.

## POST /webhook/delete.json

Deletes an event notification handler

You can also temporarily deactivate webhook without deleting it by setting it's status to "disabled" in [webhook/set](https://docs.unione.io/en/web-api-ref#webhook-set) method.

Request body (application/json):

- `url` (string, required) — Webhook URL.

Response 200: Webhook deleted successfully.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
