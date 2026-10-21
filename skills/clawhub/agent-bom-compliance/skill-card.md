## Description:

Helps agents evaluate AI infrastructure scan results against security and regulatory frameworks, check policies, and generate compliance reports and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to assess scan results against compliance frameworks, check custom policies, and create SBOMs or compliance reports. Optional CIS checks query cloud accounts only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external package requires trust in its source.

Mitigation: Confirm the package source before installing.

Risk: Optional CIS checks access cloud accounts using local credentials.

Mitigation: Run these checks only when intended, using operator-configured credentials; do not paste or print secrets.

Risk: Broad compliance-related phrases may trigger an unwanted workflow.

Mitigation: Invoke the skill only when a compliance, policy, or SBOM task is explicitly requested.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom on PyPI](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard (skill metadata)](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands]

**Output Format:** [Markdown guidance and commands; compliance reports and CycloneDX or SPDX SBOMs when generated]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional CIS checks use locally configured cloud credentials for read-only provider API calls.]

## Skill Version(s):

0.109.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
