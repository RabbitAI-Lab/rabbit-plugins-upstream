## Description:

Benxiang Memory is an MCP-based project-state persistence skill that lets agents recover durable project context, commit semantic state changes, inspect history, explain provenance, and diagnose state consistency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dongsheng123132](https://clawhub.ai/user/dongsheng123132)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to persist project decisions, tasks, risks, facts, and module state across conversations so new sessions and collaborating agents can recover context with traceable updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release promotes an unrelated U-King executable installer that is not required for the documented memory workflow.

Mitigation: Do not run the promoted executable unless you independently trust its publisher and verify the installer source.

Risk: The skill creates and updates a persistent .origin project-state package.

Mitigation: Install and use it only when you understand the persistence behavior and are comfortable storing durable project state in that package.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dongsheng123132/skills/benxiang-memory)
- [ClawHub publisher profile](https://clawhub.ai/user/dongsheng123132)
- [U-King website](https://u-king.org)
- [U-King installer download](https://u-claw.org.cn/download/U-King-Setup.exe)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell commands, JSON examples, and MCP tool guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides use of a Node.js stdio MCP server and persistent .origin project-state package.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
