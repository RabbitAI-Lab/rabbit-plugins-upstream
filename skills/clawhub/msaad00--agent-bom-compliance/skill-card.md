## Description:

AI compliance and policy engine that evaluates scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use this skill to evaluate AI infrastructure scan results against common security and regulatory frameworks, enforce policy-as-code rules, generate SBOMs, and produce compliance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS benchmark checks can access cloud account metadata through configured provider credentials.

Mitigation: Use dedicated read-only cloud profiles and confirm the selected account or tenant before allowing provider API access.

Risk: The release depends on a third-party package source.

Mitigation: Install only after verifying that the third-party agent-bom package source is trusted for the target environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline examples and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference local SBOM or policy files supplied by the user; optional CIS checks may call read-only cloud provider APIs when explicitly invoked.]

## Skill Version(s):

0.100.0 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
