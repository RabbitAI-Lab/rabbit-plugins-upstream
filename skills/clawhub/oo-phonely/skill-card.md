## Description:

Phonely lets agents read Phonely agents, calls, summaries, and transcripts through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect connected Phonely data, including accessible agents, call lists, call summaries, and transcripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can expose call transcripts and summaries from a connected Phonely account.

Mitigation: Install and use it only where transcript access is intended, and review transcript privacy expectations before use.

Risk: First-time setup may require installing and signing in to the oo CLI.

Mitigation: Install the CLI and authenticate only when setup or command failures require it, then rerun the intended read action.

## Reference(s):

- [Phonely homepage](https://www.phonely.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-phonely)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-oriented connector guidance; command responses are JSON from the oo CLI.]

## Skill Version(s):

1.0.0 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
