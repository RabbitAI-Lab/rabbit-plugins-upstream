## Description:

Evaluate AI scan results against security and regulatory frameworks, enforce policy checks, and generate SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and security or compliance teams use the skill to evaluate AI infrastructure scan results, check custom policies, generate SBOMs, and run explicitly requested cloud CIS checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup examples may scan more local data or use more network access than the privacy description suggests.

Mitigation: Review the setup scan’s access plan before running it. For local-only evaluation, choose explicit input files and disable ambient discovery and network lookups using the installed version’s documented controls. Use scoped read-only credentials for confirmed cloud checks.

## Reference(s):

- [Project homepage](https://github.com/koda-ai-studio/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/koda-ai-studio/agent-bom)
- [ClawHub release](https://clawhub.ai/msaad00/skills/agent-bom-compliance)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files]

**Output Format:** [Compliance findings and reports, policy results, and CycloneDX or SPDX SBOMs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Cloud CIS checks use operator-configured credentials and make read-only provider API calls when explicitly invoked.]

## Skill Version(s):

0.111.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
