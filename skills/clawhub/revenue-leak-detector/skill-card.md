## Description:

Identifies high-value audience segments missing premium monetization opportunities by analyzing subscriber databases and engagement patterns to recommend upsell, churn-prevention, and revenue growth actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ncreighton](https://clawhub.ai/user/ncreighton)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, revenue operations, and growth teams use this skill to analyze customer and subscriber data for upsell, churn-prevention, and win-back opportunities, then draft alerts, dashboards, and campaign guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests payment and customer-data credentials, including Stripe, Mailchimp, and Google Sheets access.

Mitigation: Use read-only, least-privilege credentials where available, avoid live production keys until the requested scope is explicit, and rotate any keys used during evaluation.

Risk: Reports, Slack alerts, and Sheets exports may expose customer identifiers or sensitive business data.

Mitigation: Mask customer identifiers before sending information to Slack or Sheets, and review exports for unnecessary personal or confidential data.

Risk: Generated campaigns, webhooks, CRM tags, and revenue recommendations could affect customers or business operations if activated automatically.

Mitigation: Treat generated campaigns, exports, webhooks, and CRM tags as drafts until a human reviews and approves them.

Risk: The security summary notes inconsistent promises about PII handling and campaign activation.

Mitigation: Confirm consent, suppression-list, and compliance requirements before using outputs for customer communications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ncreighton/skills/revenue-leak-detector)
- [Publisher profile](https://clawhub.ai/user/ncreighton)
- [Project homepage](https://github.com/ncreighton/empire-skills)
- [Stripe account API endpoint](https://api.stripe.com/v1/account)
- [Mailchimp API endpoint pattern](https://{dc}.api.mailchimp.com/3.0)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, YAML configuration examples, reports, alert text, dashboard guidance, and campaign sequence drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include revenue opportunity reports, segment-specific campaign drafts, churn alerts, Slack notification text, and Google Sheets dashboard guidance.]

## Skill Version(s):

1.0.0 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
