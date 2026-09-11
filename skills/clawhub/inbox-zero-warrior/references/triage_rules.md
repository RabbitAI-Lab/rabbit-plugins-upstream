# Email Triage Classification Reference

## Urgency Levels

| Level | Color | Definition | Response Time |
|-------|-------|-----------|---------------|
| Critical | 🔴 | Deadline today, urgent request, escalation | Immediately |
| High | 🟠 | Requires response, time-sensitive | Within 24 hours |
| Medium | 🟡 | FYI, non-urgent request, routine | Within 1 week |
| Low | 🔵 | No response needed | File/Archive |

## Category System

### Work/Project
- Emails from colleagues, managers, clients about work tasks
- Contains project names, deadlines, action items
- Meeting requests and follow-ups

### Personal
- Friends, family, personal contacts
- Non-work commitments, social plans

### Newsletter/Promo
- Marketing emails, newsletters, promotional offers
- Subscription digests, blog notifications
- Identified by: List-Unsubscribe header, sender domain patterns, content keywords

### Notification
- System alerts (build failures, security warnings)
- Social media notifications (mentions, friend requests)
- Service status updates

### Receipt/Finance
- Purchase confirmations, invoices
- Bank/credit card statements
- Subscription billing notices

### Social
- Event invitations, party planning
- Social media DMs routed through email

## Classification Heuristics

### Critical Detection
- Subject contains: URGENT, ASAP, CRITICAL, EMERGENCY (case-insensitive)
- Time-sensitive: "deadline today", "by EOD", "within the hour"
- From boss/exec/important client with a question
- Server/system failure notifications

### Newsletter Detection
- Has `List-Unsubscribe` header
- Sender domain matches known ESPs: mailchimp.com, sendgrid.net, hubspot.com
- Contains "unsubscribe", "manage preferences", "view in browser"
- Sender has sent 3+ emails in past 7 days with no replies

### No-Response-Needed Detection
- Receipt/confirmation emails
- "No-reply" sender addresses
- FYI/notification emails without a question
- Auto-generated status updates

## Email Export Formats

### JSON Format (recommended)
```json
[
  {
    "from": "sender@example.com",
    "to": "user@example.com",
    "subject": "Subject line",
    "date": "2026-08-13T10:30:00Z",
    "body": "Email body text...",
    "headers": {
      "List-Unsubscribe": "<mailto:unsub@example.com>",
      "X-Mailer": "Mailchimp"
    }
  }
]
```

### CSV Format
Columns: from, to, subject, date, body, has_unsubscribe

### MBOX Format
Standard mbox format exportable from Gmail, Thunderbird, Apple Mail.
