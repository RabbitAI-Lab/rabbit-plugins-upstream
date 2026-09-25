## Description:

Speak AI connector skill for reading, creating, updating, and analyzing Speak AI workspace data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Speak AI media, transcripts, folders, processing status, and AI-generated insights, and to submit public audio or video URLs for transcription and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires installing and running the oo CLI, including documented pipe-to-shell installer commands.

Mitigation: Install only if OOMOL is trusted, review the installer or use the official install guide, and follow the release security guidance before running setup commands.

Risk: The upload_media action can change Speak AI workspace state by submitting public audio or video URLs for processing.

Mitigation: Confirm the exact payload and expected effect with the user before running write actions.

## Reference(s):

- [Speak AI homepage](https://speakai.co)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
