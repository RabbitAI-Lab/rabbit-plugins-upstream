# UniOne API: Domain

Generated from the UniOne Web API spec. Every method: `POST https://api.unione.io/en/transactional/api/v1<path>?platform=skill` with the `X-API-KEY` header and a JSON body (`?platform=skill`: the channel of the skills in the statistics).

## POST /domain/get-dns-records.json

Returns info on domain DNS setup for using with UniOne.

In order to send emails you have to confirm that you own the domain that you are going to send emails from and setup DKIM signature for the domain. This method allows you to register your domain in UniOne and generate verification record and DKIM key, or return previously generated ones if domain is already registered.
You should add then DNS records like this to all of the domains you want to confirm:

`@             IN TXT "unione-validate-hash=483bb362ebdbeedd755cfb1d4d661"`

`us._domainkey IN TXT "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDo7"`

`@             IN TXT  "v=spf1 include:spf.unione.io ~all"`

`_dmarc        IN CNAME "example.com.dmarc.unione.io."`


- First record value should contain "verification-record" field returned by get-dns-records method "as is".
- Second record value should contain "dkim" field value after "v=DKIM1; k=rsa; p=". Mind the name of this record! "us._domainkey." prefix is important for DKIM selector of UniOne to work properly.
- Third record contains optional, but very recommended SPF entry. It is not returned by the method. Probably you already have one, then just add append include:spf.unione.io right after v=spf1.
- Fourth record is a CNAME of the "_dmarc" host to the "dmarc" field value: UniOne then publishes the DMARC policy of the domain. If the domain already has its own DMARC TXT record, keep it instead.

Syntax requirements of different DNS providers may differ:
- sometimes it's necesarry to put full domain name instead of @ sign.
- some providers require add TTL value (like 3600)
- some providers don't require quotes for enclosing values
Please check requirements of your provider and advice your users to do it.

Request body (application/json):

- `domain` (string, required) — Domain to get DNS records for.

Response 200: Domain DNS info returned successfully.

- `status` (string, required; enum: success) — "success" string
- `domain` (string, required) — Domain to get DNS records for.
- `verification-record` (string, required) — Record to be added "as is" to verify ownership of this domain.
- `dkim` (string, required) — DKIM signature for the domain. This property contains only the key part, you should prepend it with "v=DKIM1; k=rsa; p=" for the TXT record to be valid.
- `dmarc` (string) — Target of the CNAME record for the "_dmarc" host of the domain.

Response default: Error occured.

## POST /domain/validate-verification-record.json

Triggers verification record validation for domain.

If you get 200 OK then it means the validation process started succesfully, but it doesn't mean the verification record is valid. You should check later verification-record.status field returned by [domain/list](https://docs.unione.io/en/web-api-ref#domain-list) method to get the result. Please read more [here](https://docs.unione.io/en/web-api-ref#domain).

Request body (application/json):

- `domain` (string, required) — Domain to validate verification record for.

Response 200: Verification record is valid.

- `status` (string, required; enum: success) — "success" string
- `message` (string, required) — Debug message.

Response default: Error occured or record is invalid.

## POST /domain/validate-dkim.json

Validates DKIM record for domain.

If you get 200 OK then it means the validation process started succesfully, but it doesn't mean the DKIM record is valid. You should check later dkim.status field returned by [domain/list](https://docs.unione.io/en/web-api-ref#domain-list) method to get the result. Please read more [here](https://docs.unione.io/en/web-api-ref#domain).

Request body (application/json):

- `domain` (string, required) — Domain to validate DKIM record for.

Response 200: DKIM record validation has started successfully.

- `status` (string, required; enum: success) — "success" string
- `message` (string, required) — Debug message.

Response default: Error occured or record is invalid.

## POST /domain/list.json

Returns a list of all registered domains for user or project, together with statuses of last validations.

Returns last status of ownership validation and DKIM validation for each domain. Read more [here](https://docs.unione.io/en/web-api-ref#domain).

Request body (application/json):

- `domain` (string) — Optional domain name if you want to get the status of single domain only.
- `limit` (integer, default: 50) — Limits the number of domains returned. Default is 50.
- `offset` (integer, default: 0) — Index of the first domain in the list, starting with 0.

Response 200: The list of the registered domains returned successfully.

- `status` (string, required; enum: success) — "success" string
- `domains` (array of object, required) — Array of objects describing domains.
  - `domain` (string, required) — Domain name.
  - `verification-record` (object, required) — Object describing verification record value and status.
    - `value` (string) — Record to be added "as is" to verify ownership of this domain.
    - `status` (string, enum: confirmed, unconfirmed) — Only domains with "confirmed" verification record are allowed as sender domains.
  - `dkim` (object, required) — Object describing DKIM record value and status.
    - `key` (string) — DKIM signature for the domain. This property contains only the key part, you should prepend it with "k=rsa, p=" part for the record to be valid (see [domain/get-dns-records](https://docs.unione.io/en/web-api-ref#domain-get-dns-records)).
    - `status` (string, enum: active, inactive) — Only domains with "active" DKIM record are allowed as sender domains.

Response default: Error occured.

## POST /domain/get-sandbox-domain.json

Creates a sandbox domain for the account or returns the existing one.

Returns an account sandbox domain that is ready for use in the `from_email` field of [email/send](https://docs.unione.io/en/web-api-ref#email-send). If the account has no sandbox domain, UniOne creates one and returns it. Repeated calls return the same domain.

The sandbox domain is removed 31 days after it was created; the next call creates a new one. Up to 100 emails a day can be sent from it (the default limit of the account).

The method is available only with an account API key. Project API keys cannot create sandbox domains.

Request body (application/json):


Response 200: Sandbox domain has been returned.

- `status` (string, required; enum: success) — "success" string
- `domain` (string, required) — Sandbox domain name.

Response default: Error occurred.

## POST /domain/delete.json

Deletes a domain. Attention: you should use project's API key to delete a project's domain.

Deletes a domain.

Request body (application/json):

- `domain` (string, required) — Domain name to delete.

Response 200: Domain has been successfully deleted.

- `status` (string, required; enum: success) — "success" string
- `message` (string, required) — Domain deleted

Response default: Error occured.
