# Gmail access policy

An access policy limits which endpoints Gmail connections may call through Maton. Change it only when the user asks; see the Connections section of SKILL.md. Also at https://docs.maton.ai/google-mail#permissions.

## Read-only access policy

The rules the Maton console saves when the user picks **Read** for Gmail: its 30 read-only endpoints. Endpoints that return credentials, start jobs, or spend credits are left out. Save them as `policy.json` and pass `--access-policy-file policy.json` to `maton connection create` or `maton connection update`; trim or extend them when the user wants narrower or wider access.

```bash
maton connection create google-mail --access-policy-file policy.json
maton connection update {connection_id} --access-policy-file policy.json
```

```json
{
  "allow": [
    {"method": "GET", "path": "gmail/v1/users/{id}/drafts"},
    {"method": "GET", "path": "gmail/v1/users/{id}/drafts/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/history"},
    {"method": "GET", "path": "gmail/v1/users/{id}/labels"},
    {"method": "GET", "path": "gmail/v1/users/{id}/labels/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/messages"},
    {"method": "GET", "path": "gmail/v1/users/{id}/messages/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/messages/{id}/attachments/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/autoForwarding"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/cse/identities"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/cse/identities/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/cse/keypairs"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/cse/keypairs/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/delegates"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/delegates/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/filters"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/filters/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/forwardingAddresses"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/forwardingAddresses/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/imap"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/language"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/pop"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/sendAs"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/sendAs/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/settings/vacation"},
    {"method": "GET", "path": "gmail/v1/users/{id}/threads"},
    {"method": "GET", "path": "gmail/v1/users/{id}/threads/{id}"},
    {"method": "GET", "path": "gmail/v1/users/{id}/profile"}
  ],
  "deny": []
}
```

## Endpoints

The Gmail endpoints Maton has reviewed, each marked read or write, for building custom rules. Paths are relative to the app, as in an access policy; `{id}` matches one path segment.

