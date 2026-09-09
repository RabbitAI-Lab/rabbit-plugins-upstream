## Description:

agent-bom compliance evaluates AI infrastructure scan results against security and regulatory frameworks, enforces policy-as-code, and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and compliance teams use this skill to assess AI infrastructure scan results against frameworks such as OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, AISVS, and related controls. It also supports policy checks and SBOM generation for compliance reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional CIS benchmark checks can use cloud credentials and make read-only calls to AWS, Azure, GCP, or Snowflake APIs.

Mitigation: Use least-privilege read-only credentials and confirm the target provider account, tenant, or project before invoking CIS checks.

Risk: Installing or invoking the referenced package trusts the upstream package source.

Mitigation: Install only when the publisher and package source are trusted, and review package provenance before operational use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-compliance)
- [agent-bom source repository](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OpenSSF Scorecard](https://securityscorecards.dev/viewer/?uri=github.com/msaad00/agent-bom)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline command examples and structured compliance or SBOM output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local compliance analysis, policy-check guidance, SBOM generation instructions, and optional read-only cloud benchmark guidance.]

## Skill Version(s):

0.103.2 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
