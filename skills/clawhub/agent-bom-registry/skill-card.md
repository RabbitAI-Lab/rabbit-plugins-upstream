## Description:

Looks up MCP servers in a security registry and helps assess marketplace packages, skill trust, fleet risk, and code-scan findings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security reviewers use this skill to check MCP servers before installation, assess skill files and server inventories, and review code-scan findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation adds a third-party Python package, and requested scans may read local skill files or code.

Mitigation: Install only if the package is acceptable to your environment, and scan only files or paths you intend to share with the tool.

Risk: Optional vulnerability enrichment may use an external service and an access token.

Mitigation: Enable it only when needed; keep SNYK_TOKEN in the operator environment and out of skill output.

## Reference(s):

- [Project homepage (listed in skill metadata; provenance unavailable)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [Project security scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry matches, trust assessments, risk scores, or scan findings, depending on the requested check.]

## Skill Version(s):

0.107.2 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
