## Description:

AI compliance and policy engine for evaluating scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and for generating SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and compliance teams use this skill to evaluate AI infrastructure scan results, enforce policy checks, generate SBOMs, and prepare compliance reports across supported frameworks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS benchmark checks can call cloud provider APIs using locally configured credentials.

Mitigation: Use scoped read-only credentials and confirm the provider and account before running CIS checks.

Risk: Compliance and SBOM outputs depend on the accuracy of user-provided scan data, SBOMs, and policy files.

Mitigation: Review input files and have security or compliance owners validate reports before relying on them for governance decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project Homepage](https://github.com/msaad00/agent-bom)
- [PyPI Package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and structured compliance guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided SBOM files, policy files, and optional cloud provider account context for explicitly requested CIS checks.]

## Skill Version(s):

0.101.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
