## Description:

Sunsama MCP helps an agent read, create, update, and delete Sunsama tasks, calendar events, channels, objectives, notes, estimates, and related planning data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to manage Sunsama daily planning workflows, including task lifecycle actions, backlog organization, scheduling, recurring tasks, notes, timers, calendar events, and Sunsama help lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify Sunsama tasks, channels, objectives, and calendar events, and security evidence reports that some state-changing actions are not labeled as writes.

Mitigation: Require explicit user confirmation before any action that changes scheduling, notes, ordering, backlog state, restored or deleted state, channels, objectives, or calendar timeboxes; confirm exact targets before destructive actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sunsama-mcp)
- [Sunsama MCP help article](https://help.sunsama.com/docs/integrations/mcp/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON data and execution metadata from the Sunsama MCP connector.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
