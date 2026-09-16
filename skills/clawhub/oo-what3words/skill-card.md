## Description:

Provides what3words lookup actions through the OOMOL-connected oo CLI for converting coordinates and three-word addresses, autosuggesting addresses, listing languages, and retrieving grid sections.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run what3words connector actions through OOMOL without handling raw API credentials. It supports address suggestions, coordinate-to-address conversion, address-to-coordinate conversion, supported-language lookup, and grid-section retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Do not allow an agent to run installer commands automatically; install the oo CLI only from a trusted, verified source and review commands before execution.

Risk: what3words query data is routed through OOMOL and the what3words integration.

Mitigation: Use the skill only when the user is comfortable sending the specific lookup data through OOMOL and what3words, and avoid sensitive location queries unless approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-what3words)
- [what3words homepage](https://what3words.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect action schemas before constructing JSON payloads; normal actions are read-oriented lookup operations.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
