## Description:

Google Slides API integration with managed OAuth for creating presentations, adding slides, inserting content, and managing slide formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agent operators, and users with a Maton account use this skill to inspect and update Google Slides presentations through an approved Google Slides connection. It supports read-first API workflows, user-confirmed writes, and optional user-approved automation around Slides actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access or modify Google Slides data for the connected account.

Mitigation: Use OAuth where possible, select only task-required scopes, default to read and list calls, and get explicit user confirmation before writes or new connection creation.

Risk: Long-lived API keys can expose account access if placed in environment variables or copied into raw HTTP workflows.

Mitigation: Prefer Maton OAuth and the operating system credential store; use raw HTTP only when the CLI cannot be installed and avoid exporting MATON_API_KEY unless the user has accepted that exposure.

Risk: Automation through functions, triggers, or third-party destinations can repeatedly act on or disclose user data after setup.

Mitigation: Require user-reviewed handlers, explicit approval for each deploy or trigger destination, DENY_ALL network policy unless a host is specifically approved, and remove unused connections, functions, triggers, or destinations when finished.

## Reference(s):

- [ClawHub Google Slides Skill](https://clawhub.ai/byungkyu/skills/google-slides)
- [Maton Homepage](https://maton.ai)
- [Google Slides API Reference](https://developers.google.com/slides/api/reference/rest)
- [Google Slides Presentations API](https://developers.google.com/slides/api/reference/rest/v1/presentations)
- [Google Slides BatchUpdate API](https://developers.google.com/slides/api/reference/rest/v1/presentations/batchUpdate)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Time Trigger Reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and a user-approved Google Slides connection; writes and automation setup require explicit user confirmation.]

## Skill Version(s):

1.2.3 (source: server release metadata; artifact frontmatter version is 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
