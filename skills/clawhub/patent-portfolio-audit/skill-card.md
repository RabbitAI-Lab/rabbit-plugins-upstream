## Description:

Audits a company or university patent portfolio, summarizes patent status and technology areas, flags estimated upcoming expirations, and exports an asset list.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ip930](https://clawhub.ai/user/ip930)

### License/Terms of Use:

MIT-0

## Use Case:

Patent teams, business analysts, and organizations use this skill to inventory a company or university’s patents, compare legal-status and technology distributions, and prepare an exportable asset list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Patent queries and API credentials are sent to an external PatentMax service.

Mitigation: Confirm the service destination before use and ensure PATENTMAX_BASE_URL is unset or points only to the legitimate service.

Risk: Confidential invention details may be processed by a third party.

Mitigation: Do not submit confidential invention details without accepting third-party processing.

Risk: Broader patent-search workflows can incur paid API charges.

Mitigation: Review the planned searches and monitor paid API usage.

Risk: Trial credentials and task caches may persist on the local device.

Mitigation: Protect and review locally stored files under ~/.patentmax.

Risk: Estimated expiration dates and patent status may not reflect official records.

Mitigation: Confirm material portfolio decisions against the official patent register.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/ip930/skills/patent-portfolio-audit)
- [PatentMax API platform](https://api.ip930.com/features/api-platform)
- [PatentMax API reference](artifact/references/api-reference.md)
- [Patent search workflow](artifact/references/search-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [Markdown summary and UTF-8 CSV patent asset list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CSV lists patent identifiers, legal status, technology area, and estimated expiration year.]

## Skill Version(s):

1.0.1 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
