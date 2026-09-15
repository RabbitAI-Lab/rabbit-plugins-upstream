## Description:

NASA (nasa.gov). Use this skill for NASA search and read-data requests through OOMOL's NASA connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to retrieve NASA data through the OOMOL oo CLI connector, including Astronomy Picture of the Day metadata, near-Earth object records, DONKI space-weather events, and EPIC imagery metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NASA requests and payloads are routed through OOMOL's connector.

Mitigation: Use the skill only when OOMOL's NASA connector is intended, and avoid including sensitive context in connector payloads.

Risk: The artifact includes remote oo CLI installer commands.

Mitigation: Do not run the installer commands unless the oo CLI installation source has been independently trusted and verified.

Risk: The security verdict is suspicious.

Mitigation: Review the skill before installing or deploying it.

## Reference(s):

- [NASA homepage](https://www.nasa.gov)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nasa)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-oriented NASA connector actions through the oo CLI and returns connector response data with execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
