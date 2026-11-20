# UniOne API errors

A failed call answers an HTTP status other than 200 and `{"status": "error", "code": <API code>, "message": "..."}`. Fix 4xx requests; retry 429 and 5xx with backoff. Source: [API reference](https://docs.unione.io/en/web-api-ref#api-errors).

| HTTP | Code | Meaning and fix |
|---|---|---|
| 401 | 101 | **API key is not passed or empty.** Make sure you have passed correct X-API-KEY header or 'api_key' JSON parameter. |
| 401 | 102 | **Invalid key '$apiKey'.** Use correct [user API-key](https://cp.unione.io/en/user/info/api) or [project API key](https://cp.unione.io/en/user/project). |
| 403 | 105 | **API is turned OFF.** You can turn API on [here](https://cp.unione.io/en/user/info/api). |
| 403 | 106 | **User is inactive.** To solve this problem, [contact support](https://cp.unione.io/en/support). |
| 400 | 111 | **JSON parsing error.** Check your JSON request syntax. |
| 401 | 114 | **The user has not been found.** Please send the request to the host you have been registered at, us1.unione.io or eu1.unione.io. |
| 400 | 118 | **No DNS TXT records found.** Add a DNS verification record to your domain with values returned by domain/get-dns-records. |
| 500 | 120 | **Internal DKIM validation error.** Please [contact support](https://cp.unione.io/en/support). |
| 400 | 121 | **Timeout searching domain.** DNS request has timed out. Please make sure your DNS provider is online and try again later. |
| 400 | 122 | **DKIM record not found (almost the same as 120).** Please add to your domain a DKIM record with key returned by domain/get-dns-records method. |
| 400 | 123 | **DKIM record malformed.** You should properly setup DKIM for your domain. |
| 400 | 124 | **DKIM record does not match expected.** Seems like you have changed the record. While it's technically correct, it doesn't match the one we expect. You should use DKIM key returned by domain/get-dns-records method. |
| 400 | 125 | **There are several different DKIM keys in the DNS entry.** Please setup the DKIM record for your domain properly. |
| 400 | 126 | **There are other non-DKIM record types present in the DNS record.** Please add a DKIM record for your domain with a key returned by domain/get-dns-records API method. |
| 400 | 127 | **Main domain DKIM record limit reached.** A maximum of 10 DKIM records are allowed per primary domain. |
| 400 | 129 | **Unknown DKIM validation error with reason distinct to the ones from 120-124 errors.** Please check that you have correctly added a DKIM record with key returned by domain/get-dns-records method and try again. Please [contact support](https://cp.unione.io/en/support) if the error still occurs. |
| 400 | 130 | **The domain is not allowed according to Registry policy.** Please use another domain. |
| 500 | 150 | **An unknown internal error occurred.** Unknown error occurred. Please try again later or [contact support](https://cp.unione.io/en/support). |
| 413 | 199 | **Request is too large.** The data in request should be no more than 10 MB. |
| 400 | 201 | **The message body is missing.** Check that your message body is being passed properly. |
| 400 | 202 | **Sender email is missing.** Enter the sender email. |
| 400 | 203 | **Email subject is missing.** Enter the subject. |
| 400 | 204 | **Email recipients are passed improperly.** Make sure that the recipient's list is passed as an array where each recipient is an array with obligatory 'email' parameter. |
| 400 | 205 | **Invalid sender email.** Make sure the parameter is passed properly. |
| 400 | 206 | **Sender email is not verified.** To avoid this error please use an email on a [verified domain](https://docs.unione.io/en/web-api-ref#domain). |
| 400 | 207 | **MIME file type is incorrect.** Check the file and the file type again. |
| 400 | 208 | **Invalid attachment filename. Forbidden symbol '$symbol'.** Rename files with the forbidden symbols. |
| 400 | 209 | **The attached file names are duplicated.** Rename files with the same names. |
| 400 | 210 | **Inline attachment names are duplicated.** Rename files with the same names. |
| 400 | 211 | **Invalid inline attachment filename. Forbidden symbol '$symbol'.** Rename files with the forbidden symbols. |
| 400 | 212 | **Recipients passed improperly ('substitutions' array is not set).** The possible maximum substitutions number has been exceeded or substitutions have incorrect filetype (string/integer is allowed). |
| 400 | 213 | **Invalid or non-existent custom_backend_id.** Please enter a valid 'custom_backend_id' parameter. |
| 403 | 215 | **The user is not allowed to send.** Try contacting [support](https://cp.unione.io/en/support). |
| 400 | 216 | **Recipients passed improperly.** 'Metadata' value should be a string or integer. Array for 'metadata' key is expected. |
| 400 | 217 | **Too many metadata fields passed.** Maximum 10 metadata fields allowed. |
| 400 | 218 | **Recipients passed improperly.** Metadata key length should be less than 64. |
| 400 | 219 | **Recipients passed improperly.** Metadata value length should less than 1024. |
| 400 | 220 | **Metadata key should not be blank.** Make sure the metadata key is passed. |
| 400 | 221 | **The <body> tag does not exist in the request or is invalid.** Add the html &lt;body&gt; tag inside the &lt;html&gt; tag. The &lt;body&gt; tag is required to display HTML content. |
| 400 | 223 | **The body is missing in the attachments 'content' or the void is transferred.** Add the 'content' and specify a value for it. |
| 400 | 224 | **Substitution name should contain only latin characters, numbers, "_" character and start with a letter.** Make sure the substitution name is passed correctly. |
| 400 | 228 | **Passing 'smtp_pool_id' requires passing 'custom_backend_id' also.** Make sure the 'custom_backend_id' is passed. |
| 400 | 229 | **Custom backend domain or tracking domain required for sending.** Make sure the custom backend domain or tracking domain is passed. |
| 400 | 230 | **Only default backend or tracking domain required for sending.** Make sure the default backend or tracking domain is passed. |
| 400 | 227 | **Invalid or non-existent 'smtp_pool_id'.** Please enter a valid 'smtp_pool_id' parameter. |
| 400 | 303 | **Events list contains an unsupported value or the event is not supported.** Verify that the event list is entered correctly. |
| 400 | 304 | **Webhook with the specified URL has not been found.** Make sure the URL is passed correctly. |
| 400 | 305 | **URL is not passed.** Make sure the URL is passed correctly. |
| 400 | 601 | **Template has not been found.** Check the passed template id. |
| 400 | 602 | **The template name is missing.** Check the passed template name. |
| 400 | 603 | **Template name passed in the request already belongs to another template.** Use another name for this template. |
| 400 | 604 | **Maximum number of templates has been reached.** Delete already created templates to create new ones. The number of templates is limited to 10000. |
| 400 | 701 | **Cause not found.** Invalid reason for blocking email. Please [contact support](https://cp.unione.io/en/support). |
| 403 | 901 | **Sending is blocked because limit is reached.** Each user has a maximum daily limit for sending to prevent abuse. This limit increases automatically in case of good delivery and is reset each night. You can smoothly increase amount of daily sending or you can contact support and ask for manual limit increase. |
| 403 | 902 | **Sending limit for free tariff is reached.** Wait till next day or switch to paid tariff. |
| 403 | 903 | **On free tariff you can send only to your own domains with confirmed verification record or checked emails.** Please [confirm ownership](https://docs.unione.io/en/web-api-ref#domain-validate-verification-record) of all domains you want to send emails to or switch tariff to the paid one. |
| 403 | 904 | **Insufficient funds. Credit card transaction failure.** Please try another card or [contact support](https://cp.unione.io/en/support) to resolve the situation. |
| 403 | 905 | **You have reached the limit of emails included in your subscription plan.** Usually tariff allows paid overage. In this case it's prohibited, possibly due to unpaid invoice. Please check that all invoices are paid or [contact support](https://cp.unione.io/en/support) to solve the problem. |
| 400 | 906 | **Exceeded the daily email reset limit.** You have used the entire available block reset limit. Try it tomorrow or [contact support](https://cp.unione.io/en/support) to increase the limit. |
| 500 | 908 | **Internal error, project owner not found.** Please [contact support](https://cp.unione.io/en/support). |
| 400 | 1000 | **Missing recipient address.** Specify the recipient address. |
| 400 | 1001 | **Invalid recipient address value.** Please enter a valid recipient address. |
| 400 | 1002 | **Missing sender address.** Specify the sender address. |
| 400 | 1003 | **Sender address not verified.** Verify the sender domain address. |
| 400 | 1004 | **Invalid sender address value.** Please enter a valid sender address. |
| 400 | 1005 | **Sender name is too long.** The sender name must be shorter. Please correct this value. |
| 400 | 1006 | **Exceeded the daily limit of the email/subscribe method call.** Try to repeat the call the next day. |
| 400 | 1007 | **Sender domain is not confirmed.** Use an address from a confirmed domain. |
| 400 | 1100 | **Missing domain name.** Specify the domain to be verified. |
| 400 | 1101 | **Invalid domain value.** Please enter a valid domain value. |
| 400 | 1102 | **Error in 'domain' field. Sending emails from the domain example.ru is prohibited.** Please use another domain. |
| 400 | 1103 | **Error in 'domain' field. Public free domains are not allowed.** Use only your own domains. |
| 400 | 1200 | **Missing domain name.** Specify the domain for validating. |
| 400 | 1201 | **Invalid domain value.** Please enter a valid domain value. |
| 400 | 1202 | **Domain is not registered in UniOne.** Make a domain/get-dns-records method call. |
| 400 | 1301 | **Invalid domain value.** Specify the domain to be verified. |
| 400 | 1302 | **Invalid limit value.** The value of limit must be an integer in the range of 1 - 100. |
| 400 | 1303 | **Invalid offset value.** The value of offset must be greater than or equal to 0. |
| 400 | 1304 | **Invalid offset value type.** The value of offset must be an integer. |
| 400 | 1305 | **Invalid limit value type.** The value of limit must be an integer. |
| 400 | 4300 | **Sandbox domain is not available for projects.** Use the account API key. |
| 400 | 1350 | **Error in 'domain' field. This value should not be blank.** Make sure the 'domain' is passed. |
| 400 | 1351 | **Error in 'domain' field. This value 'XXXXX' is not a valid domain.** Please enter a valid domain value. |
| 400 | 1352 | **Error in 'domain' field. You don't have domain 'gmail.com' added.** Make sure the 'domain' is passed. |
| 400 | 1353 | **Error in 'domain' field. Unable to delete the sandbox domain.** Please use another domain. |
| 400 | 1400 | **Missing domain name.** Specify the domain for validating. |
| 400 | 1401 | **Invalid or non-existent domain.** Either you have mistyped the domain name and should correct it or DNS changes have not yet propagated through DNS and you should wait a couple of hours and try again. There should be A, AAAA or MX record for domain. |
| 400 | 1402 | **Domain is not registered in UniOne.** Please call domain/get-dns-records method for domain to be registered. |
| 400 | 1506 | **Error in 'headers' field. This value should have object type.** Please check your JSON and use object for 'headers' field, not array or string or whatever. |
| 400 | 1507 | **Error in 'headers' field. This container should contain over 50 elements.** Please limit 'headers' to no more than 50 elements. |
| 400 | 1508 | **Error in 'template_id' field. There is no template with this ID.** Make sure the template ID is correct. |
| 400 | 1510 | **Error in 'body.html' field. The value should have a string type.** Use string type for 'body.html' parameter. |
| 400 | 1511 | **Error in 'body.plaintext' field. The value should have a string type.** Use string type for 'body.plaintext' parameter. |
| 400 | 1512 | **Error in 'body.amp' field. The value should have a string type.** Use string type for 'body.amp' parameter. |
| 400 | 1516 | **Error in 'body.html' field. Substitutions contain invalid values.** Check the correct substitutions in the 'body.html' field. |
| 400 | 1517 | **Error in 'body.plaintext' field.  Substitutions contain invalid values.** Check the correct substitutions in the 'body.plaintext' field. |
| 400 | 1518 | **Error in 'body.amp' field.  Substitutions contain invalid values.** Check the correct substitutions in the 'body.amp' field. |
| 400 | 1519 | **Error in 'reply_to' field. The value should have a string type.** Use string type for 'reply_to' parameter. |
| 400 | 1520 | **Error in 'reply_to' field. Invalid email.** Check if the email is correct. |
| 400 | 1521 | **Error in 'from_name' field. The value should have a string type.** Use string type for 'from_name' parameter. |
| 400 | 1522 | **Error in 'subject' field. The value should have a string type.** Use string type for 'subject' parameter. |
| 400 | 1523 | **Error in 'template_engine' field. Invalid value, template_engine could be one of 'simple', 'liquid', 'velocity' or 'none'.** Please pass one of the following values: 'simple', 'liquid', 'velocity' or 'none'. |
| 400 | 1524 | **Error in 'recipients' field. This container should contain over 500 elements.** Please limit 'recipients' to no more than 500 elements. |
| 400 | 1525 | **Error in 'options.send_at' field.** Make sure the date and time of the scheduled sending is no more than 24 hours in advance. |
| 400 | 1526 | **Error in 'headers["X-UNIONE-Template-Engine"]' field. Invalid value, headers[\"X-UNIONE-Template-Engine\"] could be one of 'simple', 'liquid', 'velocity' or 'none'.** Please pass only one of the following values: 'velocity', 'liquid', 'simple' or 'none'. |
| 400 | 1527 | **Error in 'headers["X-UNIONE-Global-Language"]' field. Language is not allowed.** Please pass only one of 'be', 'de', 'en', 'es', 'fr', 'it', 'kz', 'ru', 'pl', 'pt', 'ua' values. |
| 400 | 1528 | **Error in 'global_language' field. Language is not allowed.** Please pass only one of 'be', 'de', 'en', 'es', 'fr', 'it', 'kz', 'ru', 'pl', 'pt', 'ua' values. |
| 400 | 1529 | **Error in 'options.send_at' field. This value should be greater than Aug NN, 2023, 3:10 PM.** Make sure the datetime is passed correctly. |
| 400 | 1530 | **Error in 'options.send_at' field. This value should be of type string or this value is not a valid datetime.** Use string type for 'options.send_at' parameter. Make sure the datetime is passed correctly. |
| 400 | 1532 | **This collection should contain 4 elements or less.** Please limit tags to no more than 4 elements. |
| 400 | 1533 | **Error in 'tags' field. You can not create any more tags. Max tags number is 10000** Delete already created tags to create new ones. The number of tags is limited to 10000. |
| 400 | 1534 | **One or more tags is too long, max. 100 characters.** The tags must be shorter. Please correct this value. |
| 400 | 1535 | **One or more tags contains invalid symbols.** Make sure the tags is passed correctly. |
| 400 | 1537 | **Error in 'bypass_global' field. 'bypass_global' should be equal to 1.** Set parameter value to 1. |
| 400 | 1538 | **Error in 'bypass_unsubscribed' field. 'bypass_unsubscribed' usage is prohibited without 'allow_skip_unsubscribe' flag.** [contact support](https://cp.unione.io/en/support) to set the flag. |
| 400 | 1539 | **Error in 'bypass_complained' field. 'bypass_complained' usage is prohibited without 'allow_skip_unsubscribe' flag.** [contact support](https://cp.unione.io/en/support) to set the flag. |
| 400 | 1540 | **Error in 'metadata' field. The maximum allowable 'metadata' size is 4000 bytes.** Metadata value size should less than 4000 bytes. |
| 400 | 1541 | **Error in 'global_metadata' field. The maximum allowable 'global_metadata' size is 4000 bytes.** Metadata value size should less than 4000 bytes. |
| 400 | 1542 | **Error in 'metadata and global_metadata' field. The maximum allowable 'global_metadata' and 'metadata' size is 4000 bytes.** Metadata value size should less than 4000 bytes. |
| 400 | 1543 | **Error in 'global_metadata.campaign_id' field. This value should be of type string.** Use string type for 'global_metadata.campaign_id' parameter. |
| 400 | 1544 | **Error in 'metadata.campaign_id' field. This value should be of type string.** Use string type for 'metadata.campaign_id' parameter. |
| 400 | 1545 | **Error in 'metadata.campaign_id' field. Value ' ' is not a valid number or uuid** Make sure the 'metadata.campaign_id' is passed correctly. |
| 400 | 1546 | **Error in 'subject' field.  Substitutions contain invalid values.** Check the correct substitutions in the 'subject' field. |
| 400 | 1547 | **Error in 'from_name' field.  Substitutions contain invalid values.** Check the correct substitutions in the 'from_name' field. |
| 400 | 1549 | **Error in 'options.unsubscribe_url' field. Invalid substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1550 | **Error in 'options' field. The value should have an object type.** Use object type for the 'options' parameter. |
| 400 | 1551 | **Error in 'metadata or global_metadata collection' field. The value parameter must be a string.** Use string type for 'metadata' and 'global_metadata' parameters. |
| 400 | 1554 | **Error in 'headers['Cc']' field. The number of emails in "Cc" must not exceed 'N'.** Make sure that the number of emails in 'headers['Cc']' is not exceeded. |
| 400 | 1555 | **Error in 'headers['Cc']' field. Email in "Cc" must not differ from recipient emails.** Use only emails from the 'recipient' parameter. |
| 400 | 1556 | **Error in 'headers['Cc']' field. "Cc" header allows only with non empty "To" header.** Make sure that the 'headers['To']' is passed. |
| 400 | 1557 | **Error in 'headers['To']' field. The number of emails in "To" must not exceed %d.** Make sure that the number of emails in 'headers['To']' is not exceeded. |
| 400 | 1558 | **Error in 'headers['To']' field. Email in "To" must not differ from recipient emails.** Use only emails from the 'recipient' parameter. |
| 400 | 1559 | **Error in 'recipients' field. Email not exist in headers "To" or "Cc" or email domain is not confirmed** BCC may contain only addresses on your verified domain. |
| 400 | 1560 | **Error in 'recipients' field. Limit of 'recipients' must not be more then limit of sum of "To" and "Cc" emails.** Make sure that the number of emails in "To" and "Cc" headers is not exceeded. |
| 400 | 1561 | **Error in 'headers['Cc']' field. Header 'example' is not valid Cc.** Make sure the headers is passed correctly. |
| 400 | 1562 | **Error in 'headers['To']' field. Header 'example' is not valid To.** Make sure the headers is passed correctly. |
| 400 | 1565 | **Error in 'body.html' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1566 | **Error in 'subject' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1567 | **Error in 'from_name' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1568 | **Error in 'reply_to_name' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1569 | **Error in 'body.plaintext' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1570 | **Error in 'body.amp' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1571 | **Error in 'options.unsubscribe_url' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 1572 | **Error in 'idempotence_key' field. This value is too long. It should have 64 characters or less.** The key must be shorter. Please correct this value. |
| 400 | 1573 | **Error in 'idempotence_key' field. Error sending duplicate message with the same idempotence_key='xxxxxxxxxx'.** Make sure the key is correct. |
| 400 | 1574 | **Error in 'from_email' field. Denied 'from_email': example.com - use address from a confirmed domain.** To avoid this error please use an email on a verified domain. |
| 400 | 1575 | **User is not allowed to send.** Try contacting [support](https://cp.unione.io/en/support). |
| 400 | 1576 | **Error in 'subject' field. This value should not be blank.** Enter the subject. |
| 400 | 1577 | **Error in 'body' field. No message body passed.** Check that your message body is being passed properly. |
| 400 | 1578 | **Error in 'body.html' field. No valid <body> tag format: tag is not valid or do not exist.** Add the html &lt;body&gt; tag inside the &lt;html&gt; tag. The &lt;body&gt; tag is required to display HTML content. |
| 400 | 1579 | **Error in 'global_substitutions' field. Maximum 2 substitutions allowed.** The possible maximum substitutions number has been exceeded. |
| 400 | 1580 | **Error in 'global_substitutions' field. Substitution name should contain latin characters, numbers or '_' character and start with a letter.** Make sure the substitution name is passed correctly. |
| 400 | 1581 | **Error in 'globalSubstitutions[CompanyRef]' field. This value should satisfy at least one of the following constraints: [1] This value should be of type integer. [2] This value should be of type string.** This value should be a string or integer. |
| 400 | 1582 | **Error in 'global_metadata' field. This collection should contain 10 elements or less.** Maximum 10 metadata fields allowed. |
| 400 | 1583 | **Error in 'global_substitutions' field. Recipients passed improperly.** 'Metadata' value should be a string or integer. |
| 400 | 1584 | **Error in 'global_metadata' field. Global metadata key should not be blank.** Make sure the metadata key is passed. |
| 400 | 1585 | **Error in 'global_metadata' field. Global metadata key length should less than 64.** Make sure the metadata key is passed correctly. |
| 400 | 1586 | **Error in 'global_metadata' field. This value is too long.** It should have 1024 characters or less. |
| 400 | 1587 | **Error in 'force_send' field. No rights to use 'force_send' option.** Try contacting [support](https://cp.unione.io/en/support). |
| 400 | 1588 | **Error in 'skip_unsubscribe' field. No right for 'skip_unsubscribe = 1'. ** Try contacting [support](https://cp.unione.io/en/support). |
| 400 | 1590 | **Error in 'attachments.name' field. Invalid filename: 'IMG\/1'. Forbidden symbol '\/'.** Rename files with the forbidden symbols. |
| 400 | 1591 | **Error in 'attachments' field. Duplicated filename: 'IMG1'.** Rename files with the same names. |
| 400 | 1592 | **Error in 'attachments.content' field. No attachment content passed, attachment filename: IMG1.** Add the 'content' and specify a value for it. |
| 400 | 1593 | **Error in 'attachments.type' field. Mime type of file IMG1 is skipped or empty.** Check the file and the file type again. |
| 400 | 1594 | **Error in 'inline_attachments.name' field. Invalid filename: 'IMG\/1'. Forbidden symbol '\/'.** Rename files with the forbidden symbols. |
| 400 | 1595 | **Error in 'inline_attachments' field. Duplicated filename: 'IMG1'.** Rename files with the same names. |
| 400 | 1596 | **Error in 'inline_attachments.content' field. No attachment content passed, attachment filename: IMG1.** Add the 'content' and specify a value for it. |
| 400 | 1597 | **Error in 'inline_attachments.type' field. Mime type of file IMG1 is skipped or empty.** Check the file and the file type again. |
| 403 | 1598 | **Error in 'from_email' field. Sandbox domain in 'from_email' used with unconfirmed email 'test@example.com'.** To avoid this error please use only confirmed email addresses. |
| 403 | 1599 | **Error in 'from_email' field. The daily sending limit for the sandbox domain has been exceeded.** Try to repeat the call the next day. |
| 400 | 1606 | **Error in the 'send_enabled' field. This value should be of type bool.** Set parameter value to true or false only. |
| 400 | 1607 | **Error in 'custom_unsubscribe_url_enabled' field. This value should be of type bool.** Set parameter value to true or false only. |
| 400 | 1706 | **Error in 'project_api_key' field. One of the two properties ['project_api_key' or 'project_id'] is required.** Don't forget to send either project_id or project_api_key. |
| 400 | 1708 | **Error in the 'project_api_key' field. The value should have a string type.** Use string type for 'project_api_key'. |
| 400 | 1709 | **Error in the 'send_enabled' field. The value should have a bool type.** Set parameter value to true or false only. |
| 400 | 1710 | **Error in 'custom_unsubscribe_url_enabled' field. The value should have a bool type.** Set parameter value to true or false only. |
| 400 | 1721 | **Error in 'email_counter' field. This value should be of type int.** Use int type for 'email_counter' parameter. |
| 400 | 1722 | **Error in 'email_counter' field. This value should be equal to 0.** Set parameter value equal to 0. |
| 400 | 1723 | **Error in 'email_counter_limit' field. This value should be of type int.** Use int type for 'email_counter_limit' parameter. |
| 400 | 1724 | **Error in 'email_counter_limit' field. This value should be greater than or equal to 0.** Set parameter value greater than or equal to 0. |
| 400 | 1725 | **Error in 'email_counter_mode' field. This value should be of type bool.** Set parameter value to default or permanent only. |
| 400 | 1801 | **Error in 'project_api_key' field. One of the two properties ['project_api_key' or 'project_id'] is required.** Don't forget to send either project_id or project_api_key. |
| 400 | 1904 | **Error in 'project_id' field. This value is not valid. The value should contain digits only.** Use correct numbers-only format for 'project_id'. |
| 400 | 2306 | **Error in 'recipients' field. This value should not be blank.** Make sure the 'recipients' is passed. |
| 400 | 2307 | **Error in 'recipients' field. This value should be of type string.** Use string type for 'recipients' parameter. |
| 400 | 2500 | **Error in 'editor_type' field. 'html' is required.** Make sure the 'editor_type' field is passed 'html'. |
| 400 | 2501 | **The template was created in a visual editor.** Make sure the template is created in HTML editor. |
| 400 | 2502 | **Error in 'editor_type' field. This value should not be blank.** Pass 'html' in 'editor_type' field. |
| 400 | 2503 | **Error in 'id' field. There is no template with this ID.** Make sure the template ID is correct. |
| 400 | 2504 | **Error in 'headers' field. This value should have object type.** Please check your JSON and use object for 'headers' field, not array or string or whatever. |
| 400 | 2505 | **Error in 'headers' field. This container should contain 50 elements or less.** Please limit headers to no more than 50 elements. |
| 400 | 2514 | **Error in 'reply_to' field. This value should be of type string.** Use string type for 'reply_to' parameter. |
| 400 | 2515 | **Error in 'reply_to' field. This value is not a valid email address.** Check if the email is correct. |
| 400 | 2516 | **Error in 'template_engine' field. Invalid value, template_engine could be one of 'simple', 'liquid', 'velocity' or 'none'.** Please pass one of the following values: 'simple', 'liquid', 'velocity' or 'none'. |
| 400 | 2517 | **Error in 'subject' field. This value should be of type string.** Use string type for 'subject' parameter. |
| 400 | 2518 | **Error in 'subject' field. Substitutions contain invalid values.** Check the correct substitutions in the 'subject' field. |
| 400 | 2519 | **Error in 'from_name' field. This value should be of type string.** Use string type for 'from_name' parameter. |
| 400 | 2520 | **Error in 'from_name' field. Substitutions contain invalid values.** Check the correct substitutions in the 'from_name' field. |
| 400 | 2521 | **Error in 'from_name' field. Invalid velocity substitution format . Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 2522 | **Error in 'subject' field. Invalid velocity substitution format . Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 2523 | **Error in 'reply_to_name' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 2524 | **Error in 'options' field. This value should be of type string.** Use string type for 'options' parameter. |
| 400 | 2525 | **Error in 'options.unsubscribe_url' field. Invalid substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 2526 | **Error in 'options.unsubscribe_url' field. Invalid velocity substitution format. Substitution name in body should contain latin characters, numbers or '_' character and start with a letter".** Make sure the substitution name is passed correctly. |
| 400 | 2600 | **Error in 'limit' field. This value should be greater than or equal to 0.** Set parameter value greater than or equal to 0. |
| 400 | 2601 | **Error in 'limit' field. This value should be of type int.** Use int type for 'limit' parameter. |
| 400 | 2602 | **Error in 'offset' field. This value should be greater than or equal to 0.** Set parameter value greater than or equal to 0. |
| 400 | 2603 | **Error in 'offset' field. This value should be of type int.** Use int type for 'offset' parameter. |
| 400 | 2700 | **Error in 'url' field. This value should be of type string.** Use string type for 'url' parameter. |
| 400 | 2701 | **Error in 'url' field. This value should not be blank.** Make sure the URL is passed. |
| 400 | 2702 | **Error in 'offset' field. This value should be greater than or equal to 0.** Set parameter value greater than or equal to 0. |
| 400 | 2703 | **Error in 'eventFormat' field. The value you selected is not a valid choice.** Use format 'json_post' or 'json_post_gzip' only. |
| 400 | 2704 | **Error in 'deliveryInfo' field. 'delivery_info' value should be 1\0 either true\false.** Set parameter 'delivery_info'  value to 1\0 either true\false. |
| 400 | 2705 | **Error in 'singleEvent' field. 'single_event' value should be 1\0 either true\false.** Set parameter 'single_event' value to 1\0 either true\false. |
| 400 | 2706 | **Error in 'maxParallel' field. This value should be of type int.** Use int type for 'maxParallel' parameter. |
| 400 | 2707 | **Error in 'maxParallel' field. This value should be between 5 and 100.** Use a valid value of 5 to 100. |
| 400 | 2708 | **Error in 'events' field. This value should be of type array.** Use array type for 'events' parameter. |
| 400 | 2709 | **Error in 'events' field. This value should not be blank.** Use non-blank events. |
| 400 | 2710 | **Error in 'events' field. Field 'email_status' is required.** Add 'email_status' parameter. |
| 400 | 2711 | **Error in 'email_status' field. This value 'test' is not a valid email_status.** Add valid email statuses in the value. |
| 400 | 2712 | **Error in 'spam_block' field. This value 'test' is not a valid spam_block.** Add valid spam blocking events in the value. |
| 400 | 2713 | **Error in 'url' field. Webhook domain name not found.** Make sure the domain is passed correctly. |
| 400 | 2714 | **Error in 'status' field. Invalid value, status could be one of 'active' or 'disabled'.** Set status 'active' or 'disabled'. |
| 400 | 2715 | **Error in 'status' field. This value should be of type string.** Use string type for 'status' parameter. |
| 400 | 2800 | **Error in 'name' field. This value should not be blank.** Make sure the 'name' is passed. |
| 400 | 2801 | **Error in 'name' field. The value should have a string type.** Use string type for 'name' parameter. |
| 400 | 2802 | **Error in 'type' field. The value should have a string type.** Use string type for 'type' parameter. |
| 400 | 2803 | **Error in 'content' field. The value should have a string type.** Use string type for 'content' parameter. |
| 400 | 2804 | **The size of the 'content' field must not exceed 7MB.** Reduce the size of the 'content' field to 7MB (9786710 bytes in base64). |
| 400 | 2903 | **Error in 'all_projects' field. This value should be of type bool.** Set parameter value to true or false only. |
| 400 | 3003 | **Error in 'email' field. Email doesn't exist.** Email was not found in the suppression list. |
| 400 | 3004 | **Error in 'email' field. Email cannot be deleted.** Email cannot be removed from the suppression list. Probably because of the severe reason like 'blocked'. |
| 400 | 3103 | **Error in 'cause' field. This value should not be blank.** Make sure the 'cause' is passed. |
| 400 | 3106 | **Error in 'created' field. This value should be of type string.** Use string type for 'created' parameter. |
| 400 | 3107 | **Error in 'created' field. This value is not a valid datetime.** Make sure the datetime is passed correctly. |
| 400 | 3202 | **Error in 'source' field. This value should be of type string.** Use string type for 'source' parameter. |
| 400 | 3203 | **Error in 'source' field. Source 'test' not allowed.** Please pass only one of the available values. |
| 400 | 3204 | **Error in 'start_time' field. This value should be of type string.** Use string type for 'start_time' parameter. |
| 400 | 3205 | **Error in 'start_time' field. This value is not a valid datetime.** Make sure the datetime is passed correctly. |
| 400 | 3206 | **Error in 'cursor' field. This value should be of type string.** Use string type for 'cursor' parameter. |
| 400 | 3207 | **Error in 'cursor' field. Cursor 'test' not allowed.** Please pass only one of the available values. |
| 400 | 3208 | **Error in 'limit' field. This value should be of type int.** Use int type for 'limit' parameter. |
| 400 | 3209 | **Error in 'limit' field. This value should be greater than or equal to 0.** Set parameter value greater than or equal to 0. |
| 400 | 3300 | **Error in 'start_time' field. This value should not be blank.** Make sure the 'start_time' is passed. |
| 400 | 3301 | **Error in 'start_time' field. This value is not a valid datetime.** Make sure the datetime is passed correctly. |
| 400 | 3302 | **Error in 'end_time' field. This value is not a valid datetime.** Make sure the datetime is passed correctly. |
| 400 | 3303 | **Error in 'limit' field. This value should be positive.** Set parameter value greater than or equal to 0. |
| 400 | 3304 | **Error in 'format' field. Incorrect value of the event dump file format.** Use 'csv' or 'csv_gzip' format only. |
| 400 | 3305 | **Error in 'delimiter' field. Incorrect value of the event dump file delimiter.** Use 'delimiter' ';' or ',' only. |
| 400 | 3308 | **Error in 'all_projects' field. The user does not have the required roles.** Projects methods are disabled by default. To enable them,[contact support](https://cp.unione.io/en/support). |
| 400 | 3309 | **User can have no more than 10 event dumps at a time.** Delete already created dumps to create new ones. The number of dumps is limited to 10. |
| 400 | 3310 | **Error in 'start_time' field. The interval start date cannot be earlier than '$time'.** Make sure 'start_time' is in the allowed range. |
| 400 | 3311 | **Error in 'limit' field. This value should be of type integer.** Use int type for 'limit' parameter. |
| 400 | 3312 | **Error in 'delimiter' field. This value should be of type string.** Use string type for 'delimiter' parameter. |
| 400 | 3313 | **Error in 'format' field. This value should be of type string.** Use string type for 'format' parameter. |
| 400 | 3315 | **Error in 'aggregate' field. This value should be of type string.** Use string type for 'aggregate' parameter. |
| 400 | 3316 | **Error in 'filter' field.** Can not use filter with "aggregate" parameter. Please pass only one of the available parameter. |
| 400 | 3317 | **Error in 'dumpFields' field. This value should be of type array.** Use array type for 'dumpFields' parameter. |
| 400 | 3318 | **Error in 'dumpFields' field. Incorrect fields of the event dump.** Please pass only one of the available values. |
| 400 | 3319 | **Error in 'aggregate' field.** Invalid value, aggregate could be only 'day_status' or empty. Please pass only one of the available values. |
| 400 | 3400 | **Error in 'filter' field. This value should be of type object.** Please check your JSON and use object for 'filter' field, not array or string or whatever. |
| 400 | 3401 | **Error in 'filter.job_id' field. This value should be of type string.** Use string type for 'filter.job_id' parameter. |
| 400 | 3402 | **Error in 'filter.status' field. This value should be of type string.** Use string type for 'filter.status' parameter. |
| 400 | 3403 | **Error in 'filter.status' field. Status 'dfdfs' is invalid.** Please enter a valid 'filter.status' parameter. |
| 400 | 3404 | **Error in 'filter.email' field. This value should be of type string.** Use string type for 'filter.email' parameter. |
| 400 | 3405 | **Error in 'filter.email' field. This value 'ewrewrew@dsfdfdds' is not a valid email address.** Check if the email is correct. |
| 400 | 3406 | **Error in 'filter.email_from' field. This value should be of type string.** Use string type for 'filter.email_from' parameter. |
| 400 | 3407 | **Error in 'filter.email_from' field. This value 'bitko82@gmailcom' is not a valid email address.** Check if the email is correct. |
| 400 | 3408 | **Error in 'filter.domain' field. This value should be of type string.** Use string type for 'filter.domain' parameter. |
| 400 | 3409 | **Error in 'filter.domain' field. This value 'test' is not a valid domain.** Please enter a valid domain value. |
| 400 | 3410 | **Error in 'filter.domain' field. Domain 'gmail.com' different from the domain in the email.** Make sure the domain is passed correctly. |
| 400 | 3411 | **Error in 'filter.delivery_status' field. This value should be of type string.** Use string type for 'filter.delivery_status' parameter. |
| 400 | 3412 | **Error in 'filter.delivery_status' field. Status '63' is invalid.** Please enter a valid 'filter.delivery_status' parameter. |
| 400 | 3413 | **Error in 'filter.campaign_id' field. This value should be of type string.** Use string type for 'filter.campaign_id' parameter. |
| 400 | 3414 | **Error in 'filter.campaign_id' field. Value '340282366920938463463374607431768211255999' is invalid number.** The data in request should be no more than 128 bit. |
| 400 | 3700 | **This value should not be blank.** Make sure the 'tag_id' is passed. |
| 400 | 3701 | **This value should be of type int.** Use int type for 'tag_id' parameter. |
| 400 | 3800 | **Error in 'email' field. The maximum number of concurrent requests should not exceed 4.** Reduce the the numbers of concurrent requests to 4. |
| 400 | 3801 | **Error in 'email' field. This value should not be blank.** Make sure the email is passed. |
| 400 | 3802 | **Error in 'email' field. This value should be of type string.** Use string type for 'email' parameter. |
| 400 | 3803 | **Error in 'email' field. Exceeded the daily limit of the email-validation/single method call.** Try to repeat the call the next day. |
| 400 | 3900 | **Error in 'idempotence_key' field. This value should be of type string.** Use string type for 'idempotence_key' parameter. |
| 400 | 4000 | **The confirmed-email/create method is unavailable with a project API key.** Use the main account API key. |
| 400 | 4001 | **Error in 'email' field. This value should not be blank.** Pass an email address. |
| 400 | 4002 | **Error in 'email' field. This value should be of type string.** Use string type for 'email' parameter. |
| 400 | 4003 | **Error in 'email' field. This value is not a valid email address.** Pass a valid email address. |
| 400 | 4004 | **The email address is already in the list and is not confirmed.** Delete it and call confirmed-email/create again to send a new confirmation link. |
| 400 | 4005 | **The email address is already confirmed.** No action is required. |
| 400 | 4006 | **The confirmed email limit has been reached.** Delete an address before adding a new one. |
| 400 | 4100 | **The confirmed-email/delete method is unavailable with a project API key.** Use the main account API key. |
| 400 | 4101 | **Error in 'email' field. This value should not be blank.** Pass an email address. |
| 400 | 4102 | **Error in 'email' field. This value should be of type string.** Use string type for 'email' parameter. |
| 400 | 4103 | **Error in 'email' field. This value is not a valid email address.** Pass a valid email address. |
| 400 | 4104 | **The email address is not in the confirmed email list.** Use confirmed-email/list to get the current list. |
| 400 | 4200 | **The confirmed-email/list method is unavailable with a project API key.** Use the main account API key. |
