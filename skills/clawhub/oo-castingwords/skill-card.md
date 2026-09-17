## Description:

CastingWords helps agents operate CastingWords through the OOMOL oo CLI for account balance checks, transcript retrieval, transcription status lookups, and transcription submissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to handle CastingWords account and transcription workflows through an OOMOL-connected account, including checking balances, retrieving transcripts, checking job status, and submitting public media URLs for human transcription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask users to execute remote installer scripts without integrity verification.

Mitigation: Review the installer path before installing and prefer an official package manager, a pinned release, or a downloaded installer with checksum or signature verification.

Risk: Submitting a transcription changes CastingWords account state.

Mitigation: Confirm the exact transcription submission payload and expected account impact before running write actions.

## Reference(s):

- [CastingWords homepage](https://castingwords.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub CastingWords skill page](https://clawhub.ai/oomol/skills/oo-castingwords)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action-schema inspection before constructing connector payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
