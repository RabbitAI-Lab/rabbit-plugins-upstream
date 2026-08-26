## Description:

Enables an agent to operate Reddit through an OOMOL-connected account for reading, searching, posting, commenting, editing, and deleting authenticated Reddit content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fulfill Reddit tasks through an authenticated OOMOL connector, including reading posts and comments, searching Reddit, creating posts or comments, editing text content, and deleting authenticated content after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a connected Reddit account to post, comment, edit, or delete content.

Mitigation: Review the exact payload and expected effect before approving write actions, and require explicit approval before destructive deletion.

Risk: Installing or using the skill grants an agent access to Reddit through the user's OOMOL-connected account.

Mitigation: Install and connect Reddit only when that account access is intended, and use the setup flow only after an auth or connection error.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-reddit)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Reddit homepage](https://www.reddit.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; state-changing actions require user confirmation.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
