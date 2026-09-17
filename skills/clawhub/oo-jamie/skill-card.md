## Description:

Jamie lets an agent search and read Jamie meetings, transcripts, summaries, tasks, and tags through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Jamie meeting details, list or search meetings, and read Jamie tags and action items through the OOMOL `oo` CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote shell installer commands for the oo CLI.

Mitigation: Use a reviewed, versioned, or checksum-verified oo CLI installation method before running Jamie connector actions.

Risk: Jamie data is accessed through OOMOL as an intermediary.

Mitigation: Install and use the skill only when the user is comfortable with OOMOL handling the connected Jamie data.

## Reference(s):

- [Jamie skill page](https://clawhub.ai/oomol/skills/oo-jamie)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Jamie homepage](https://www.meetjamie.ai)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Markdown, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides read-only Jamie connector actions and first-time setup fallback steps.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
