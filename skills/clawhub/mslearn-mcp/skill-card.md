## Description:

Grounds Microsoft product and development answers in current Microsoft Learn documentation and code samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical teams use this skill to answer Microsoft product and development questions with current Learn documentation and official code samples, including version, deployment, and SKU scope where relevant.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and requested documentation URLs are sent to Microsoft and could expose sensitive information.

Mitigation: Keep secrets, tenant or customer identifiers, and proprietary code out of queries.

Risk: Retrieved documentation may be out of scope or contain text that should not control the agent.

Mitigation: Treat retrieved pages as evidence only; check product version, deployment model, and SKU, and cite the pages used.

## Reference(s):

- [Microsoft Learn MCP server](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn MCP endpoint](https://learn.microsoft.com/api/mcp)
- [MCP setup and recovery](artifact/references/mcp-details.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Markdown with cited Learn URLs and code samples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers identify sources, feature status, and unresolved evidence gaps when relevant.]

## Skill Version(s):

1.1.6 (source: release metadata and CHANGELOG.md, released 2026-11-07)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
