## Description:

Helps evaluate AI security scan results against compliance frameworks, check policies, and generate SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess scan results against AI security and regulatory frameworks, enforce policies, and generate SBOMs or compliance reports. Optional CIS checks inspect cloud accounts only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS checks inspect cloud accounts using existing credentials.

Mitigation: Run them only when intentionally requested, use operator-configured credentials, and do not disclose secrets in reports or chat.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage listed in skill metadata](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Compliance reports, SBOM files, Policy results, Shell commands, Guidance]

**Output Format:** [Markdown guidance and commands; compliance reports and CycloneDX or SPDX SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local compliance, policy, and SBOM checks need no cloud credentials; optional CIS checks use operator-configured cloud credentials.]

## Skill Version(s):

0.108.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
