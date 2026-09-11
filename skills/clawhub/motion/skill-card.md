## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, recurring tasks, and scheduled work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and manage Motion tasks, projects, workspaces, users, comments, recurring tasks, schedules, statuses, and custom fields through Maton's authenticated gateway.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Motion account access is routed through Maton and can expose task, project, workspace, user, comment, schedule, and custom-field data from the connected account.

Mitigation: Install only if the user trusts Maton, prefer OAuth, connect only needed accounts, and choose the narrowest Motion scopes available.

Risk: Write and delete requests can change or remove Motion resources, including tasks, projects, comments, recurring tasks, and custom fields.

Mitigation: Default to read and list calls, verify resource identifiers first, and confirm the exact target, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Raw HTTP fallback with MATON_API_KEY uses a long-lived credential that can leak through logs, shell history, child processes, or persisted files.

Mitigation: Use the CLI with OAuth when possible; when an API key is required, keep it in the process environment only, never print or persist it, send it only to api.maton.ai, and rotate it if exposed.

Risk: Multiple Maton profiles or Motion connections can cause reads or writes to target the wrong account.

Mitigation: List active connections before sensitive work and specify the intended connection and profile whenever there is ambiguity.

## Reference(s):

- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, Code, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON payloads, and optional Python or JavaScript snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Motion resource identifiers, request payloads, filtered API responses, and confirmation prompts for write or delete actions.]

## Skill Version(s):

1.2.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
