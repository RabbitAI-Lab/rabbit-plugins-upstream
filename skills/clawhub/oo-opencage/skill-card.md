## Description:

OpenCage helps an agent run forward, reverse, and GeoJSON geocoding actions through OOMOL's oo CLI and connected OpenCage credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to geocode addresses or place names, reverse-geocode coordinates, and request OpenCage results as GeoJSON through an authenticated OOMOL connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include executing a remotely fetched installer script in a shell without verification.

Mitigation: Use the OpenCage actions only when the OOMOL oo CLI is already trusted; if setup is required, prefer an official package or a download-and-verify process instead of blindly running the one-line installer.

Risk: Authentication, connection, billing, or expired credential states can block connector execution.

Mitigation: Run sign-in and OpenCage connection steps only after a matching command failure, and connect OpenCage intentionally before retrying.

Risk: Connector payload schemas may change over time.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [OpenCage Homepage](https://opencagedata.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-opencage)

## Skill Output:

**Output Type(s):** [shell commands, JSON, GeoJSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands; connector responses are JSON and may include GeoJSON FeatureCollection data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the oo CLI, an OOMOL sign-in, and an OpenCage connection before actions can run.]

## Skill Version(s):

1.0.4 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
