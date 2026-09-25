## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, tasklists, time tracking, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Zoho Projects work items, milestones, tasklists, time tracking, and collaboration through Maton-managed OAuth. It supports read/list workflows by default and documents approval-gated writes, hosted functions, and trigger-based automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorized calls can change Zoho Projects data such as projects, tasks, milestones, tasklists, and collaboration records.

Mitigation: Default to read and list calls, verify the target account and resource identifiers, and get explicit user approval before any create, update, delete, or workflow action.

Risk: Broad or stale connections, functions, and triggers can keep access or automation active after the immediate task is done.

Mitigation: Use OAuth where possible, choose least-privilege scopes, approve each automation separately, and remove unused connections, functions, and triggers when finished.

Risk: Trigger destinations can create persistent event forwarding to a URL.

Mitigation: Create or update destinations only after confirming the exact host, event fields, persistence, and credential handling; avoid broad trigger destinations and remove unused destinations.

Risk: Long-lived API keys can be exposed through environment variables or raw HTTP workflows.

Mitigation: Prefer Maton OAuth and the CLI credential store; use raw HTTP with MATON_API_KEY only where the CLI cannot be installed and avoid printing, exporting, or embedding credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-projects)
- [Maton homepage](https://maton.ai)
- [Maton API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)
- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [Time trigger catalog](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with bash, JSON, Python, and HTTP examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and OAuth or a valid Maton API key; write and automation actions require explicit user approval.]

## Skill Version(s):

1.2.5 (source: server release metadata; artifact frontmatter lists 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
