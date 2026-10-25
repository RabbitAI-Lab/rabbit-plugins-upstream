## Description:

Guides agents in connecting to Cargo's hosted MCP server, choosing actions, checking costs, running actions, and reading workspace data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to connect an agent to Cargo's hosted MCP server, identify and price available actions, execute single or batch jobs, and query workspace models without installing the CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An agent could act on the wrong Cargo workspace or with broader access than intended.

Mitigation: Confirm the workspace with whoami before acting and use OAuth or a workspace-scoped token with only the permissions needed.

Risk: Batch actions can spend credits before their results or hit rate are known.

Mitigation: Review action costs, test a small batch, and obtain approval for the estimated full batch before proceeding.

Risk: Actions involving personal data or outreach may lack consent or appropriate targeting.

Mitigation: Check lawful basis, suppression status, and job relevance; avoid unsolicited bulk messaging and purchased or scraped lists.

## Reference(s):

- [Cargo MCP skill release](https://clawhub.ai/cargo-ai/skills/cargo-mcp)
- [Cargo skills homepage (skill metadata; not verified source provenance)](https://github.com/getcargohq/cargo-skills)
- [Cargo hosted MCP endpoint](https://mcp.getcargo.io/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands]

**Output Format:** [Markdown with JSON configuration and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Explains workspace checks, action costs, batch outcomes, and when to use the CLI instead.]

## Skill Version(s):

1.1.1 (source: skill frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
