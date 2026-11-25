# UniOne API: Email

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /email/send.json

Sends an email or a bunch of emails

While sending you can provide substitutions (merge tags), use a template, turn on read or click tracking, etc.

Restrictions:
* maximum request size is 10 MB
* maximum number of recipients is 500
* The symbol '/' is not allowed in attachment names

If the list of recipients contains invalid, non-existent, duplicate, or unsubscribed emails, those emails will be returned in the output parameter failed_emails, and the email will be sent to all other valid emails addresses. If all the emails addresses fall into failed_emails, sending will not be carried out and API error 204 will be returned.

Request body (application/json):

- `message` (object, required) — Object containing all message properties.
  - `recipients` (array of object, required) — Contains recipient emails, substitutions(merge tags) and metadata.
    - `email` (string, required) — Recipient email
    - `substitutions` (object) — Object to pass the substitutions(merge tags) for the recipient (e.g. recipient name, discount code, password change link, etc. See [Template engines](https://docs.unione.io/en/template-engines)). The substitutions can be used in the following parameters:<ul><li>body.html <li>body.plaintext <li>body.amp <li>subject <li>from_name <li>headers["List-Unsubscribe"] <li>options.unsubscribe_url </ul>  A substitution name can consist from latin characters, numbers and "_" symbol, and should start with the letter. There's a special substitution "to_name" which is used to put recipent's name like "Name Surname" to include it to SMTP header "To" in the form "Name Surname &lt;email@example.com&gt;". The "to_name" length is limited to 78 symbols.
    - `metadata` (object) — Object for passing the metadata, such as "key": "value". Max key quantity: 10. Max key length: 64 symbols. Max value length: 1024 symbols. The metadata is returned by [webhook](https://docs.unione.io/en/web-api-ref#webhook) and [event-dump](https://docs.unione.io/en/web-api-ref#event-dump) methods. If you pass strign up to 128 bit with "campaign_id" field name (name is configurable thru support), it will be considered as campaign identifier in statistics.
  - `template_id` (string) — Optional identifier of the template that had been created by [template/set](https://docs.unione.io/en/web-api-ref#template-set) method. If template_id is passed then fields from the template are used instead of missed email/send parameters. E.g. if "body" parameter in email/send is omitted, "body" from template will be used. If "subject" in email/send is omitted, "subject" from template will be used.
  - `tags` (array of string) — An array of strings. The maximum string length is 100 characters. You can include up to 4 strings which must be unique. No more than 10 000 tags are allowed per project; if you try to add more, email/send will return an error. You may use tags to categorize emails by your own criteria, and they will be passed along by event-dump methods.
  - `skip_unsubscribe` (integer, enum: 0, 1) — Whether to skip or not appending default unsubscribe footer. 1=skip, 0=append, default is 0. You should [ask support](https://cp.unione.io/en/support) to approve usage of skip_unsubscribe=1. [Read more](https://docs.unione.io/en/unsubscribe-link).
  - `global_language` (string) — The language of the unsubscribe footer and unsubscribe page. Languages supported are: "be", "de", "en", "es", "fr", "it", "pl", "pt", "ru", "ua", "kz".
  - `template_engine` (string, enum: simple, velocity, liquid, none) — The [template engine](https://docs.unione.io/en/template-engines) for handling the substitutions(merge tags), "simple", "velocity", "liquid" or "none". Default value is "simple".
  - `global_substitutions` (object) — Object for passing the substitutions(merge tags) common for all recipients - e.g., company name. If the substitution names are duplicated in object "substitutions", the values of the variables will be taken from the object "substitutions". The substitutions can be used in the following parameters: <ul><li>body.html <li>body.plaintext <li>body.amp <li>subject <li>from_name <li>options.unsubscribe_url</ul>A substitution name can consist from latin characeters, numbers and "_" symbol, and should start with the letter.
  - `global_metadata` (object) — Object for passing the metadata common for all the recipients, such as "key": "value". Max key quantity: 10. Max key length: 64 symbols. Max value length: 1024 symbols. The metadata is returned by [webhook](https://docs.unione.io/en/web-api-ref#webhook). To group single emails into a campaign, you can use the system key 'campaign_id' with a value in the form of a non-negative decimal integer up to 128 bits or a UUID in the format 'c7703772-453e-4c77-a9ae-9a1b94051b5a'. Incorrect values will be treated as '0'.
  - `body` (object, required) — Contains HTML/plaintext/AMP parts of the email. Either html or plaintext part is required.
    - `html` (string) — HTML part of the email body
    - `plaintext` (string) — Plaintext part of the email body.
    - `amp` (string) — Optional [AMP](http://amp.dev/documentation/guides-and-tutorials/learn/email_fundamentals/) part of the email body.
  - `subject` (string, required) — Email subject.
  - `from_email` (string) — Sender's email. Required only if template_id parameter is empty.
  - `from_name` (string) — Sender's name.
  - `reply_to` (string) — Optional Reply-To email (in case it's different to sender's email)
  - `reply_to_name` (string) — Optional Reply-To name (if reply_to email is specified and you want to display not only this email but also the name)
  - `track_links` (integer, enum: 0, 1) — 1 = click tracking is on (default), 0 = click tracking is off. To use track_links = 0, you need to ask support to enable this feature.
  - `track_read` (integer, enum: 0, 1) — 1 = read tracking is on (default), 0=read tracking is off. To use track_read = 0, you need to ask support to enable this feature.
  - `bypass_global` (integer, enum: 0, 1) — (allowed values 0 or 1, default 0) If set to 1, the global unavailability list will be ignored. Even if the address was found to be unreachable while sending other UniOne users' emails, or its owner has issued complaints, the message will still be sent. The setting may be ignored for certain addresses.
  - `bypass_unavailable` (integer, enum: 0, 1) — (allowed values 0 or 1, default 0) If set to 1, the current user's or project's unavailability list will be ignored. Works only if bypass_global is set to 1.
  - `bypass_unsubscribed` (integer, enum: 0, 1) — (allowed values 0 or 1, default 0) If set to 1, the current list of unsubscribed addresses for this account or project will be ignored. Works only if bypass_global is set to 1. The setting is available only for users that have been granted the right to omit the unsubscribe link (to request, please contact [support](https://cp.unione.io/en/support)).
  - `bypass_complained` (integer, enum: 0, 1) — (allowed values 0 or 1, default 0) If set to 1, the user's or project's complaint list will be ignored. Works only if bypass_global is set to 1. The setting is available only for users that have been granted the right to omit the unsubscribe link (to request, please contact [support](https://cp.unione.io/en/support)).
  - `idempotence_key` (string) — A string of up to 64 characters containing a unique message key. This can be used to prevent occasional message duplicates. If you send another API request with the same message key within the next minute, it will be declined. We can generate a message key for each letter automatically; to enable this option, please contact our [tech support](https://cp.unione.io/en/support).
  - `headers` (object) — Contains email headers, maximum 50. Only headers with “X-” name prefix are accepted, all other are ignored, for example X-UNIONE-Global-Language, X-UNIONE-Template-Engine. Standard headers "To," "CC," and "BCC" are passed without the "X-." Yet, they are processed in a particular way and, as a result, have a number of restrictions. You can find more details about it [here](https://docs.unione.io/en/cc-and-bcc). If our support have approved omitting standard unsubscription block for you, you can also pass List-Unsubscribe, List-Subscribe, List-Help, List-Owner, List-Archive, In-Reply-To and References headers.
    - `X-UNIONE-Global-Language` (string) — The language of the unsubscribe footer and unsubscribe page. Languages supported are: "be", "de", "en", "es", "fr", "it", "pl", "pt", "ru", "ua", "kz".
    - `X-UNIONE-Template-Engine` (string) — The template engine for handling the substitutions(merge tags), “simple”, “velocity”, “liquid” or “none”. Default value is “simple”. Has a priority over the value allowed in the “template_engine” parameter.
  - `attachments` (array of object) — Optional array of attachments
    - `type` (string, required) — Attachment type, see [MIME](https://en.wikipedia.org/wiki/MIME). If unsure, use "application/octet-stream".
    - `name` (string, required) — Attachment name in the format: "name.extension". When multiple attachments are passed, their names must be unique. The symbol ‘/’ is not allowed in attachment names.
    - `content` (string, required) — File contents in [base64](https://en.wikipedia.org/wiki/Base64). Maximum file size 7MB (9786710 bytes in base64).
  - `inline_attachments` (array of object) — Optional array of inline attachments, e.g. for including images in email instead of loading them from external URL.
    - `type` (string, required) — Attachment type, see [MIME](https://en.wikipedia.org/wiki/MIME). If unsure, use "application/octet-stream".
    - `name` (string, required) — Attachment content id. For example, "name"="IMAGECID1" should be referenced in HTML like &lt;img src="cid:IMAGECID1"&gt;.
    - `content` (string, required) — File contents in [base64](https://en.wikipedia.org/wiki/Base64). Maximum file size 7MB (9786710 bytes in base64).
  - `options` (object) — Additional message options.
    - `send_at` (string) — Date and time in "YYYY-MM-DD hh:mm:ss" format in the UTC timezone. Allows schedule sending up to 24 hours in advance.
    - `unsubscribe_url` (string) — Custom unsubscribe link. Read more [here](https://docs.unione.io/en/unsubscribe-link).
    - `custom_backend_id` (integer) — Backend-domain identifier to send message with. If custom_backend_id is not set, default one for your account/project will be used. You can pay for one or more dedicated IPs and use this option.
    - `smtp_pool_id` (string) — SMTP pool identifier to send message with. Usually you don't need to pass this parameter because correct smtp_pool_id is selected automatically based on the default one for your account/project or according to custom_backend_id parameter.

Response 200: Email successfully accepted for sending.

- `status` (string, required; enum: success) — "success" string
- `job_id` (string, required) — Job identifier, might be useful for investigating errors.
- `emails` (array of string) — Array of recipients emails successfully accepted for sending.
- `failed_emails` (object) — Object with emails rejected for sending as property names and their statuses as property values, e.g.: {"email1@gmail.com": "temporary_unavailable"}. Possible statuses:<ul><li>__unsubscribed__ - specified email is unsubscribed;<li>__invalid__ - the email does not exist or has been entered incorrectly;<li>__duplicate__ - the email already exists in the request, email duplicating is prevented;<li>__temporary_unavailable__ - the email address is unavailable. This means that over the next three days sending to this address will return an error. Email may be temporarily unavailable due to several reasons, e.g.: <ol><li>a previous email has been rejected by the recipient's server for spam;<li>the recipient's mailbox is full or is not used;<li>recipient's domain does not accept mail;<li>sending server was rejected due to blacklisting;</ol><li>__permanent_unavailable__ - the email address is permanently unavailable or unsubscribed globally.<li>__complained__ -  the recipient reported spam in the previous emails;<li>__blocked__ -  sending to the email is prohibited by administration of UniOne.</ul>We may added new statuses in the future.

Response default: Error occured.

## POST /email/subscribe.json

Sends an email with (re)subscribe link.

This method allows subscription renewal by a former subscriber who has previously unsubscribed, or who is blocked because of complaints. This method sends an email with a new subscription link to a former subscriber. Once the recipient clicks the link, their subscription status is restored.
There is a default restriction that limits this method to being used once a day. If you need to resubscribe more often, please ask support about it.

Request body (application/json):

- `from_email` (string, required) — Sender’s email on a confirmed domain. (Field alias "email_address_from" is supported, too).
- `from_name` (string, required) — Sender’s name. (Field alias "name_from" is supported, too).
- `to_email` (string, required) — Recipient’s email. (Field alias "email_address_to" is supported, too).

Response 200: Email successfully accepted for sending.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
