## Description:

Use TokST to retrieve, store, govern, and hand off durable context across cloud workspaces or Local SQLite.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anthemty](https://clawhub.ai/user/anthemty)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect agents to TokST memory, search prior context, store durable facts and decisions, manage sessions, and configure Cloud or Local SQLite workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill tells agents to silently save and reuse context across sessions, which can preserve sensitive, regulated, client, or cross-project information if used without scoping.

Mitigation: Use local mode or a narrowly scoped workspace where possible, avoid automatic silent storage for sensitive work, and do not store secrets, private credentials, raw chain-of-thought, or transient tool output.

Risk: The skill includes remote installer commands that execute scripts from TokST URLs.

Mitigation: Inspect or verify remote installer scripts before running them, especially in confidential or regulated environments.

Risk: Cloud and MCP workflows can expose durable memory through API keys, OAuth channels, or workspace roles if credentials or permissions are mismanaged.

Mitigation: Use dedicated API keys per client, keep keys in protected settings, revoke unused keys, and review workspace roles before enabling shared memory.

## Reference(s):

- [TokST Documentation](https://tokst.com/docs)
- [TokST Help Center](https://tokst.com/help)
- [TokST MCP Setup](https://tokst.com/docs/mcp)
- [TokST Sessions](https://tokst.com/docs/sessions)
- [TokST Local](https://tokst.com/docs/local)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with inline shell and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent-facing memory workflow instructions, CLI commands, MCP configuration examples, and operational guidance.]

## Skill Version(s):

0.7.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
