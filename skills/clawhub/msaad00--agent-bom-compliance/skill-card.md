## Description:

AI compliance and policy engine for evaluating scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and for generating SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use this skill to evaluate AI infrastructure scan results against security and regulatory frameworks, enforce policy-as-code rules, run AISVS or CIS benchmark checks, and generate SBOMs or compliance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad compliance-related prompts may activate the skill when the user only mentioned a framework name generically.

Mitigation: Use the skill for explicit compliance, SBOM, policy-evaluation, AISVS, or CIS benchmark requests, and ask for clarification before running provider-specific checks.

Risk: Optional CIS benchmark checks can access AWS, Azure, GCP, or Snowflake APIs with locally configured credentials.

Mitigation: Run CIS checks only in accounts where read-only audit access is intended, rely on configured SDK credentials, and do not paste or print secrets.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project Homepage](https://github.com/msaad00/agent-bom)
- [PyPI Package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or text guidance with shell commands, plus compliance reports and SBOM outputs such as CycloneDX or SPDX JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local compliance, SBOM, AISVS, and policy checks require no credentials; optional CIS checks make read-only calls to configured cloud provider APIs.]

## Skill Version(s):

0.99.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
