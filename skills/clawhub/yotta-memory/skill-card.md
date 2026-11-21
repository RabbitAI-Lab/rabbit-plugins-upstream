## Description:

Yotta-memory gives AI agents persistent, file-based memory for restoring context, saving important information, and carrying work across sessions, with shared facts and agent-private memories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agent users use it to restore relevant context at the start of a task, capture durable information as work proceeds, and prepare handoffs across sessions or agents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Potential exposure of private memories, as reported in the release security summary.

Mitigation: Review access controls before use and avoid storing sensitive private memories until that review is complete.

Risk: Plaintext network traffic, as reported in the release security summary.

Mitigation: Review the network path before connecting remotely; keep remote access disabled until the risk is assessed.

Risk: Unsafe handling of imported data, as reported in the release security summary.

Mitigation: Review imported memory content before loading it into the memory store.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-memory)
- [Project homepage](https://github.com/YottaMeta/yotta-memory)
- [Protocol reference](references/protocol.md)
- [Provider protocol reference](references/provider-protocol.md)
- [FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON, Files]

**Output Format:** [Natural language guidance, shell command examples, Markdown memory files, and structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs vary by command; memory data and reports are stored or returned as readable text or structured data.]

## Skill Version(s):

0.24.4 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
