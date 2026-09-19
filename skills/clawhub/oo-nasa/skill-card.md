## Description:

NASA (nasa.gov). Use this skill for any NASA request involving searching, reading, or retrieving NASA data through the OOMOL NASA connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve NASA data through OOMOL, including Astronomy Picture of the Day metadata, near-Earth object data, DONKI space-weather events, and EPIC imagery metadata.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: NASA-related requests are handled through OOMOL rather than only by NASA.

Mitigation: Use the skill only when routing NASA query payloads through OOMOL is acceptable for the user and organization.

Risk: The artifact documents one-line installer commands that execute network-fetched scripts.

Mitigation: Prefer a verifiable installation method and review installer contents before execution.

Risk: Connector payloads can be malformed or out of date if the live action contract is skipped.

Mitigation: Inspect the live action schema before constructing each connector payload.

## Reference(s):

- [ClawHub NASA skill page](https://clawhub.ai/oomol/skills/oo-nasa)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [NASA homepage](https://www.nasa.gov)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before running connector actions; responses include data and execution metadata.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
