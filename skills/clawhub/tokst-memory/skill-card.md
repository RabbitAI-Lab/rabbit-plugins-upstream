## Description:

Use TokST Cloud MCP for durable memory, shared context, and governed knowledge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and external agent users use this skill to connect agents to TokST Cloud MCP for durable memory, shared context, knowledge governance, and agent runtime boundaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CLI setup can execute an unverified remote installer script.

Mitigation: Prefer Cloud MCP with OAuth or a dedicated API key; use the CLI installer only after separately verifying the installer source.

Risk: Selected memory and workspace context are sent to TokST's cloud service.

Mitigation: Install only where that data flow is acceptable, use least-privilege workspaces and tokens, and scope each request to the narrowest Workspace and Atlas.

Risk: Sensitive shared memory can persist under an explicit exception mode and may be visible to authorized workspace members and connected agents.

Mitigation: Avoid storing raw credentials, prefer safe summaries or secret-manager references, and require explicit confirmation with `sensitive: true` and a concise reason before any governed exception.

Risk: Broad memory archive or access changes can affect shared durable knowledge.

Mitigation: Confirm the intended Workspace, Atlas, or memory ID before mutation and rely on traceable update, archive, restore, and audit actions.

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

**Output Format:** [Markdown guidance with MCP endpoint URLs and optional shell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing memory workflow, storage quality, safety, connection, and error recovery guidance.]

## Skill Version(s):

0.9.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
