# Sending domains and the sandbox

## Production domain

1. `domain/get-dns-records` with `domain` → `verification-record`, `dkim` (the key only) and `dmarc` (a CNAME target).
2. The user adds the records at their DNS provider:

   | Type | Host | Value |
   |---|---|---|
   | TXT | `@` | `verification-record` as is |
   | TXT | `<selector>._domainkey` (the selector is on the domain page of the control panel, e.g. `us`) | `v=DKIM1; k=rsa; p=` + `dkim` |
   | TXT | `@` | the SPF record with `include:spf.unione.io` (not in the response; merge into the existing SPF record) |
   | CNAME | `_dmarc` | `dmarc` (e.g. `example.com.dmarc.…`): UniOne then publishes the DMARC policy; skip it if the domain already has its own DMARC TXT record |

3. `domain/validate-verification-record` and `domain/validate-dkim` until both pass (DNS may take hours).
4. `domain/list` shows the statuses; send from any address of a domain whose verification record is confirmed and
   whose DKIM is active.

`from_email` must be on such a domain: a subdomain is a separate domain (verified `mail.example.com` does not
cover `example.com`). DMARC: the `_dmarc` CNAME above, or your own DMARC TXT record (see the email-best-practices
skill).

## Sandbox: the first email without DNS

1. `domain/get-sandbox-domain` → a sandbox domain of the account.
2. `confirmed-email/create` with the user's own address: a confirmation email goes to it; the link lives
   **48 hours** and works once (no resend: `confirmed-email/delete`, then create again).
   `confirmed-email/list` shows `confirmed` / `unconfirmed`.
3. `email/send` from any address on the sandbox domain (e.g. `noreply@<sandbox-domain>`) to a confirmed address.

Limits: up to **10 confirmed addresses**, **100 emails a day**, the domain lives 31 days; sending to an unconfirmed
address fails with API code 1598, over the daily limit with 1599. Account API key only (not a project key).

Never use the sandbox domain as the production sender (it is not in `domain/list`); read `from_email` from config.
Never test with made-up addresses at real mailbox providers (`test@gmail.com`): they bounce and hurt the reputation.
