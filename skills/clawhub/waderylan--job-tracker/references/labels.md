# Labels and stages

Choose exactly one label per email.

| Label | Use when | Not when |
| --- | --- | --- |
| `application_received` | Explicit confirmation that the application itself was received, including automated and duplicate confirmations | Acknowledging extra documents; out-of-office replies |
| `outreach` | An individual recruiter introduces a new opportunity | Administration of an existing candidacy; other advertised roles mentioned in a status update |
| `invite` | A new interview, assessment, booking or explicit advancement to a next hiring step | A promise of feedback alone |
| `scheduling_update` | An explicit reschedule, change or cancellation of an already scheduled meeting | A newly booked interview, even in a reply thread (that is `invite`) |
| `deadline_reminder` | A reminder of an existing assessment, assignment or offer-response deadline | A first offer or new assessment (`offer` or `invite`) |
| `offer` | An actual employment offer to this candidate | Hypothetical offers, positive feedback, undecided outcomes |
| `rejection` | The candidacy ends, including the role being filled or closed to this candidate | Delays or pauses |
| `recruiting_event` | An announced recruiting gathering such as a career fair or information session | Interviews, panel feedback, mentions of other vacancies |
| `info_request` | A request to supply or confirm information such as availability, graduation or start date | An acknowledgement saying no action is needed |
| `other_job` | Other hiring correspondence: document receipts, absence replies, waiting for panel feedback, thanks or positive feedback without a next step | A genuine application receipt (`application_received`) |

## Stages (only with `invite`)

| Stage | Meaning |
| --- | --- |
| `oa` | Online or timed coding assessment |
| `recruiter_screen` | Recruiter call or screen, including for technical roles |
| `technical` | Technical, coding or system-design interview |
| `take_home` | Take-home assignment |
| `onsite` | Explicitly onsite interview or loop |
| `work_trial` | Explicitly named work trial |
| `unknown` | An invite with no supported named stage. "Behavioral" or "final" alone do not name a stage. |

For every label other than `invite`, the stage is null.

## Examples (synthetic)

| Email excerpt | Label | Stage |
| --- | --- | --- |
| "Thanks for applying to the Backend Engineer role at Northwind. We have received your application." | `application_received` | null |
| "Please complete the HackerRank assessment within 5 days." | `invite` | `oa` |
| "Can we move Thursday's technical interview to Friday at 2 PM PT?" | `scheduling_update` | null |
| "We are pleased to offer you the position of Software Engineer. Please respond by June 3." | `offer` | null |
| "The position has been filled. We wish you the best." | `rejection` | null |
| "Could you share your availability next week and your expected graduation date?" | `info_request` | null |
| "We received your transcript. The panel will share feedback soon." | `other_job` | null |
