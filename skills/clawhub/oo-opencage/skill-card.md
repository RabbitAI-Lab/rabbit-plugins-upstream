## Description:

OpenCage helps agents geocode addresses, return GeoJSON geocoding results, and reverse geocode latitude and longitude coordinates through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to look up OpenCage geocoding results, convert coordinates to address data, and format geocoding responses as GeoJSON.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan flags unsafe one-line remote installer commands for the oo CLI.

Mitigation: Prefer a pinned, signed, or package-manager CLI installation path and review the installer before use.

Risk: The security scan flags overbroad or mismatched capability labels for a read-oriented geocoding skill.

Mitigation: Inspect the live action schema before execution and confirm the exact payload and effect with the user for any action tagged as write or destructive.

Risk: Authentication, connection, or billing failures can interrupt OpenCage connector actions.

Mitigation: Run setup or recovery steps only after matching failures, and keep credential handling within the connected OOMOL account.

## Reference(s):

- [OpenCage Homepage](https://opencagedata.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Skill Listing](https://clawhub.ai/oomol/skills/oo-opencage)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful connector actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
