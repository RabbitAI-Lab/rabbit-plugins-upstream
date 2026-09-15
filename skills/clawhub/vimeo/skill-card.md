## Description:

Vimeo API integration with managed OAuth for uploading, managing, organizing, and interacting with Vimeo videos through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to a user's Vimeo account via Maton, perform read and list operations by default, and, with explicit approval, upload, organize, or modify Vimeo resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton acts as the gateway for Vimeo account access, so installation is a supply-chain and account-access trust decision.

Mitigation: Install only if you trust Maton, prefer OAuth, and choose the narrowest Vimeo scopes available for the task.

Risk: Write, delete, connection, function, trigger, and automation operations can change Vimeo data or create ongoing behavior.

Mitigation: Confirm the target resource, payload, intended effect, and automation scope with the user before each operation.

Risk: Raw API-key mode uses a long-lived credential and can expose the key through environment variables or shell history.

Mitigation: Use CLI OAuth when possible; use raw API-key mode only where the CLI cannot be installed and rotate any key that was printed, committed, or pasted.

Risk: Trigger destinations can create persistent forwarding of matching events to a URL.

Mitigation: Prefer platform destinations such as api.maton.ai or *.maton.app, forward only the minimum fields needed, and require explicit approval for any third-party host.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/vimeo)
- [Maton Homepage](https://maton.ai)
- [Vimeo API Reference](https://developer.vimeo.com/api/reference)
- [Vimeo Developer Portal](https://developer.vimeo.com)
- [Vimeo API Authentication](https://developer.vimeo.com/api/authentication)
- [Vimeo Upload API](https://developer.vimeo.com/api/upload/videos)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)
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

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with bash, Python, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include authenticated Maton API calls; connection, write, delete, function, trigger, and automation steps require explicit user approval.]

## Skill Version(s):

1.2.2 (source: server release metadata; frontmatter metadata.version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
