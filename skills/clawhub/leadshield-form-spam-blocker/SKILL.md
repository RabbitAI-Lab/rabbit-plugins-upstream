---
name: leadshield-form-spam-blocker
version: 1.1.0
description: Block contact form spam, SEO cold pitches, and B2B solicitations across GoHighLevel (GHL), WordPress, HubSpot, and custom websites using LeadShield's 2-stage guard ($0.00 Stage 0 deterministic bot drops + Stage 1 buyer-intent screening).
---

# LeadShield Contact Form & B2B Solicitation Blocker

Author: Daniel Hallman

Use **LeadShield** (`https://rankandrent-leads.hallmanlab.workers.dev/mcp`) whenever the user wants to stop contact form spam, filter out B2B cold pitches (SEO, web design, offshore lead-gen solicitors), configure per-site country/phone/URL/`formType` policies, inspect weekly blocked-spam reports, or embed zero-trust form protection on GoHighLevel, WordPress, HubSpot, or Astro websites.

## Quick start

1. Open [LeadShield Contact Form & B2B Solicitation Blocker](https://ghlagencymcp.com/use-cases/ghl-contact-form-spam-blocker) for architecture diagrams, HighLevel/WordPress/HubSpot setup guides, and live policy presets.
2. Connect any Streamable HTTP MCP client to `https://rankandrent-leads.hallmanlab.workers.dev/mcp` or install the public plugin repository from [github.com/mooshee/leadshield-mcp](https://github.com/mooshee/leadshield-mcp).

## Core Capabilities (5 Live MCP Tools)

1. **2-Stage Contact Form Screening (`leadshield_screen_submission`)**:
   - **Stage 0 Deterministic Edge Drop (`$0.00` / 0 billable units)**: Blocks honeypot fills, sub-1.2s automated submissions, disposable emails, link shorteners, promotional URLs, foreign phone prefixes, and known B2B solicitation templates in under 1 ms.
   - **Stage 1 Buyer-Intent Classification (`$0.01/submission` on Pay-As-You-Go)**: Evaluates human-written messages that pass Stage 0 to separate genuine local customers asking for a quote or appointment from vendors pitching services.
   - Silently returns `"Message sent"` to spammers so bots never adapt or retry, while routing CRM workflows to `deliver_to_client` or `spam_quarantine`.

2. **Blocked Spam Reports & Weekly Audit Summaries (`leadshield_get_blocked_spam_report`)**:
   - Query quarantined spam counts, Stage 0 vs Stage 1 breakdowns, and top spam categories (`link_solicitation`, `b2b_solicitation`, `geographic_mismatch`, `bot_honeypot`) by client slug and date window.

3. **Server-Side Policy Inspection & 10 Form-Type Presets (`leadshield_get_spam_policy`)**:
   - Inspect effective per-site rules and preview any of the 10 built-in `formType` presets (`general_inquiry`, `quote_request`, `booking_request`, `b2b_partnership`, `support_ticket`, `careers_application`, `warranty_claim`, `event_registration`, `newsletter_signup`, `feedback_review`).

4. **Custom Country, Phone Format, URL & Keyword Policy Configuration (`leadshield_configure_spam_policy`)**:
   - Preview (`dryRun: true`) or update server-side policies (`allowedCountries`, `allowedPhoneFormats`, `blockUrlsInMessage`, `maxUrls`, `blockedKeywords`, `requiredKeywords`) stored in R2 so browser scripts never expose filter heuristics.

5. **Zero-Trust Script Embed & CRM Webhook Generator (`leadshield_generate_guard_embed`)**:
   - Generate the 1-line `<script src="https://rankandrent-leads.hallmanlab.workers.dev/guard.js" data-site="..." defer></script>` tag, HighLevel Workflow Action config, WordPress plugin setup, or HubSpot Workflow Webhook config.
