---
name: inbox-zero-warrior
description: "Triage, categorize, and conquer email overload. Classifies emails by urgency, generates quick replies, detects newsletters for bulk unsubscribe, and produces daily digests. Use when facing an overflowing inbox or wanting to maintain inbox zero."
version: 1.0.0
author: Denis Voronin
license: MIT
tags: [email, productivity, inbox-zero, triage, automation]
---

# Inbox Zero Warrior

## Overview

Email overload is the #1 productivity drain for knowledge workers. The average professional receives 120+ emails per day and spends 28% of their workday managing email. This skill analyzes an email export, classifies every message by urgency and category, identifies newsletters and promotional emails for batch unsubscribe, generates suggested quick replies for common patterns, and produces a prioritized action list and daily digest.

## When to Use

- A user has an **overflowing inbox** (50+ unread) and needs to triage
- A user wants to **reach inbox zero** and maintain it
- A user wants to **unsubscribe from newsletters** in bulk
- A user needs **quick replies** generated for routine emails
- A user wants a **daily email digest** instead of checking constantly
- **Don't use for:** actual email sending/receiving (this analyzes exports), or enterprise email archiving

## Core Features

### 1. Email Triage (`scripts/email_triage.py`)
Classifies emails by urgency, category, and action needed:
- **Urgency:** Critical (deadline today), High (respond within 24h), Medium (respond within a week), Low (no response needed)
- **Category:** Work/Project, Personal, Newsletter/Promo, Social, Receipt/Finance, Notification
- **Action:** Reply Now, Reply Later, File, Unsubscribe, Delete

### 2. Newsletter Detector (`scripts/newsletter_detector.py`)
Identifies newsletters and promotional emails from patterns:
- List-Unsubscribe headers
- Sender domain patterns (mailchimp, sendgrid, etc.)
- Content patterns ("unsubscribe", "view in browser", frequency)
- Generates a prioritized unsubscribe list

### 3. Quick Reply Generator (`scripts/quick_reply.py`)
Generates suggested replies for common email patterns:
- Meeting confirmations, rejections, reschedules
- "Got it, will follow up" responses
- Out-of-office auto-replies
- Document/file acknowledgment

## Numbered Workflow

1. **Export emails** — Export inbox as JSON, CSV, or MBOX
2. **Triage** — Run classification to categorize all emails
3. **Newsletter purge** — Identify and batch-unsubscribe from newsletters
4. **Quick replies** — Generate suggested responses for actionable emails
5. **Action list** — Get a prioritized task list for the day
6. **Digest** — Set up a daily summary instead of constant checking

## Common Pitfalls

1. **Not setting up filters after unsubscribing.** After unsubscribing, set up rules to auto-file or delete future emails from that sender. Otherwise you'll just resubscribe.

2. **Over-responding to Low priority emails.** Most emails don't need a response. If the triage says "No response needed," trust it — responding just creates more email.

3. **Checking email too frequently.** The goal of a daily digest is to check 2-3 times per day, not constantly. Turn off notifications and batch-process.

4. **Ignoring the 2-minute rule.** If a reply takes less than 2 minutes, do it immediately instead of filing it for later.

5. **Unsubscribing from everything at once.** Some newsletters are valuable. Review the unsubscribe list before nuking everything.

## Verification Checklist

- [ ] All emails classified with urgency and category
- [ ] Newsletter list generated and reviewed
- [ ] Quick replies generated for all "Reply Now" items
- [ ] Daily action list prioritized by urgency
- [ ] Filters/rules set up for recurring non-actionable emails

## Example Session

**User:** "I have 200 unread emails and I'm overwhelmed. Help me get to inbox zero."

**Agent:** Let me triage your inbox. After analyzing your export:

```
📊 INBOX TRIAGE REPORT
═══════════════════════════════════════
Total emails: 200

🔴 CRITICAL (3): Require response today
  • "Q3 Budget Approval Needed" - from CFO
  • "Client demo in 2 hours - slides?" - from Sales
  • "Server down - URGENT" - from DevOps

🟠 HIGH (12): Respond within 24h
  • Project updates, meeting requests, client questions...

🟡 MEDIUM (45): Respond within a week
  • FYIs, routine updates, non-urgent requests...

🔵 LOW (140): No response needed
  • Receipts (23), newsletters (89), notifications (28)

💡 RECOMMENDED ACTIONS:
  1. Respond to 3 CRITICAL emails NOW
  2. Generate quick replies for 12 HIGH emails
  3. Unsubscribe from 34 newsletters (unsubscribe list ready)
  4. Auto-file 140 LOW emails to "Archive"
  5. Set up 8 rules for recurring senders

⏱️ Estimated time to inbox zero: 45 minutes
```
