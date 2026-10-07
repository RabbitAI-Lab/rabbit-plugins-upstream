## Description:

Helps agents check package vulnerabilities, scan container images and local agent environments, verify package integrity, and generate SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to check package CVEs, inspect container images and agent dependencies, assess vulnerability impact, and prepare scan reports or SBOMs. Full discovery can inspect local agent and service configuration files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A full scan may broadly read local agent and service configuration files in the user's home directory.

Mitigation: Review the listed discovery paths first, and prefer targeted package checks or image scans when full local discovery is unnecessary.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Project homepage listed in skill metadata (not verified import provenance)](https://github.com/msaad00/agent-bom)
- [PyPI package listed in skill metadata](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard listed in skill metadata](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands, Reports]

**Output Format:** [Markdown or text guidance; scan reports in JSON, SARIF, HTML, or Markdown; CycloneDX or SPDX SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vulnerability findings, impact analysis, remediation priorities, and package integrity checks.]

## Skill Version(s):

0.108.1 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
