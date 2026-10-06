## Description:

Scans agent infrastructure, packages, container images, and filesystems for vulnerabilities, assesses impact and provenance, and helps generate SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security engineers use this skill to check dependency and container vulnerabilities, assess their impact on agent systems, verify packages, and prepare scan reports or SBOMs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A full scan can inspect local agent and MCP configuration files.

Mitigation: Run a targeted package or image check when local agent discovery is not needed.

Risk: Shared scan reports may reveal configuration details.

Mitigation: Review reports for sensitive configuration details before sharing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-scan)
- [Publisher-listed project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown guidance and commands; scan reports may use JSON, SARIF, or CycloneDX/SPDX]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can provide prioritized remediation and vulnerability impact assessments.]

## Skill Version(s):

0.108.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
