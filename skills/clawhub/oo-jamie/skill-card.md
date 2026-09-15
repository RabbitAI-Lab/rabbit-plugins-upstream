## Description:

Jamie connector for searching and reading meeting data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Jamie meeting records, including meeting details, summaries, transcripts, tasks, tags, and search results through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup flow includes remote installer commands that could run arbitrary code if executed without review.

Mitigation: Review the oo CLI installation process separately before installation and avoid piping remote installer scripts directly into a shell.

Risk: Jamie meeting details may include sensitive transcript, task, tag, and summary content.

Mitigation: Use the skill only for explicit Jamie requests and treat returned meeting records as sensitive user or workspace data.

## Reference(s):

- [Jamie homepage](https://www.meetjamie.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-jamie)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Jamie meeting details that include summaries, transcripts, tasks, and tags.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
