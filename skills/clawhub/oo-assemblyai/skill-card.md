## Description:

AssemblyAI (assemblyai.com). Use this skill for ANY AssemblyAI request, including reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate AssemblyAI through an OOMOL-connected account, including creating transcripts from media URLs and retrieving transcript details, paragraphs, or sentences. Users can also list or delete transcripts when the requested action is confirmed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts in a shell.

Mitigation: Install the oo CLI through a verified package or a downloaded installer whose checksum or signature can be validated; avoid running curl|bash or irm|iex from an elevated shell.

Risk: Transcript creation and deletion can change or remove AssemblyAI data.

Mitigation: Confirm the exact payload, target transcript, and expected effect before allowing create_transcript or delete_transcript to run.

## Reference(s):

- [AssemblyAI homepage](https://www.assemblyai.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-assemblyai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce AssemblyAI transcript data returned through the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
