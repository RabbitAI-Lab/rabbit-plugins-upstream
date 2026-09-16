## Description:

OpenAlex connector skill for searching and reading OpenAlex works and entities through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve OpenAlex works and entities, get autocomplete suggestions, and run search, filter, pagination, or grouping queries through an OOMOL-connected OpenAlex account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified remote installer commands that can execute changing network code on a user's machine.

Mitigation: Install the oo CLI only from a trusted OOMOL delivery path, prefer a signed, versioned, or checksum-verified source, and avoid administrator or root privileges.

## Reference(s):

- [OpenAlex homepage](https://openalex.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-openalex)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live OpenAlex connector schemas before constructing request payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
