# Suppressions and unsubscribes

UniOne does not send to suppressed addresses: they come back in `failed_emails` of `email/send`.

| Cause | Meaning |
|---|---|
| `unsubscribed` | The recipient unsubscribed (unsubscribe link, List-Unsubscribe or your import). |
| `temporary_unavailable` | Recent rejection (spam block, full mailbox, domain not accepting mail); sending fails for the next three days. |
| `permanent_unavailable` | Repeated hard bounces. |
| `complained` | The recipient reported spam. |

- `suppression/get` (one address, with causes and dates), `suppression/list` (by cause / date, cursor paging),
  `suppression/set` (add, e.g. import the unsubscribes of your previous provider), `suppression/delete` (only when
  the recipient asks to receive mail again; complaints and permanent bounces should stay).
- The `bypass_*` flags of `email/send` ignore suppressions; they need support approval and are for critical
  messages to addresses that asked for them (e.g. a password reset), never for marketing.
- Every message gets an unsubscribe link by default; transactional messages can use their own
  `options.unsubscribe_url`. Marketing email must always offer a working unsubscribe.
