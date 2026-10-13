## Description:

Helps agents read and manage SolarWinds Service Desk incidents through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Service desk staff and agents use this skill to list, retrieve, create, update, comment on, and delete SolarWinds Service Desk incidents through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creating, updating, commenting on, or deleting incidents changes service desk data; comments may notify others.

Mitigation: Confirm write payloads and effects with the user; get explicit approval and verify the target before deletion.

Risk: First-time setup may require installing the oo CLI from a third-party installer.

Mitigation: Confirm trust in OOMOL and its installer, and use a verified installation path when possible.

## Reference(s):

- [SolarWinds Service Desk skill release](https://clawhub.ai/oomol/skills/oo-solarwinds-service-desk)
- [SolarWinds Service Desk](https://www.solarwinds.com/service-desk)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown text and JSON service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Incident results may include an execution ID.]

## Skill Version(s):

1.0.0 (source: artifact metadata and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
