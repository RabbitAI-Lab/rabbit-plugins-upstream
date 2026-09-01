## Description:

Shadow Memory continuously commits agent work into a persistent .origin project state so new sessions can recover context, inspect change history, and explain why current values exist.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to persist project state across sessions, coordinate multi-agent work, and trace decisions, tasks, risks, facts, and modules through explicit semantic commits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill promotes an unrelated external installer executable without verification or a clear connection to the memory tool.

Mitigation: Review the U-King installer section carefully and do not run the linked executable unless it is independently trusted and verified.

Risk: Persisted project state may retain secrets, credentials, personal data, or confidential chat content for later reuse.

Mitigation: Keep the .origin package in a project-specific location and avoid committing sensitive or confidential information.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/benxiang-memory)
- [Publisher profile](https://clawhub.ai/user/dongsheng123132)
- [Benxiang protocol repository](https://github.com/dongsheng123132/2origin.git)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides setup and use of an MCP memory server that persists project state in a local .origin package.]

## Skill Version(s):

1.1.0 (source: server release evidence and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
