## Description:

Operate Reddit through an OOMOL-connected account for reading posts and profiles, creating or editing posts and comments, and deleting authenticated-user content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to perform authenticated Reddit workflows through OOMOL, including profile lookup, subreddit listing, post search, comment retrieval, posting, replying, editing, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can post, edit, or delete Reddit content using the authenticated account.

Mitigation: Confirm the exact action, target, payload, and expected effect before running any write or destructive action.

Risk: First-time setup instructions include direct execution of remote installer scripts.

Mitigation: Use a verified, versioned installer when available, or inspect and validate the installer before execution.

## Reference(s):

- [ClawHub Reddit skill page](https://clawhub.ai/oomol/skills/oo-reddit)
- [Reddit homepage](https://www.reddit.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Reddit connector schemas before execution; read actions can return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
