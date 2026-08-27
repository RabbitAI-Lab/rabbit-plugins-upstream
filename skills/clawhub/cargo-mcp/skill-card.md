## Description:

Guides agents through connecting to Cargo's hosted MCP server, choosing MCP versus CLI workflows, discovering action costs, executing single or batch actions, polling runs, and reading workspace models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill when an agent needs to connect to Cargo's hosted MCP server, inspect available workspace actions and costs, run actions over one record or a batch, poll completion, and read model records. It also helps decide when a task should use Cargo MCP versus Cargo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent may act in the wrong Cargo workspace if the connected token belongs to a different workspace.

Mitigation: Start each session with whoami and state the resolved workspace before reading records, running actions, or spending credits.

Risk: Batch actions can spend credits or trigger integrations across many records.

Mitigation: Sample 10 to 20 records, report observed cost and hit rate, estimate the full run, and require explicit user approval before the batch.

Risk: API tokens or bearer credentials could be exposed if copied into configuration files directly.

Mitigation: Store tokens in environment variables and reference them from MCP client configuration instead of inlining secret values.

Risk: Actions involving people data can create privacy, consent, or outreach-policy issues.

Mitigation: Require lawful basis, suppression checks, and job relevance before sourcing, enriching, or contacting people, and refuse bulk unsolicited messaging or consumer targeting.

## Reference(s):

- [Cargo skills repository](https://github.com/getcargohq/cargo-skills)
- [Cargo hosted MCP server](https://mcp.getcargo.io/mcp)
- [ClawHub skill page](https://clawhub.ai/cargo-ai/skills/cargo-mcp)
- [ClawHub publisher profile](https://clawhub.ai/user/cargo-ai)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP client configuration snippets, Cargo CLI commands, tool-selection guidance, cost checks, and approval guidance.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
