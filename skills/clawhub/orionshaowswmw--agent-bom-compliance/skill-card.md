## Description:

Agent BOM Compliance evaluates AI agent systems and software supply chains against common security and compliance frameworks and generates SBOMs and compliance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to assess AI agent projects against frameworks such as OWASP, NIST, SOC 2, ISO 27001, CMMC, EU AI Act, and AISVS, then review generated SBOM and compliance reports before relying on them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional remote enrichment or template fetching may send project-derived data outside the local environment if enabled.

Mitigation: Keep scans local by default and enable remote enrichment only after confirming the endpoint and data shared.

Risk: Generated SBOM and compliance reports may contain project inventory or compliance-sensitive details.

Mitigation: Store generated reports in protected workspace locations and review them before sharing or relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/agent-bom-compliance)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and locally generated SBOM/compliance report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include project inventory and compliance details and should be protected after generation.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
