## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, recurring tasks, and scheduled work through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to connect a Motion account through Maton, query Motion work data, and perform approved updates or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify data in the connected Motion account.

Mitigation: Use OAuth where possible, select the narrowest available Motion scopes, default to read/list calls, and confirm every write, deletion, or new connection with the user before execution.

Risk: Raw HTTP or environment-based API key use can expose a long-lived credential.

Mitigation: Prefer the Maton CLI OAuth flow and credential store; use raw HTTP only when the CLI cannot be installed, avoid printing or logging keys, and rotate any key that was exposed.

Risk: Functions, triggers, and destinations can create persistent automation or ongoing data forwarding.

Mitigation: Require explicit approval for each hosted function, trigger, destination, deploy, update, and invocation; keep destinations on Maton-controlled hosts unless the user approves a named third-party host and understands what data will flow.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/motion)
- [Maton Homepage](https://maton.ai)
- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Calendly Trigger Reference](references/calendly/triggers.md)
- [GitHub Trigger Reference](references/github/triggers.md)
- [Gmail Trigger Reference](references/google-mail/triggers.md)
- [HubSpot Trigger Reference](references/hubspot/triggers.md)
- [Linear Trigger Reference](references/linear/triggers.md)
- [Notion Trigger Reference](references/notion/triggers.md)
- [Slack Trigger Reference](references/slack/triggers.md)
- [Stripe Trigger Reference](references/stripe/triggers.md)
- [Time Trigger Reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and API request snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OAuth setup, Motion API calls, hosted automation guidance, and approval checks; no binary outputs.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
