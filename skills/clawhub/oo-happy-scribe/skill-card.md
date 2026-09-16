## Description:

Happy Scribe helps agents read, create, update, and delete Happy Scribe transcriptions, orders, translations, and exports through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Happy Scribe transcription, subtitling, translation, order, and export workflows from an agent session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer pipe commands for the OOMOL CLI.

Mitigation: Use reviewed installation documentation, pinned releases, and checksum or signature verification before installing the CLI.

Risk: Write actions can create orders, exports, translations, or update Happy Scribe data.

Mitigation: Confirm the exact action payload and expected effect with the user before running any write action.

Risk: The delete action removes a Happy Scribe transcription.

Mitigation: Require explicit approval for the specific transcription ID before running destructive actions.

## Reference(s):

- [Happy Scribe homepage](https://www.happyscribe.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions may return JSON data and execution metadata from the connector.]

## Skill Version(s):

1.0.3 (source: evidence release, metadata, and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
