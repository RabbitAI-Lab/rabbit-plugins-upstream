## Description:

Checks MCP server registry entries, marketplace packages, skill files, and code for security and trust concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to look up MCP server trust information, assess skill files, and review code scan findings before installation or deployment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing agent-bom with pip or pipx fetches and runs an external package.

Mitigation: Review and approve the package and its dependencies before installation.

Risk: Optional vulnerability enrichment sends requests to a third-party service using SNYK_TOKEN.

Mitigation: Enable enrichment only when intended, and keep the token in the operator environment rather than skill output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Text, Shell commands]

**Output Format:** [Text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Registry matches, trust assessments, fleet risk scores, and optional code scan findings.]

## Skill Version(s):

0.108.1 (source: server release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
