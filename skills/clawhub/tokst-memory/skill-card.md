## Description:

Use TokST Cloud MCP for durable memory, shared context, and governed knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to connect to TokST Cloud MCP for durable memory, shared context, knowledge governance, and governed memory lifecycle operations across authorized workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The README documents an optional remote pipe-to-shell CLI installer.

Mitigation: Prefer the direct Cloud MCP setup path; run the optional CLI installer only after independently trusting and verifying it.

Risk: TokST is a cloud memory system, so inappropriate sensitive information could persist in shared durable workspace memory.

Mitigation: Store only information appropriate for durable shared memory, avoid raw secrets, and use Absolute mode only with explicit approval and a clear reason.

Risk: Broad archive or access changes can affect shared memory records.

Mitigation: Confirm the intended Workspace, Atlas, memory ID, or access target before mutation and use traceable lifecycle operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/anthemty/skills/tokst-memory)
- [TokST documentation](https://tokst.com/docs)
- [TokST MCP guide](https://tokst.com/docs/mcp)
- [TokST agent guide](https://tokst.com/llms.txt)
- [TokST full agent context](https://tokst.com/llms-full.txt)
- [TokST MCP discovery](https://api.tokst.com/.well-known/mcp)
- [TokST help](https://tokst.com/help)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with MCP endpoint configuration and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include relevant memory or evidence IDs when they help the user inspect or continue the work.]

## Skill Version(s):

0.9.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
