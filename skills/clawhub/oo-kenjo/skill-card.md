## Description:

Helps agents manage Kenjo offices and look up related calendars, companies, and departments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Teams using Kenjo can have an agent list and inspect offices, calendars, companies, and departments, or create, update, and delete offices with appropriate approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested remote shell installer has not been verified.

Mitigation: Review or replace it with a trusted official installation method before running it.

Risk: The connected account can modify or delete Kenjo business data.

Mitigation: Check the exact target and payload, and obtain explicit approval before changes or deletion.

Risk: OOMOL intermediates access to the connected Kenjo account.

Mitigation: Use the skill only if you trust OOMOL with that access and accept its permissions.

## Reference(s):

- [Kenjo skill release](https://clawhub.ai/oomol/skills/oo-kenjo)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Kenjo](https://www.kenjo.io/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Text and structured JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Office changes depend on the connected Kenjo account and require confirmation.]

## Skill Version(s):

1.0.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
