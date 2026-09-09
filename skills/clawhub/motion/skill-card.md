## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, recurring tasks, and related scheduled work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and manage Motion tasks, projects, workspaces, comments, recurring tasks, schedules, statuses, and custom fields through Maton-managed access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Motion account access is granted through Maton OAuth or API credentials.

Mitigation: Install only if Maton is trusted, prefer OAuth over long-lived API keys, and select the narrowest Motion scopes available.

Risk: Write operations can create, update, move, or delete Motion data in the connected account.

Mitigation: Confirm the exact account, connection, target resource, payload, and intended effect before any POST, PUT, PATCH, or DELETE request.

Risk: Raw HTTP fallback requires handling a long-lived Maton API key.

Mitigation: Use the CLI when available; when raw HTTP is necessary, keep the key in the process environment, avoid logging or persisting it, and rotate it if exposed.

## Reference(s):

- [Motion skill page](https://clawhub.ai/byungkyu/skills/motion)
- [Publisher profile](https://clawhub.ai/user/byungkyu)
- [Maton homepage](https://maton.ai)
- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code, markdown]

**Output Format:** [Markdown with inline shell commands, JSON examples, and Python or JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce API request examples and structured response-handling guidance for Motion resources.]

## Skill Version(s):

1.2.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