| Method | Path | Access | Resource | Description |
| --- | --- | --- | --- | --- |
| GET | gmail/v1/users/{id}/drafts | read | drafts | Lists the drafts in the user's mailbox. |
| POST | gmail/v1/users/{id}/drafts | write | drafts | Creates a draft with the `DRAFT` label. |
| POST | gmail/v1/users/{id}/drafts/send | write | drafts | Sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers. |
| GET | gmail/v1/users/{id}/drafts/{id} | read | drafts | Gets the specified draft. |
| PUT | gmail/v1/users/{id}/drafts/{id} | write | drafts | Replaces a draft's content. |
| DELETE | gmail/v1/users/{id}/drafts/{id} | write | drafts | Immediately and permanently deletes the specified draft. |
| POST | upload/gmail/v1/users/{id}/drafts | write | drafts | Creates a draft with the `DRAFT` label. (media upload) |
| POST | upload/gmail/v1/users/{id}/drafts/send | write | drafts | Sends the specified, existing draft to the recipients in the `To`, `Cc`, and `Bcc` headers. (media upload) |
| PUT | upload/gmail/v1/users/{id}/drafts/{id} | write | drafts | Replaces a draft's content. (media upload) |
| GET | gmail/v1/users/{id}/history | read | history | Lists the history of all changes to the given mailbox. |
| GET | gmail/v1/users/{id}/labels | read | labels | Lists all labels in the user's mailbox. |
| POST | gmail/v1/users/{id}/labels | write | labels | Creates a label. |
| GET | gmail/v1/users/{id}/labels/{id} | read | labels | Gets the specified label. |
| PUT | gmail/v1/users/{id}/labels/{id} | write | labels | Updates the specified label. |
| PATCH | gmail/v1/users/{id}/labels/{id} | write | labels | Patch the specified label. |
| DELETE | gmail/v1/users/{id}/labels/{id} | write | labels | Immediately and permanently deletes the specified label and removes it from any messages and threads that it's applied to. |
| GET | gmail/v1/users/{id}/messages | read | messages | Lists the messages in the user's mailbox. |
| POST | gmail/v1/users/{id}/messages | write | messages | Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. |
| POST | gmail/v1/users/{id}/messages/batchDelete | write | messages | Deletes many messages by message ID. |
| POST | gmail/v1/users/{id}/messages/batchModify | write | messages | Modifies the labels and the Classification Label values on the specified messages. |
| POST | gmail/v1/users/{id}/messages/import | write | messages | Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. |
| POST | gmail/v1/users/{id}/messages/send | write | messages | Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. |
| GET | gmail/v1/users/{id}/messages/{id} | read | messages | Gets the specified message. |
| DELETE | gmail/v1/users/{id}/messages/{id} | write | messages | Immediately and permanently deletes the specified message. |
| GET | gmail/v1/users/{id}/messages/{id}/attachments/{id} | read | messages | Gets the specified message attachment. |
| POST | gmail/v1/users/{id}/messages/{id}/modify | write | messages | Modifies the labels and the Classification Label values on the specified message. |
| POST | gmail/v1/users/{id}/messages/{id}/trash | write | messages | Moves the specified message to the trash. |
| POST | gmail/v1/users/{id}/messages/{id}/untrash | write | messages | Removes the specified message from the trash. |
| POST | upload/gmail/v1/users/{id}/messages | write | messages | Directly inserts a message into only this user's mailbox similar to `IMAP APPEND`, bypassing most scanning and classification. (media upload) |
| POST | upload/gmail/v1/users/{id}/messages/import | write | messages | Imports a message into only this user's mailbox, with standard email delivery scanning and classification similar to receiving via SMTP. (media upload) |
| POST | upload/gmail/v1/users/{id}/messages/send | write | messages | Sends the specified message to the recipients in the `To`, `Cc`, and `Bcc` headers. (media upload) |
| GET | gmail/v1/users/{id}/settings/autoForwarding | read | settings | Gets the auto-forwarding setting for the specified account. |
| PUT | gmail/v1/users/{id}/settings/autoForwarding | write | settings | Updates the auto-forwarding setting for the specified account. |
| GET | gmail/v1/users/{id}/settings/cse/identities | read | settings | Lists the client-side encrypted identities for an authenticated user. |
| POST | gmail/v1/users/{id}/settings/cse/identities | write | settings | Creates and configures a client-side encryption identity that's authorized to send mail from the user account. |
| GET | gmail/v1/users/{id}/settings/cse/identities/{id} | read | settings | Retrieves a client-side encryption identity configuration. |
| PATCH | gmail/v1/users/{id}/settings/cse/identities/{id} | write | settings | Associates a different key pair with an existing client-side encryption identity. |
| DELETE | gmail/v1/users/{id}/settings/cse/identities/{id} | write | settings | Deletes a client-side encryption identity. |
| GET | gmail/v1/users/{id}/settings/cse/keypairs | read | settings | Lists client-side encryption key pairs for an authenticated user. |
| POST | gmail/v1/users/{id}/settings/cse/keypairs | write | settings | Creates and uploads a client-side encryption S/MIME public key certificate chain and private key metadata for the authenticated user. |
| GET | gmail/v1/users/{id}/settings/cse/keypairs/{id} | read | settings | Retrieves an existing client-side encryption key pair. |
| POST | gmail/v1/users/{id}/settings/cse/keypairs/{id}:disable | write | settings | Turns off a client-side encryption key pair. |
| POST | gmail/v1/users/{id}/settings/cse/keypairs/{id}:enable | write | settings | Turns on a client-side encryption key pair that was turned off. |
| POST | gmail/v1/users/{id}/settings/cse/keypairs/{id}:obliterate | write | settings | Deletes a client-side encryption key pair permanently and immediately. |
| GET | gmail/v1/users/{id}/settings/delegates | read | settings | Lists the delegates for the specified account. |
| POST | gmail/v1/users/{id}/settings/delegates | write | settings | Adds a delegate with its verification status set directly to `accepted`, without sending any verification email. |
| GET | gmail/v1/users/{id}/settings/delegates/{id} | read | settings | Gets the specified delegate. |
| DELETE | gmail/v1/users/{id}/settings/delegates/{id} | write | settings | Removes the specified delegate (which can be of any verification status), and revokes any verification that may have been required for using it. |
| GET | gmail/v1/users/{id}/settings/filters | read | settings | Lists the message filters of a Gmail user. |
| POST | gmail/v1/users/{id}/settings/filters | write | settings | Creates a filter. |
| GET | gmail/v1/users/{id}/settings/filters/{id} | read | settings | Gets a filter. |
| DELETE | gmail/v1/users/{id}/settings/filters/{id} | write | settings | Immediately and permanently deletes the specified filter. |
| GET | gmail/v1/users/{id}/settings/forwardingAddresses | read | settings | Lists the forwarding addresses for the specified account. |
| POST | gmail/v1/users/{id}/settings/forwardingAddresses | write | settings | Creates a forwarding address. |
| GET | gmail/v1/users/{id}/settings/forwardingAddresses/{id} | read | settings | Gets the specified forwarding address. |
| DELETE | gmail/v1/users/{id}/settings/forwardingAddresses/{id} | write | settings | Deletes the specified forwarding address and revokes any verification that may have been required. |
| GET | gmail/v1/users/{id}/settings/imap | read | settings | Gets IMAP settings. |
| PUT | gmail/v1/users/{id}/settings/imap | write | settings | Updates IMAP settings. |
| GET | gmail/v1/users/{id}/settings/language | read | settings | Gets language settings. |
| PUT | gmail/v1/users/{id}/settings/language | write | settings | Updates language settings. |
| GET | gmail/v1/users/{id}/settings/pop | read | settings | Gets POP settings. |
| PUT | gmail/v1/users/{id}/settings/pop | write | settings | Updates POP settings. |
| GET | gmail/v1/users/{id}/settings/sendAs | read | settings | Lists the send-as aliases for the specified account. |
| POST | gmail/v1/users/{id}/settings/sendAs | write | settings | Creates a custom "from" send-as alias. |
| GET | gmail/v1/users/{id}/settings/sendAs/{id} | read | settings | Gets the specified send-as alias. |
| PUT | gmail/v1/users/{id}/settings/sendAs/{id} | write | settings | Updates a send-as alias. |
| PATCH | gmail/v1/users/{id}/settings/sendAs/{id} | write | settings | Patch the specified send-as alias. |
| DELETE | gmail/v1/users/{id}/settings/sendAs/{id} | write | settings | Deletes the specified send-as alias. |
| GET | gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo | read | settings | Lists S/MIME configs for the specified send-as alias. |
| POST | gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo | write | settings | Insert (upload) the given S/MIME config for the specified send-as alias. |
| GET | gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo/{id} | read | settings | Gets the specified S/MIME config for the specified send-as alias. |
| DELETE | gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo/{id} | write | settings | Deletes the specified S/MIME config for the specified send-as alias. |
| POST | gmail/v1/users/{id}/settings/sendAs/{id}/smimeInfo/{id}/setDefault | write | settings | Sets the default S/MIME config for the specified send-as alias. |
| POST | gmail/v1/users/{id}/settings/sendAs/{id}/verify | write | settings | Sends a verification email to the specified send-as alias address. |
| GET | gmail/v1/users/{id}/settings/vacation | read | settings | Gets vacation responder settings. |
| PUT | gmail/v1/users/{id}/settings/vacation | write | settings | Updates vacation responder settings. |
| GET | gmail/v1/users/{id}/threads | read | threads | Lists the threads in the user's mailbox. |
| GET | gmail/v1/users/{id}/threads/{id} | read | threads | Gets the specified thread. |
| DELETE | gmail/v1/users/{id}/threads/{id} | write | threads | Immediately and permanently deletes the specified thread. |
| POST | gmail/v1/users/{id}/threads/{id}/modify | write | threads | Modifies the labels applied to the thread. |
| POST | gmail/v1/users/{id}/threads/{id}/trash | write | threads | Moves the specified thread to the trash. |
| POST | gmail/v1/users/{id}/threads/{id}/untrash | write | threads | Removes the specified thread from the trash. |
| GET | gmail/v1/users/{id}/profile | read | users | Gets the current user's Gmail profile. |
| POST | gmail/v1/users/{id}/stop | write | users | Turn off push notification delivery for the given user mailbox. |
| POST | gmail/v1/users/{id}/watch | write | users | Set up or update a push notification watch on the given user mailbox. |
| POST | batch/gmail/v1 | write | batch | Send several Gmail API calls in one request. |
