## Description:

This skill supports searching and reading Granola meetings, notes, folders, summaries, and eligible transcripts through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve Granola meeting data, notes, summaries, folders, and transcripts from an OOMOL-connected Granola account. It is suited for read-oriented workflows that need current Granola context without direct API integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands for the oo CLI that could be unsafe if run automatically or from an unverified source.

Mitigation: Require human review before installation and use verified official instructions or a trusted package source for the oo CLI.

Risk: The skill handles Granola meeting, note, and transcript data through OOMOL as an intermediary.

Mitigation: Use only when the user accepts OOMOL-mediated Granola access and review authentication, connection, and billing prompts before proceeding.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-granola)
- [Granola Homepage](https://www.granola.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read actions return Granola connector data with execution metadata; transcripts may require an eligible paid Granola plan.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
