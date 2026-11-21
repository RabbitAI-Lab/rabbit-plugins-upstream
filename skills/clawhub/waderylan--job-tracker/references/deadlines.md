# Deadlines and interview times

Capture a deadline only when the email states a date. Never estimate one.

| Label and stage | Deadline kind |
| --- | --- |
| `invite`, stage `oa` | `oa_expiry` |
| `invite`, stage `take_home` | `take_home_due` |
| `offer` | `offer_decision` |
| `deadline_reminder` | Updates the open deadline for the record's current stage |
| `info_request` | `respond_by` |

- Relative dates ("within 5 days", "by Friday") resolve against the email's date. Record the resolved date and keep the original wording in `note`.
- Keep the stated time zone. If none is given, record the date only.
- An `invite` that names a time records an interview in `interviews`: `{stage, start, end, time_zone, status: "scheduled"}`. A `scheduling_update` replaces the start and end or sets `status: "cancelled"`.
- Ignore times unrelated to the candidacy, such as event talk slots or office hours in a signature.
