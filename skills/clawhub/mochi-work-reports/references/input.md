# Work ledger input and output

## Add a dated item

Required: `action: "add"`, unique `requestId` (up to 200 characters), `date` (valid YYYY-MM-DD), non-empty `title` (up to 500 characters), non-empty `detail` (up to 12000 characters), `status` (`done`, `in-progress` or `blocked`), and non-empty `evidence` array of source-reference strings (up to 1000 characters each).

Optional `minutes`: integer 0..1440. Omit unknown duration; zero means a recorded zero. Evidence labels retain the source supplied by the user and do not independently verify it. The successful result is `ok: true` and `record` with generated id and createdAt. Identical input and requestId replays the prior result with `replayed: true`; changed input under that ID returns an error. Records are appended; no update or delete action is implemented.

## Retrieve a period

`action: "report"`, `from` and `to` as valid YYYY-MM-DD dates, with from <= to. Both endpoints are included. Output: `ok: true`, `from`, `to`, selected `records`, `sections` grouped into the three states, `recordedMinutes`, and `recordsWithoutDuration`. An empty period has empty records/sections, zero recorded minutes and zero missing-duration records. Retrieval does not need requestId.

## Persistence and errors

Use an existing active workspace and put the request JSON inside it. The ledger file is `.mochilab/mochi-work-reports/state.json`; JSON CLI output is not a saved report document. The common store validates workspace paths, uses a write lock and atomic replacement, and enforces an 8 MiB state limit. Leave another operation's busy lock in place. CLI failures return `ok: false` with an error on stderr and exit code 1. The bundled add sample is fictional; replace its dates and evidence for real work.
