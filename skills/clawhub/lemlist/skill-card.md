## Description:

Lemlist API integration with managed OAuth for managing campaigns, leads, activities, schedules, unsubscribes, and related sales outreach workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and sales teams use this skill to guide authenticated Lemlist API calls through Maton for account setup, reads, writes, and approved automation involving campaigns, leads, activities, schedules, and unsubscribes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide authenticated access to Lemlist outreach data through a Maton connection.

Mitigation: Verify trust in Maton as the package and OAuth provider, prefer OAuth over long-lived API keys, and confirm the exact Lemlist account and connection before use.

Risk: Writes and automation can modify outreach data or create persistent event forwarding.

Mitigation: Confirm every write with the user, review functions and triggers before enabling them, and avoid third-party trigger destinations unless the forwarded data and host are explicitly approved.

## Reference(s):

- [ClawHub lemlist skill page](https://clawhub.ai/byungkyu/skills/lemlist)
- [Maton homepage](https://maton.ai)
- [Lemlist API Documentation](https://developer.lemlist.com/)
- [Lemlist API Reference](https://developer.lemlist.com/api-reference)
- [Lemlist Help Center - API](https://help.lemlist.com/en/collections/17109856-api-webhooks)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](artifact/references/time/triggers.md)
- [Calendly Trigger Reference](artifact/references/calendly/triggers.md)
- [GitHub Trigger Reference](artifact/references/github/triggers.md)
- [Gmail Trigger Reference](artifact/references/google-mail/triggers.md)
- [HubSpot Trigger Reference](artifact/references/hubspot/triggers.md)
- [Linear Trigger Reference](artifact/references/linear/triggers.md)
- [Notion Trigger Reference](artifact/references/notion/triggers.md)
- [Slack Trigger Reference](artifact/references/slack/triggers.md)
- [Stripe Trigger Reference](artifact/references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, JSON, Python, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include API endpoint paths, request payload examples, authentication steps, connection selection guidance, and automation setup guidance.]

## Skill Version(s):

1.2.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
