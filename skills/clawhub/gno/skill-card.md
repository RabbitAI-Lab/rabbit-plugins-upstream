## Description:

Helps agents index and search local documents and notes, retrieve cited answers, and manage a local knowledge base through GNO.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users of local agent tools use this skill to search files and notes, retrieve cited evidence, and organize a personal knowledge base. It also supports optional agent-session lookup, memory, and publishing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing sensitive files may expose their contents to local search or enabled integrations.

Mitigation: Limit indexed collections and avoid indexing secrets unless explicitly accepted.

Risk: Optional remote model backends, network exports, and publishing may send document content outside the machine.

Mitigation: Review egress and publishing settings before enabling remote calls, exports, or uploads.

Risk: Enabling MCP write tools can allow changes to notes and knowledge records.

Mitigation: Leave MCP write tools disabled unless needed and review requested writes.

## Reference(s):

- [GNO ClawHub release](https://clawhub.ai/gmickel/skills/gno)
- [GNO skill documentation](artifact/README.md)
- [GNO CLI reference](artifact/cli-reference.md)
- [GNO MCP reference](artifact/mcp-reference.md)
- [GNO agent installation guide](https://gno.sh/docs/agents-install)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with cited answers and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a separately installed GNO CLI; results depend on indexed local documents.]

## Skill Version(s):

1.2.8 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
