## Description:

Kaggle API integration with managed authentication for accessing datasets, models, competitions, and notebooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search, download, and interact with Kaggle resources through a user's authenticated Maton connection. It also documents optional hosted functions and trigger-based automation for approved Kaggle workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Kaggle through the user's Maton connection and can optionally create hosted functions or triggers that continue running.

Mitigation: Use OAuth where possible, confirm every connection, write, delete, function, trigger, or destination action explicitly, and scope automation to approved accounts and connections.

Risk: Raw API-key mode exposes a long-lived Maton credential to the process environment.

Mitigation: Prefer the Maton CLI OAuth flow; when raw HTTP is unavoidable, never print, persist, or pass the key on a command line and send it only to api.maton.ai.

Risk: Trigger destinations and event watches can create ongoing data flows or unattended local automation.

Mitigation: Create them only after separate approval that names the destination or handler, transmitted fields, persistence, and cleanup plan; prefer api.maton.ai or *.maton.app destinations.

## Reference(s):

- [ClawHub Kaggle Skill](https://clawhub.ai/maton/skills/kaggle-api)
- [Maton](https://maton.ai)
- [Kaggle API Documentation](https://www.kaggle.com/docs/api)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Models](https://www.kaggle.com/models)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](references/time/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands, code blocks, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Maton CLI commands, raw HTTP examples, Kaggle API payloads, and approval guidance.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
