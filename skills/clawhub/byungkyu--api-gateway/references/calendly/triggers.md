# Calendly Trigger Reference

> **Invitee payloads contain third-party personal data.** These events carry the invitee's full name, email address, timezone, free-text question responses, cancellation reasons, and meeting join URLs. The invitee is a *third party* — they booked a meeting, they did not consent to their details being relayed to an arbitrary downstream system.
>
> Before attaching a destination:
> - Recognize that every matching booking will be forwarded automatically and continuously, PII included.
> - Forward only the fields the downstream workflow needs via `body_template` (e.g. name and start time) rather than the whole payload. Cancellation reasons and question responses are often personal — omit them unless required.
> - Treat join URLs as secrets: anyone holding one may be able to enter the meeting. Do not relay them to public channels or third-party hosts.
> - Prefer destinations on the `api.maton.ai` host; get explicit user approval before sending invitee data to any external host.

## Event Types

- [`invitee.created`](#inviteecreated)
- [`invitee.canceled`](#inviteecanceled)
- [`invitee_no_show.created`](#invitee_no_showcreated)

---

## `invitee.created`

### Sample Payload

```json
{
  "event": "invitee.created",
  "created_at": "2026-06-24T22:30:45.105381Z",
  "created_by": ".../users/00000000-0000-0000-0000-0000000000a1",
  "payload": {
    "uri": ".../scheduled_events/00000000-0000-0000-0000-000000000002/invitees/00000000-0000-0000-0000-000000000001",
    "name": "John Doe",
    "status": "active",
    "cancel_url": "https://calendly.com/cancellations/00000000-0000-0000-0000-000000000001",
    "reschedule_url": "https://calendly.com/reschedulings/00000000-0000-0000-0000-000000000001",
    "email": "john.doe@example.com",
    "timezone": "America/Los_Angeles",
    "scheduled_event": {
      "uri": ".../scheduled_events/00000000-0000-0000-0000-000000000002",
      "name": "Acme - Intro",
      "start_time": "2026-06-10T06:30:00.000000Z",
      "end_time": "2026-06-10T07:00:00.000000Z"
    }
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is Calendly's full object, including absolute `api.calendly.com` resource URIs, membership and location blocks, and `questions_and_answers`. See [Calendly webhook payloads](https://developer.calendly.com/api-docs) for the complete shape, and forward only what the workflow needs.

---

## `invitee.canceled`

### Sample Payload

```json
{
  "event": "invitee.canceled",
  "created_at": "2026-06-24T22:30:45.574849Z",
  "created_by": ".../users/00000000-0000-0000-0000-0000000000a1",
  "payload": {
    "uri": ".../scheduled_events/00000000-0000-0000-0000-000000000004/invitees/00000000-0000-0000-0000-000000000003",
    "name": "Jane Doe",
    "status": "canceled",
    "cancel_url": "https://calendly.com/cancellations/00000000-0000-0000-0000-000000000003",
    "reschedule_url": "https://calendly.com/reschedulings/00000000-0000-0000-0000-000000000003",
    "email": "jane.doe@example.com",
    "timezone": "America/Los_Angeles",
    "scheduled_event": {
      "uri": ".../scheduled_events/00000000-0000-0000-0000-000000000004",
      "name": "Acme - Intro",
      "start_time": "2026-07-01T06:30:00.000000Z",
      "end_time": "2026-07-01T07:00:00.000000Z"
    }
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is Calendly's full object, including absolute `api.calendly.com` resource URIs, membership and location blocks, and `questions_and_answers`. See [Calendly webhook payloads](https://developer.calendly.com/api-docs) for the complete shape, and forward only what the workflow needs.

---

## `invitee_no_show.created`

### Sample Payload

```json
{
  "event": "invitee_no_show.created",
  "created_at": "2026-06-24T22:34:33.909091Z",
  "created_by": ".../users/00000000-0000-0000-0000-0000000000a1",
  "payload": {
    "uri": ".../scheduled_events/00000000-0000-0000-0000-000000000002/invitees/00000000-0000-0000-0000-000000000001",
    "name": "John Doe",
    "status": "active",
    "cancel_url": "https://calendly.com/cancellations/00000000-0000-0000-0000-000000000001",
    "reschedule_url": "https://calendly.com/reschedulings/00000000-0000-0000-0000-000000000001",
    "email": "john.doe@example.com",
    "timezone": "America/Los_Angeles",
    "scheduled_event": {
      "uri": ".../scheduled_events/00000000-0000-0000-0000-000000000002",
      "name": "Acme - Intro",
      "start_time": "2026-06-10T06:30:00.000000Z",
      "end_time": "2026-06-10T07:00:00.000000Z"
    }
  }
}
```

> Trimmed to the fields a `body_template` normally reads. The real event is Calendly's full object, including absolute `api.calendly.com` resource URIs, membership and location blocks, and `questions_and_answers`. See [Calendly webhook payloads](https://developer.calendly.com/api-docs) for the complete shape, and forward only what the workflow needs.