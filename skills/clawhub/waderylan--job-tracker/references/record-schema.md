# Record schema

`job-tracker/applications.json`:

```json
{
  "applications": [
    {
      "id": "a1",
      "origin": "applied",
      "company": "Northwind",
      "role": "Backend Engineer",
      "applied_date": "2026-05-04",
      "status": "Interviewing",
      "stage": "technical",
      "stage_history": [
        {"status": "Applied", "stage": "applied", "at": "2026-05-04", "source": "application_received"},
        {"status": "Interviewing", "stage": "technical", "at": "2026-05-12", "source": "invite"}
      ],
      "status_before_ghosted": null,
      "deadlines": [
        {"kind": "oa_expiry", "due": "2026-05-09", "note": "within 5 days", "open": false}
      ],
      "interviews": [
        {"stage": "technical", "start": "2026-05-15T14:00", "end": "2026-05-15T15:00", "time_zone": "America/Los_Angeles", "status": "scheduled"}
      ],
      "last_inbound_at": "2026-05-12",
      "message_log": [
        {"date": "2026-05-12", "label": "invite", "stage": "technical", "summary": "Technical interview booked for May 15."}
      ],
      "needs_review": false
    }
  ],
  "events": [
    {"name": "Spring career fair", "date": "2026-05-20", "source_date": "2026-05-01"}
  ]
}
```

- `id`: `a` plus a sequence number, unique within the file.
- `origin`: `applied` or `sourced`.
- `status`, `stage`: values from [transitions.md](transitions.md).
- `message_log.summary`: one line in your own words; never copy the email body, addresses or phone numbers.
- Dates are `YYYY-MM-DD`; times are local `YYYY-MM-DDTHH:MM` with `time_zone`.
