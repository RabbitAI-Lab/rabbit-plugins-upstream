## Description:

Provides access to a 1,356-entry MCP server security registry for lookups, pre-install checks, fleet risk scoring, skill trust assessment, and SAST code scans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams can use this skill to check MCP servers before installation, assess skill files, score server fleets, verify skill provenance, and run static code scans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A clean scan does not guarantee safety or that the skill's guidance fits a particular use.

Mitigation: Review the skill's instructions and decide whether they fit the intended use before installing.

Risk: Optional Snyk code-scan enrichment sends authenticated requests to Snyk and uses SNYK_TOKEN.

Mitigation: Keep the optional token in the operator environment and do not print or embed it in skill output.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-registry)
- [Project homepage (listed in skill metadata)](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text, Guidance]

**Output Format:** [Structured registry results, security assessments, risk scores, scan findings, and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on bundled registry coverage; SAST scanning can use optional Semgrep, and optional Snyk enrichment requires SNYK_TOKEN.]

## Skill Version(s):

0.115.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
