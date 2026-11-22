# Transition table

Statuses: `Applied`, `Interviewing`, `Offer`, `Rejected`, `Ghosted`, `Withdrawn`.
Stages: `applied`, `sourced`, `oa`, `recruiter_screen`, `technical`, `take_home`, `onsite`, `work_trial`, `offer`, `unknown`.

Apply the first matching row. Anything not listed changes nothing.

| Label | Stage | From status | To | Also |
| --- | --- | --- | --- | --- |
| `application_received` | n/a | no record | `Applied`, stage `applied` | Create the record, origin `applied` |
| `application_received` | n/a | existing record | no change | Duplicate confirmation; log only |
| `outreach` | n/a | no record | `Applied`, stage `sourced` | Create the record, origin `sourced` |
| `invite` | `oa` | Applied, Interviewing, Ghosted | `Interviewing`, stage `oa` | Set deadline `oa_expiry` if stated |
| `invite` | any other stage | Applied, Interviewing, Ghosted, Rejected | `Interviewing`, stage as named | Record the interview time if stated |
| `scheduling_update` | n/a | Interviewing | no change | Update or cancel the interview time |
| `deadline_reminder` | n/a | any | no change | Update the open deadline |
| `offer` | n/a | Interviewing, Applied, Ghosted, Rejected | `Offer`, stage `offer` | Set deadline `offer_decision` if stated |
| `rejection` | n/a | Applied, Interviewing, Offer, Ghosted | `Rejected` | None |
| `info_request` | n/a | any | no change | Set deadline `respond_by` if stated; flag action needed |
| `recruiting_event` | n/a | n/a | no record change | Add to `events`, not `applications` |
| `other_job` | n/a | any | no change | None |

If an `invite`, `scheduling_update`, `deadline_reminder`, `offer`, `rejection` or `info_request` email matches no record, create one with the company from the email, status from the table, and `needs_review: true`, and tell the user.

## Time rules

- `Applied` or `Interviewing` with no inbound email for 21 days is a `Ghosted` candidate. List candidates in reports; write `Ghosted` (reason `ghost_timer`) only after the user confirms.
- A later email on a `Ghosted` record is processed from the status it had before `Ghosted`.
- `Withdrawn` is set only by the user. `Offer`, `Rejected` and `Withdrawn` change only through the table or the user.
- Every status or stage change appends `{status, stage, at, source}` to `stage_history`, where `source` is the email date and label or `user`.
