## Description:

Helps evaluate AI scan results against security and regulatory frameworks, enforce policies, and generate compliance reports and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security teams use this skill to assess AI infrastructure scan results against compliance frameworks, apply policies, and prepare SBOMs or compliance reports. Optional cloud CIS assessments require explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional cloud CIS checks access cloud accounts using configured credentials.

Mitigation: Run only after user confirmation with accounts and profiles intended for read-only assessment; never paste or display secrets.

Risk: Installing a package or image introduces supply-chain exposure.

Mitigation: Review the package source or pin the package or image where strict supply-chain controls apply.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Agent-BOM project homepage](https://github.com/msaad00/agent-bom)
- [Agent-BOM on PyPI](https://pypi.org/project/agent-bom/)
- [Agent-BOM OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Compliance reports, SBOMs]

**Output Format:** [Markdown guidance and commands; generated SBOMs in CycloneDX or SPDX format]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud CIS checks are optional and require user confirmation.]

## Skill Version(s):

0.108.4 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
