## Description:

Retrieve source-backed understanding of public GitHub projects: repository structure, package boundaries, architecture, data flow, and codebase-specific behavior. Use for onboarding, subsystem exploration, implementation research, and repository-grounded Q&A when general library documentation is insufficient.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wei840222](https://clawhub.ai/user/wei840222)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to understand unfamiliar public GitHub repositories, onboard to a codebase, explore subsystems, and ask implementation questions when general library documentation is insufficient.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated wiki content may be incomplete, stale, or inaccurate for the source version being examined.

Mitigation: Use focused questions and verify claims that drive a change against upstream files or official documentation.

Risk: The workflow uses shell and network tools to check public GitHub visibility and query DeepWiki.

Mitigation: Query only repositories confirmed public; keep private repository identifiers, code, and metadata off public DeepWiki routes.

## Reference(s):

- [ClawHub release](https://clawhub.ai/wei840222/skills/deepwiki)
- [DeepWiki MCP guide](https://docs.devin.ai/work-with-devin/deepwiki-mcp)
- [DeepWiki guide](https://docs.devin.ai/work-with-devin/deepwiki)
- [mcporter workflow reference](artifact/references/mcporter-workflow.md)
- [Public MCP fallback reference](artifact/references/api-fallback.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown with source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Focused repository-specific answers; source references when available.]

## Skill Version(s):

1.0.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
