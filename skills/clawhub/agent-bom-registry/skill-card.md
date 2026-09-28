## Description:

Looks up MCP server security metadata, checks packages before installation, scores server inventories, assesses skill trust, and helps run code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to evaluate MCP servers and skill files before installation or deployment, review fleet risks, and inspect source code for security findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security checks may read skill files or source code selected by the user.

Mitigation: Review the scan scope and avoid supplying sensitive files unnecessarily.

Risk: Optional Snyk enrichment may send scan information to a third party and use SNYK_TOKEN.

Mitigation: Enable enrichment only when approved; keep the token in the operator environment and out of skill output.

Risk: The skill's broad privacy claims may not describe optional network-based enrichment or file reads accurately.

Mitigation: Confirm data handling for the selected operation before running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage listed in skill metadata](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard listed in skill metadata](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text and structured tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include registry matches, risk scores, skill trust assessments, and code scan findings.]

## Skill Version(s):

0.106.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
