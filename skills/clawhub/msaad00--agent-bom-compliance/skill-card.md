## Description:

AI compliance and policy engine that evaluates scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use this skill to evaluate AI infrastructure scan results against security and regulatory frameworks, enforce policy-as-code rules, and generate SBOMs or compliance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned package installation can install a newer package version than the reviewed 0.104.0 release.

Mitigation: Install from a trusted disclosed source and pin package installation to version 0.104.0 when reproducing this release.

Risk: Optional CIS benchmark checks use locally configured cloud credentials to make read-only calls to cloud provider APIs.

Mitigation: Provide cloud credentials only for the provider checks the operator explicitly chooses to run, and use least-privilege read-only credentials.

## Reference(s):

- [agent-bom GitHub project](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard for agent-bom](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)
- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline commands, policy examples, and report guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce SBOM guidance for CycloneDX or SPDX formats and compliance-report instructions.]

## Skill Version(s):

0.104.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
