## Description:

Buffer API integration with managed authentication for scheduling and managing social media posts across multiple platforms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and social media operators use this skill to connect a Buffer account through Maton, inspect account and channel data, create ideas, and schedule or manage Buffer posts with explicit approval for writes and new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Granting Maton access to Buffer can expose social media account data and enable posting through the connected account.

Mitigation: Use OAuth where possible, choose least-privilege scopes when offered, and confirm every new connection or write operation before it runs.

Risk: Hosted functions and triggers can automate actions or forward event data beyond the immediate Buffer task.

Mitigation: Create or invoke functions, triggers, and destinations only after separate user approval; prefer private functions with DENY_ALL network policy unless a specific destination is required.

Risk: API keys and raw response bodies can expose long-lived credentials or personal/business data if copied into the environment, logs, or files.

Mitigation: Prefer stored OAuth credentials, avoid MATON_API_KEY unless the CLI cannot be installed, and extract only task-needed response fields.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/buffer-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Buffer API Documentation](https://developers.buffer.com/reference.html)
- [Buffer API Getting Started](https://developers.buffer.com/guides/getting-started.html)
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

**Output Type(s):** [guidance, shell commands, code, configuration, markdown]

**Output Format:** [Markdown guidance with bash, JSON, Python, and GraphQL examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs guide authenticated Buffer API calls through Maton, including optional hosted functions and trigger configuration when the user explicitly approves automation.]

## Skill Version(s):

1.2.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
