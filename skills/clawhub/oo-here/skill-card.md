## Description:

Enables agents to use HERE through an OOMOL-connected account for address autocomplete, place suggestions, place search, geocoding, lookup, and reverse geocoding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this skill to route HERE location-data requests through the oo CLI instead of calling HERE APIs directly. It supports read-oriented mapping and geocoding workflows such as autocomplete, discover, lookup, and reverse geocode.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer scripts that can execute with shell-level authority.

Mitigation: Review and pin the oo CLI installer or inspect the installer before running it, and avoid piping remote scripts directly into an elevated shell.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-here)
- [HERE homepage](https://www.here.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, JSON, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before connector execution; connector responses are JSON.]

## Skill Version(s):

1.0.3 (source: SKILL.md frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
