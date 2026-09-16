## Description:

This skill supports Juniper Mist requests involving searching and reading data through the OOMOL-connected Juniper Mist connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and network operators use this skill to inspect Juniper Mist administrator, organization, site, and device information through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Juniper Mist profile, organization, site, and device data is routed through OOMOL.

Mitigation: Install and use the skill only when that third-party routing is acceptable for the connected Juniper Mist account and data classification.

Risk: The first-time setup section includes one-line installer commands that execute remote scripts.

Mitigation: Prefer a verified, signed, or package-manager installation path for the oo CLI before using the connector.

Risk: The connector may expose broader actions than the listed read operations.

Mitigation: Use only the listed read actions by default, and require explicit user approval before any broader, write, or destructive connector action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-juniper-mist)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Juniper Mist homepage](https://www.juniper.net/us/en/products/networking/mist-ai.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing JSON payloads.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
