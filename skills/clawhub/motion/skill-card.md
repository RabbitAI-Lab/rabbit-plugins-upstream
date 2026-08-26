## Description:

Motion API integration with managed OAuth for managing tasks, projects, workspaces, comments, recurring tasks, and scheduled work through the Maton CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to query and manage Motion tasks, projects, workspaces, comments, recurring tasks, schedules, statuses, and custom fields through authenticated Maton API calls. It is suited for workflows that need read-first Motion account access with explicit confirmation before writes or new connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent can access Motion data through a connected Maton account.

Mitigation: Install only when Motion access is intended, review connection prompts, and choose the narrowest available Motion scopes.

Risk: Creating, updating, deleting, or commenting on Motion resources can change account data.

Mitigation: Require explicit confirmation of the exact resource, payload, and intended effect before any data-changing action.

Risk: API-key authentication can expose a long-lived credential more easily than OAuth.

Mitigation: Prefer Maton OAuth and avoid printing, logging, persisting, or passing credentials on command lines.

## Reference(s):

- [Motion skill page](https://clawhub.ai/byungkyu/skills/motion)
- [Maton homepage](https://maton.ai)
- [Motion API Documentation](https://docs.usemotion.com/)
- [Motion API Reference](https://docs.usemotion.com/api-reference)
- [Motion Cookbooks](https://docs.usemotion.com/cookbooks/getting-started)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with shell commands, JSON examples, and SDK snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Maton OAuth/CLI access; defaults to read and list calls and requires confirmation for writes, deletions, and new connections.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
