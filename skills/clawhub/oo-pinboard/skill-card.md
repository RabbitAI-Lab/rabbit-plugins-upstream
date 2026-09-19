## Description:

Pinboard (pinboard.in). Use this skill for ANY Pinboard request -- reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Pinboard bookmarks through an OOMOL-connected account, including reading bookmarks and tags, adding or replacing bookmarks, and deleting bookmarks after explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup guidance includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Install the oo CLI only through a trusted, verified, pinned, or package-manager-based method before using the skill.

Risk: Bookmark add, replace, and delete actions can modify or remove Pinboard data.

Mitigation: Confirm the exact URL, payload, and intended effect before any write action, and require explicit approval before destructive deletion.

Risk: The skill relies on OOMOL-connected Pinboard access.

Mitigation: Use it only when the user accepts OOMOL as the access path for Pinboard and has connected the appropriate account.

## Reference(s):

- [Pinboard homepage](https://pinboard.in/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Pinboard app connection](https://console.oomol.com/app-connections?provider=pinboard)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before building action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
