# UniOne API: Template

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /template/set.json

Creates or updates an email template.

Restrictions:
* The maximum request size is 10 MB.
* The number of templates is limited to 10000.

Request body (application/json):

- `template` (object, required) — Object with all the template properties.
  - `id` (string) — Template unique identifier. If you omit the "id" field then new template will be created. If you specify the "id" field, the system will try to find a template with the specified id and edit it.
  - `name` (string, required) — Template name.
  - `editor_type` (string, enum: html, visual) — Editor type, "html" or "visual". Default is "html". You can create a template with "visual" editor type only in web interface.
  - `template_engine` (string, enum: simple, velocity, liquid, none) — The [template engine](https://docs.unione.io/en/template-engines) for handling the substitutions(merge tags), "simple", "velocity", "liquid" or "none". Default value is "simple".
  - `global_substitutions` (object) — Object for passing the substitutions(merge tags) common for all recipients - e.g., company name. If the substitution names are duplicated in object "substitutions", the values of the variables will be taken from the object "substitutions". The substitutions can be used in the following parameters: <ul><li>body.html <li>body.plaintext <li>body.amp <li>subject <li>from_name <li>options.unsubscribe_url</ul>A substitution name can consist from latin characeters, numbers and "_" symbol, and should start with the letter.
  - `global_metadata` (object) — Object for passing the metadata common for all the recipients, such as "key": "value". Max key quantity: 10. Max key length: 64 symbols. Max value length: 1024 symbols. The metadata is returned by [webhook](https://docs.unione.io/en/web-api-ref#webhook). To group single emails into a campaign, you can use the system key 'campaign_id' with a value in the form of a non-negative decimal integer up to 128 bits or a UUID in the format 'c7703772-453e-4c77-a9ae-9a1b94051b5a'. Incorrect values will be treated as '0'.
  - `body` (object) — Contains HTML/plaintext/AMP parts of the email. Either html or plaintext part is required.
    - `html` (string) — HTML part of the email body
    - `plaintext` (string) — Plaintext part of the email body.
    - `amp` (string) — Optional [AMP](http://amp.dev/documentation/guides-and-tutorials/learn/email_fundamentals/) part of the email body.
  - `subject` (string) — Email subject.
  - `from_email` (string, required) — Sender's email.
  - `from_name` (string) — Sender's name.
  - `reply_to` (string) — Optional Reply-To email (in case it's different to sender's email)
  - `reply_to_name` (string) — Optional Reply-To name (if reply_to email is specified and you want to display not only this email but also the name)
  - `track_links` (integer, enum: 0, 1) — 1 = click tracking is on (default), 0 = click tracking is off. To use track_links = 0, you need to ask support to enable this feature.
  - `track_read` (integer, enum: 0, 1) — 1 = read tracking is on (default), 0=read tracking is off. To use track_read = 0, you need to ask support to enable this feature.
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

Response 200: Template set successfully.

- `status` (string, required; enum: success) — "success" string
- `template` (object, required) — Object with all the template properties.
  - `id` (string) — Template unique identifier. If you omit the "id" field then new template will be created. If you specify the "id" field, the system will try to find a template with the specified id and edit it.
  - `name` (string, required) — Template name.
  - `editor_type` (string, enum: html, visual) — Editor type, "html" or "visual". Default is "html". You can create a template with "visual" editor type only in web interface.
  - `template_engine` (string, enum: simple, velocity, liquid, none) — The [template engine](https://docs.unione.io/en/template-engines) for handling the substitutions(merge tags), "simple", "velocity", "liquid" or "none". Default value is "simple".
  - `global_substitutions` (object) — Object for passing the substitutions(merge tags) common for all recipients - e.g., company name. If the substitution names are duplicated in object "substitutions", the values of the variables will be taken from the object "substitutions". The substitutions can be used in the following parameters: <ul><li>body.html <li>body.plaintext <li>body.amp <li>subject <li>from_name <li>options.unsubscribe_url</ul>A substitution name can consist from latin characeters, numbers and "_" symbol, and should start with the letter.
  - `global_metadata` (object) — Object for passing the metadata common for all the recipients, such as "key": "value". Max key quantity: 10. Max key length: 64 symbols. Max value length: 1024 symbols. The metadata is returned by [webhook](https://docs.unione.io/en/web-api-ref#webhook). To group single emails into a campaign, you can use the system key 'campaign_id' with a value in the form of a non-negative decimal integer up to 128 bits or a UUID in the format 'c7703772-453e-4c77-a9ae-9a1b94051b5a'. Incorrect values will be treated as '0'.
  - `body` (object) — Contains HTML/plaintext/AMP parts of the email. Either html or plaintext part is required.
    - `html` (string) — HTML part of the email body
    - `plaintext` (string) — Plaintext part of the email body.
    - `amp` (string) — Optional [AMP](http://amp.dev/documentation/guides-and-tutorials/learn/email_fundamentals/) part of the email body.
  - `subject` (string) — Email subject.
  - `from_email` (string, required) — Sender's email.
  - `from_name` (string) — Sender's name.
  - `reply_to` (string) — Optional Reply-To email (in case it's different to sender's email)
  - `reply_to_name` (string) — Optional Reply-To name (if reply_to email is specified and you want to display not only this email but also the name)
  - `track_links` (integer, enum: 0, 1) — 1 = click tracking is on (default), 0 = click tracking is off. To use track_links = 0, you need to ask support to enable this feature.
  - `track_read` (integer, enum: 0, 1) — 1 = read tracking is on (default), 0=read tracking is off. To use track_read = 0, you need to ask support to enable this feature.
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

Response default: Error occured.

## POST /template/get.json

Gets template properties by it's id.

Request body (application/json):

- `id` (string, required) — Template id.

Response 200: Template returned successfully.

- `status` (string, required; enum: success) — "success" string
- `template` (object, required) — Object with all the template properties.
  - `id` (string) — Template unique identifier. If you omit the "id" field then new template will be created. If you specify the "id" field, the system will try to find a template with the specified id and edit it.
  - `name` (string, required) — Template name.
  - `editor_type` (string, enum: html, visual) — Editor type, "html" or "visual". Default is "html". You can create a template with "visual" editor type only in web interface.
  - `template_engine` (string, enum: simple, velocity, liquid, none) — The [template engine](https://docs.unione.io/en/template-engines) for handling the substitutions(merge tags), "simple", "velocity", "liquid" or "none". Default value is "simple".
  - `global_substitutions` (object) — Object for passing the substitutions(merge tags) common for all recipients - e.g., company name. If the substitution names are duplicated in object "substitutions", the values of the variables will be taken from the object "substitutions". The substitutions can be used in the following parameters: <ul><li>body.html <li>body.plaintext <li>body.amp <li>subject <li>from_name <li>options.unsubscribe_url</ul>A substitution name can consist from latin characeters, numbers and "_" symbol, and should start with the letter.
  - `global_metadata` (object) — Object for passing the metadata common for all the recipients, such as "key": "value". Max key quantity: 10. Max key length: 64 symbols. Max value length: 1024 symbols. The metadata is returned by [webhook](https://docs.unione.io/en/web-api-ref#webhook). To group single emails into a campaign, you can use the system key 'campaign_id' with a value in the form of a non-negative decimal integer up to 128 bits or a UUID in the format 'c7703772-453e-4c77-a9ae-9a1b94051b5a'. Incorrect values will be treated as '0'.
  - `body` (object) — Contains HTML/plaintext/AMP parts of the email. Either html or plaintext part is required.
    - `html` (string) — HTML part of the email body
    - `plaintext` (string) — Plaintext part of the email body.
    - `amp` (string) — Optional [AMP](http://amp.dev/documentation/guides-and-tutorials/learn/email_fundamentals/) part of the email body.
  - `subject` (string) — Email subject.
  - `from_email` (string, required) — Sender's email.
  - `from_name` (string) — Sender's name.
  - `reply_to` (string) — Optional Reply-To email (in case it's different to sender's email)
  - `reply_to_name` (string) — Optional Reply-To name (if reply_to email is specified and you want to display not only this email but also the name)
  - `track_links` (integer, enum: 0, 1) — 1 = click tracking is on (default), 0 = click tracking is off. To use track_links = 0, you need to ask support to enable this feature.
  - `track_read` (integer, enum: 0, 1) — 1 = read tracking is on (default), 0=read tracking is off. To use track_read = 0, you need to ask support to enable this feature.
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

Response default: Error occured.

## POST /template/list.json

Returns the list of all or some templates of the account.

You can iterate thru large list using "offset" and "limit" parameters. When less than "limit" templates are returned then the end of list is reached.

Request body (application/json):

- `limit` (integer, default: 50) — Limits the number of templates returned, default is 50.
- `offset` (integer, default: 0) — Index of the first template in the list, starting with 0.

Response 200: Template list returned successfully.

- `status` (string, required; enum: success) — "success" string
- `templates` (array of object, required) — Array of template objects.
  - `id` (string, required) — Template unique identifier.
  - `name` (string, required) — Template name.
  - `editor_type` (string, enum: html, visual) — Editor type, "html" or "visual". Default is "html". You can create a template with "visual" editor type only in web interface.
  - `template_engine` (string, enum: simple, velocity, liquid, none) — The [template engine](https://docs.unione.io/en/template-engines) for handling the substitutions(merge tags), "simple", "velocity", "liquid" or "none". Default value is "simple".
  - `global_substitutions` (object) — Object for passing the substitutions(merge tags) common for all recipients - e.g., company name. If the substitution names are duplicated in object "substitutions", the values of the variables will be taken from the object "substitutions". The substitutions can be used in the following parameters: <ul><li>body.html <li>body.plaintext <li>body.amp <li>subject <li>from_name <li>options.unsubscribe_url</ul>A substitution name can consist from latin characeters, numbers and "_" symbol, and should start with the letter.
  - `global_metadata` (object) — Object for passing the metadata common for all the recipients, such as "key": "value". Max key quantity: 10. Max key length: 64 symbols. Max value length: 1024 symbols. The metadata is returned by [webhook](https://docs.unione.io/en/web-api-ref#webhook). To group single emails into a campaign, you can use the system key 'campaign_id' with a value in the form of a non-negative decimal integer up to 128 bits or a UUID in the format 'c7703772-453e-4c77-a9ae-9a1b94051b5a'. Incorrect values will be treated as '0'.
  - `body` (object, required) — Contains HTML/plaintext/AMP parts of the email. Either html or plaintext part is required.
    - `html` (string) — HTML part of the email body
    - `plaintext` (string) — Plaintext part of the email body.
    - `amp` (string) — Optional [AMP](http://amp.dev/documentation/guides-and-tutorials/learn/email_fundamentals/) part of the email body.
  - `subject` (string) — Email subject.
  - `from_email` (string, required) — Sender's email.
  - `from_name` (string) — Sender's name.
  - `reply_to` (string) — Optional Reply-To email (in case it's different to sender's email)
  - `reply_to_name` (string) — Optional Reply-To name (if reply_to email is specified and you want to display not only this email but also the name)
  - `track_links` (integer, enum: 0, 1) — 1 = click tracking is on (default), 0 = click tracking is off. To use track_links = 0, you need to ask support to enable this feature.
  - `track_read` (integer, enum: 0, 1) — 1 = read tracking is on (default), 0=read tracking is off. To use track_read = 0, you need to ask support to enable this feature.
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
  - `created` (string, required) — Template creation date and time in UTC timezone in format "YYYY-MM-DD hh:mm:ss"
  - `user_id` (integer, required) — Unique user identifier.
  - `project_id` (string) — Unqiue project identifier, ASCII string up to 36 characters long.
  - `project_name` (string) — Project name, unique for user account.

Response default: Error occured.

## POST /template/delete.json

Deletes a template by id.

Request body (application/json):

- `id` (string, required) — Template id.

Response 200: Template deleted successfully.

- `status` (string, required; enum: success) — "success" string

Response default: Error occured.
