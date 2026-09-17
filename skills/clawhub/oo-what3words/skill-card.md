## Description:

Operates what3words through an OOMOL-connected account for searching, reading, and converting what3words location data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to work with what3words data through OOMOL, including address suggestions, coordinate conversion, language lookup, and grid section retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup guidance includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review the installer step before use; prefer a verified, versioned installer source or inspect the installer manually before running it.

Risk: what3words queries and location-related data are sent through OOMOL-connected services.

Mitigation: Confirm that routing this location data through OOMOL is acceptable for the intended use case before submitting sensitive coordinates or addresses.

## Reference(s):

- [what3words homepage](https://what3words.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include connector command results returned as JSON with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
