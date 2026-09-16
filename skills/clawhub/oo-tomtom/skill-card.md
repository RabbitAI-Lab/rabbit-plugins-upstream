## Description:

TomTom (developer.tomtom.com). Use this skill for ANY TomTom request: searching and reading data through the TomTom connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use this skill to retrieve TomTom location data, including autocomplete, place search, geocoding, nearby points of interest, and reverse geocoding through an OOMOL-connected TomTom account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup suggests piping a remote installer directly into a shell.

Mitigation: Use an official, versioned, verifiable oo CLI installation path before authenticating or connecting TomTom.

Risk: The skill relies on OOMOL as the TomTom credential broker.

Mitigation: Deploy only where use of OOMOL-managed TomTom credentials is acceptable and verify account connection status before running actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-tomtom)
- [TomTom Developer](https://developer.tomtom.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action results are returned by the oo CLI as JSON; the skill tells the agent to inspect live connector schemas before constructing payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
