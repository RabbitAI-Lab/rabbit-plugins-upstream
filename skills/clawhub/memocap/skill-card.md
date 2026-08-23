## Description:

memocap is a local memory skill that guides an agent to retrieve, store, forget, capsule, visualize, and profile durable memories for later recall.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fslong520](https://clawhub.ai/user/fslong520)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use memocap to give an agent durable local memory for preferences, decisions, tasks, context, time capsules, visualization, and profile-style recall.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist broad personal context automatically in local memory.

Mitigation: Install only when durable local memory is desired, review stored data regularly, and use forget or export controls for sensitive or outdated memories.

Risk: Common triggers such as "remember" or "recall" may activate the skill unexpectedly.

Mitigation: Narrow activation triggers where possible and review proposed memory actions before allowing storage.

Risk: Local scripts and data under the memory directory influence future recall behavior.

Mitigation: Review the local scripts and data before use and confirm that the configured memory directory is writable only by trusted users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fslong520/skills/memocap)
- [Publisher profile](https://clawhub.ai/user/fslong520)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and concise status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write, retrieve, export, delete, and visualize local memory data under the user's configured memory directory.]

## Skill Version(s):

2.5.10 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
