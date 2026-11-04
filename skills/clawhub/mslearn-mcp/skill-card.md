## Description:

Grounds Microsoft product and development answers in current Microsoft Learn documentation and official code samples.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer Microsoft product and development questions with current Learn documentation and official code samples. It returns cited guidance, calls out preview status and evidence gaps, and helps verify product-specific details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries sent to Microsoft could expose secrets, customer identifiers, or proprietary code.

Mitigation: Keep queries generic and exclude secrets, tenant or customer identifiers, and proprietary code.

Risk: The standalone CLI fallback runs downloaded software.

Mitigation: Prefer existing connected tools when available; make persistent setup changes only when requested.

## Reference(s):

- [MCP setup and recovery](references/mcp-details.md)
- [Microsoft Learn MCP endpoint](https://learn.microsoft.com/api/mcp)
- [Microsoft Learn MCP repository](https://github.com/MicrosoftDocs/mcp)
- [Microsoft Learn MCP release notes](https://learn.microsoft.com/en-us/training/support/mcp-release-notes)
- [Microsoft Learn CLI](https://www.npmjs.com/package/@microsoft/learn-cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands]

**Output Format:** [Markdown answers with Learn page links and, when useful, official code samples or CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Identifies preview status and unresolved gaps; fetches at most three pages unless excerpts do not support a cited fact.]

## Skill Version(s):

1.1.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
