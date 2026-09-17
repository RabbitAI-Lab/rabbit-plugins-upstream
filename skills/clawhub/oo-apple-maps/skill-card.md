## Description:

Operate Apple Maps through OOMOL's oo CLI to search places, geocode addresses, retrieve place details, get directions, estimate travel times, and work with related map data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to route Apple Maps tasks through an OOMOL-connected account, including place search, autocomplete, geocoding, reverse geocoding, place lookup, directions, and ETA requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path includes one-line remote installer commands that execute content fetched from OOMOL URLs directly in a shell.

Mitigation: Install the oo CLI through a pinned, inspectable, or signed distribution path when available, or independently review and trust the installer source before execution.

## Reference(s):

- [ClawHub Apple Maps Skill](https://clawhub.ai/oomol/skills/oo-apple-maps)
- [Apple Maps for Developers](https://developer.apple.com/maps/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides the agent to inspect live connector schemas before submitting Apple Maps action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
