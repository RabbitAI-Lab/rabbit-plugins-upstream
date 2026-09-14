## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, task lists, time tracking, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and project teams use this skill to work with Zoho Projects through Maton-managed OAuth, including project, task, milestone, task list, time tracking, and collaboration workflows. It is also used to configure user-approved hosted functions and triggers around those Zoho Projects actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoho Projects access can expose business data if broad OAuth scopes or the wrong connection are approved.

Mitigation: Check requested Zoho scopes, prefer OAuth, and confirm the intended connection before calls.

Risk: Write and delete operations, hosted functions, and trigger destinations can change Zoho Projects data or run automation continuously.

Mitigation: Confirm every write/delete operation and each hosted function or trigger destination with the user before execution.

Risk: Long-lived API keys and raw API responses can leak sensitive account or project data if logged, persisted, or pasted into output.

Mitigation: Prefer CLI OAuth; when an API key is unavoidable, keep it out of command lines, files, logs, and user-facing output.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoho-projects)
- [Maton Homepage](https://maton.ai)
- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
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

**Output Format:** [Markdown with shell commands, code snippets, JSON examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Zoho Projects API request paths, Maton CLI commands, hosted function examples, trigger configuration guidance, and instructions to confirm write operations.]

## Skill Version(s):

1.2.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
