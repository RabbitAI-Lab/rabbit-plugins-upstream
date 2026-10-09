## Description:

Helps agents evaluate AI security and compliance findings against common frameworks, check policies, and generate SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to request compliance and policy checks on AI infrastructure scan results, generate SBOMs, and optionally run cloud CIS benchmark checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS checks access cloud provider APIs using configured credentials and may expose more account information than needed.

Mitigation: Run CIS checks only after explicit confirmation and use a minimally privileged cloud profile.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [Python package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with compliance guidance and example commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide generation of CycloneDX or SPDX SBOMs and compliance reports.]

## Skill Version(s):

0.108.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
