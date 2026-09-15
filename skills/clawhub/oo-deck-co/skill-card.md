## Description:

Deck.co lets agents read, create, and update Deck.co data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Deck.co sources and agents from an OOMOL-connected account, including listing and retrieving records, creating website sources, and checking API key authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may direct users to run remote installer scripts for the oo CLI.

Mitigation: Review the OOMOL CLI installation path before installing, prefer official versioned or checksum-verified installers, and avoid running one-line remote scripts from an elevated shell.

Risk: Deck.co write actions can change account state when run with a payload.

Mitigation: Fetch the live action schema and confirm the exact payload and effect with the user before running write actions.

## Reference(s):

- [ClawHub Deck.co skill page](https://clawhub.ai/oomol/skills/oo-deck-co)
- [Deck.co homepage](https://www.deck.co)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Deck.co actions require payload confirmation; first-time setup should be used only after authentication or connection failures.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
