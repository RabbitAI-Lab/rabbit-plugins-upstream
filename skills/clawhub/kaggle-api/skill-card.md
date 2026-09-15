## Description:

Kaggle API integration with managed authentication for accessing datasets, models, competitions, and kernels.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation builders use this skill to search, download, and interact with Kaggle resources through a managed Maton connection. It also guides approved hosted functions or scheduled/event-triggered automation that performs Kaggle actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dependency installation may trust an unintended Maton package or Homebrew tap.

Mitigation: Verify package names and tap source before installation, avoid elevated installs, and use the pinned versions documented by the skill.

Risk: Long-lived API keys can leak through environment variables, logs, shell history, or child processes.

Mitigation: Prefer OAuth login and the operating system credential store; use MATON_API_KEY only when the CLI cannot be installed and rotate it if exposed.

Risk: Hosted functions, triggers, or destinations can continue running or forwarding data after setup.

Mitigation: Require explicit approval for each create, update, deploy, invocation, trigger, or destination; review scope and destination host, and remove automation when no longer needed.

Risk: Kaggle resources and connected trigger payloads may contain personal, private, or business data.

Mitigation: Use least-privilege connections, forward only required fields, avoid logging raw responses or payloads, and keep destinations inside Maton unless the user approves a named external host.

## Reference(s):

- [ClawHub Kaggle Skill](https://clawhub.ai/byungkyu/skills/kaggle-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Kaggle API Documentation](https://www.kaggle.com/docs/api)
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [Kaggle Models](https://www.kaggle.com/models)
- [Kaggle Competitions](https://www.kaggle.com/competitions)
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

**Output Type(s):** [API Calls, Shell commands, Code, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with shell, JSON, Python, and JavaScript code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses managed Maton authentication; defaults to read/list operations and requires user confirmation for writes, new connections, hosted functions, triggers, and destinations.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
