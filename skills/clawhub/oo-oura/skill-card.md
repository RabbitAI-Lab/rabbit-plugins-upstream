## Description:

Oura enables an agent to read health and personal data from an Oura account through the OOMOL-connected Oura connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Oura action schemas and retrieve activity, readiness, sleep, SpO2, stress, resilience, heart-rate, workout, session, tag, ring, and account records from a connected Oura account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes unverified remote installer commands for the oo CLI that could execute arbitrary code.

Mitigation: Review the installer source first and prefer a pinned, signed, or package-manager installation path before using the skill.

Risk: The skill can read sensitive Oura health and personal data through a connected OOMOL account.

Mitigation: Use the skill only when that access is intended and confirm the connected account and requested data scope before retrieval.

## Reference(s):

- [Oura homepage](https://ouraring.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oura)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing Oura action payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
