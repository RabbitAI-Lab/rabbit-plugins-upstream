## Description:

Zoho Projects API V3 integration with managed OAuth for managing projects, tasks, milestones, tasklists, and team collaboration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project operators use this skill to work with Zoho Projects through Maton for project, task, milestone, tasklist, time tracking, and collaboration workflows. It supports read/list-first API work and requires explicit user confirmation before creating, updating, or deleting project data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Maton or Zoho credentials could be exposed or over-scoped.

Mitigation: Prefer OAuth, keep credentials in the operating system credential store, grant only needed Zoho scopes, and do not print, persist, or export tokens.

Risk: Write operations can create, update, or delete Zoho Projects data.

Mitigation: Default to read/list calls, verify identifiers and account context, and require explicit user confirmation before POST, PUT, PATCH, or DELETE requests.

Risk: API responses may contain personal data or untrusted content.

Mitigation: Extract only fields needed for the task, avoid logging raw responses, and treat returned content as data rather than instructions.

Risk: Raw HTTP fallback with a long-lived API key can broaden credential exposure.

Mitigation: Use the CLI and OAuth when possible; use raw HTTP only where the CLI cannot be installed and keep the API key out of command lines and files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/zoho-projects)
- [Maton homepage](https://maton.ai)
- [Zoho Projects API V3 Documentation](https://projects.zoho.com/api-docs)
- [Zoho Projects Developer Portal](https://www.zoho.com/projects/help/rest-api/zohoprojectsapi.html)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and API request templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and explicit user confirmation before write operations.]

## Skill Version(s):

1.2.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
