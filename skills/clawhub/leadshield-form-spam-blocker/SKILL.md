---
name: leadshield-form-spam-blocker
version: 1.1.2
description: Filter contact form spam and unwanted sales pitches on HighLevel, WordPress, HubSpot, and custom websites. Set rules for each site and review blocked submissions. Built by Moosh Works (https://mooshworks.com).
---

# LeadShield Contact Form & B2B Solicitation Blocker

Author: Daniel Hallman ([Moosh Works](https://mooshworks.com))

Use **LeadShield** to check contact form submissions for spam or unwanted sales pitches, set screening rules for a site, review blocked submissions, or add form protection to a website.

## Quick start

1. Open the [LeadShield setup guide](https://ghlagencymcp.com/use-cases/ghl-contact-form-spam-blocker) from [Moosh Works](https://mooshworks.com) and choose your website or CRM.
2. Connect a client that supports Streamable HTTP MCP to `https://rankandrent-leads.hallmanlab.workers.dev/mcp`, or install the plugin from the [public repository](https://github.com/mooshee/leadshield-mcp).
3. Use `leadshield_get_spam_policy` to check that the intended site's rules are available before changing them.

## What you can do

1. **Screen a form submission** (`leadshield_screen_submission`). Rule-based checks block submissions that match configured bot, email, link, phone, or sales-pitch rules. These checks cost $0.00. Messages that pass these checks are screened for customer inquiries or unwanted sales pitches at $0.01 per submission on the pay-as-you-go plan. The result selects the `deliver_to_client` or `spam_quarantine` workflow branch. A spam verdict does not verify a person's identity or guarantee their intent.

2. **Review blocked submissions** (`leadshield_get_blocked_spam_report`). Choose a site and date range to see counts, screening stages, and reasons such as `link_solicitation`, `b2b_solicitation`, `geographic_mismatch`, or `bot_honeypot`.

3. **Check site rules** (`leadshield_get_spam_policy`). Inspect the site's active rules and `formType` preset. Use the values returned by the tool when choosing a preset.

4. **Change site rules** (`leadshield_configure_spam_policy`). Preview the change with `dryRun: true`. After an authorized update, read the policy again to confirm the saved country, phone, link, and keyword rules. Rules are stored on the server.

5. **Add LeadShield to a site or workflow** (`leadshield_generate_guard_embed`). Generate setup instructions for a website script, HighLevel workflow action, WordPress plugin, or HubSpot webhook. Replace the site placeholder with the intended site identifier, then test a form submission and check the result.
