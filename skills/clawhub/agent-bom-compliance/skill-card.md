## Description:

Evaluates AI infrastructure scan results against security and regulatory frameworks, applies policy checks, and generates compliance reports and SBOMs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to review AI infrastructure findings against compliance frameworks, enforce policies, and produce software bills of materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an untrusted package or source could expose the operator's environment.

Mitigation: Verify the package and publisher before installing.

Risk: Optional CIS checks access cloud-account settings using configured credentials.

Mitigation: Confirm each cloud check, use least-privilege read-only profiles, and never share secrets in chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Publisher-listed project page](https://github.com/msaad00/agent-bom)
- [Publisher-listed PyPI package](https://pypi.org/project/agent-bom/)
- [Publisher-listed security scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance and command examples; compliance reports and CycloneDX or SPDX SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud benchmark checks are optional and require explicit confirmation.]

## Skill Version(s):

0.106.1 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
