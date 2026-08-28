## Description:

AI compliance and policy engine that evaluates scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security teams, and compliance reviewers use this skill to evaluate AI infrastructure findings against common security and regulatory frameworks, enforce policy-as-code checks, and generate SBOM or compliance outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad compliance-related trigger phrases may cause the skill to be invoked for generic compliance requests.

Mitigation: Use it when compliance, SBOM, or policy reporting is intended, and review proposed actions before execution.

Risk: Optional CIS benchmark checks can use locally configured AWS, Azure, GCP, or Snowflake credentials for read-only account inspection.

Mitigation: Run CIS checks only when explicitly intended, use scoped read-only credentials where possible, and do not paste secrets into the agent conversation.

Risk: Compliance reports and SBOM results may be incomplete or misleading if source scan data, SBOM files, or policies are incomplete.

Mitigation: Validate the input files and review generated reports against the target framework requirements before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline commands and structured compliance or SBOM outputs such as JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference user-provided SBOM or policy files; optional CIS benchmark checks use locally configured cloud SDK credentials for read-only provider API calls.]

## Skill Version(s):

0.102.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
