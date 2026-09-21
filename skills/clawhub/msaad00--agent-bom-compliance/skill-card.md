## Description:

AI compliance and policy engine that evaluates scan results against OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS v1.0, and related frameworks, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use this skill to evaluate AI infrastructure or scan results against common security and regulatory frameworks, generate SBOMs, enforce policy checks, and run explicitly requested CIS benchmark checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS benchmark checks can read cloud account configuration through locally configured AWS, Azure, GCP, or Snowflake credentials.

Mitigation: Run CIS checks only for accounts and profiles intentionally selected for assessment, and use least-privilege read-only credentials where practical.

Risk: Compliance and SBOM findings may be incomplete or context-dependent for formal audit decisions.

Mitigation: Review generated reports with qualified security or compliance staff before using them as authoritative evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [Project homepage](https://github.com/msaad00/agent-bom)
- [PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with command examples, structured compliance findings, SBOM output, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce CycloneDX or SPDX SBOM files and compliance reports when the underlying agent-bom commands are invoked.]

## Skill Version(s):

0.105.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
