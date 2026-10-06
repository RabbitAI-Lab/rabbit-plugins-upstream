## Description:

Helps agents assess MCP server registry entries, pre-install trust, fleet risk, skill trust, and code-scanning findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to check MCP servers before installation, assess server inventories and skill files, and review code-scanning results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional code scanning may read user-selected source files.

Mitigation: Review and limit the files selected for scanning.

Risk: Optional Snyk enrichment sends requests to a third party and requires a token.

Mitigation: Enable enrichment only when intended; keep SNYK_TOKEN in the operator environment and out of skill output.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry lookups use bundled data; optional code scans may read selected source files.]

## Skill Version(s):

0.108.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
