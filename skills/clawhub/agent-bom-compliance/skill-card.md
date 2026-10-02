## Description:

Evaluates AI infrastructure scans against security and compliance frameworks, checks policy rules, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to evaluate scan results against AI security and compliance frameworks, enforce policies, and generate SBOMs or compliance reports. Optional CIS checks assess configured cloud accounts when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS checks access cloud account data using locally configured credentials.

Mitigation: Run cloud benchmarks only when intended, confirm the target account, and use appropriately scoped credentials.

Risk: Compliance reports may be mistaken for a complete certification assessment.

Mitigation: Review findings and framework coverage with a qualified compliance owner before relying on them for decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Text or Markdown reports; JSON or SARIF findings; CycloneDX or SPDX SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional cloud benchmark results require an explicitly requested check.]

## Skill Version(s):

0.107.2 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
