## Description:

Gives your agent hands - 120 tools (code audit, lead research, strategy analysis, onchain scoring, credit discovery, prompt defense) over one zero-auth remote MCP endpoint.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zambodotdev](https://clawhub.ai/user/zambodotdev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use Zambo when an agent needs remote execution or structured analysis, such as code audits, lead research, market briefs, onchain scoring, credit discovery, or prompt-injection testing. The skill is most relevant when a task needs tool-backed work rather than pure Q&A or creative writing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Job content is sent to Zambo's remote service.

Mitigation: Avoid sending secrets, credentials, private keys, regulated data, confidential prompts, or proprietary repositories unless there is explicit approval and the service's retention and logging policies are understood.

Risk: The remote MCP endpoint provides broad and mutable tool authority.

Mitigation: Review the tools returned by tools/list before allowing the agent to call them, and keep calls limited to the user's requested job.

Risk: The unpinned npx installer may introduce install supply-chain risk.

Mitigation: Prefer the explicit MCP client configuration that points to https://zambo.dev/api/mcp.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zambodotdev/skills/zambo)
- [Zambo Agent Docs](https://zambo.dev/.well-known/llms.txt)
- [Zambo Human Docs](https://zambo.dev/for-agents/)
- [Zambo Install Docs](https://zambo.dev/install)
- [Zambo MCP Repository](https://github.com/zambodotdev/zambo-mcp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON configuration snippets, shell commands, and tool result receipts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Remote MCP tools return receipts describing the job, tools run, and result; available tool names and parameters should be discovered at runtime with tools/list.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
