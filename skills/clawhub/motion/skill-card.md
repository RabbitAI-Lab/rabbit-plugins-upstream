## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, recurring tasks, schedules, statuses, and custom fields through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to connect a Motion account through Maton and read or manage scheduled work, including tasks, projects, workspaces, comments, recurring tasks, schedules, statuses, and custom fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, or delete resources in the connected Motion account.

Mitigation: Default to read and list calls, then require explicit user confirmation of the target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Installing and using the skill grants Maton-mediated access to the user's Motion account.

Mitigation: Prefer OAuth, connect only accounts needed for the task, choose least-privilege scopes when available, and revoke unused connections.

Risk: API keys or provider credentials can be exposed if printed, stored in files, or passed through shell history.

Mitigation: Use OAuth where possible; when API keys are unavoidable, keep them in the credential store or stdin-only HTTP configuration and never log, print, or persist tokens.

## Reference(s):

- [Maton Homepage](https://maton.ai)
- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Code, Guidance]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Motion API responses are JSON; write operations require explicit user confirmation before execution.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter reports 1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
