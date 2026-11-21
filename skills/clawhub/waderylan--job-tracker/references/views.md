# Computed views

All views are read-only: they use the file contents and today's date and never write the file. State the date used.

| View | Definition |
| --- | --- |
| Status list | Records not `Rejected` or `Withdrawn`, sorted by `last_inbound_at` descending: company, role, status, stage, next deadline or interview |
| Funnel | For each stage, the number of records whose `stage_history` contains it. Stages overlap. |
| Response rate | Records with any inbound email after `application_received` (any later `message_log` entry) divided by records with origin `applied` |
| Time in stage | For each consecutive pair in `stage_history`, days between entries; report the median per stage and the count of visits |
| Follow-up due | `Applied` records with origin `applied` and 7 or more days since `last_inbound_at` |
| Ghosted | `Applied` or `Interviewing` with 21 or more days since `last_inbound_at`. List only. After the user confirms, set `status_before_ghosted`, change status to `Ghosted` and append history. |
| Deadlines | Open deadlines sorted by `due`, with days remaining; past-due items marked overdue |
| Outcomes | Counts of `Offer`, `Rejected`, `Ghosted`, `Withdrawn` |

Show counts as integers and rates as a percentage with the numerator and denominator, for example `4/10 (40%)`.
