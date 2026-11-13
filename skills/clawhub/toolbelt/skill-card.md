## Description:

This skill helps agents set up Toolbelt and use its shared MCP workspace to ingest documents, query structured and unstructured data, and share findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[toolbeltai](https://clawhub.ai/user/toolbeltai)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and agent users use this skill to connect to a shared Toolbelt workspace for document ingestion, relationship extraction, hybrid queries across structured and unstructured data, and sharing findings across sessions. First-time account provisioning and MCP configuration require user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan noted configuration access and an account setup instruction that may conflict with user expectations; scan coverage was partial.

Mitigation: Review the account setup request and proposed MCP configuration, and proceed only when the endpoint and changes are expected.

## Reference(s):

- [Toolbelt](https://toolbelt.ai)
- [Toolbelt documentation](https://toolbelt.ai/docs)
- [Toolbelt documentation (full text)](https://toolbelt.ai/llms-full.txt)
- [Toolbelt MCP endpoint](https://mcp.toolbelt.ai/mcp)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API calls]

**Output Format:** [Natural-language guidance with JSON configuration examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide user-confirmed account setup and MCP configuration.]

## Skill Version(s):

1.1.5 (source: SKILL.md frontmatter; ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
