## Description:

mubu-integration helps agents manage Mubu outlines for Obsidian-style workflows by importing and exporting Markdown, querying notes, and creating, moving, renaming, saving, or deleting Mubu documents and folders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[liuboacean](https://clawhub.ai/user/liuboacean)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users who keep outlines in Mubu or Obsidian use this skill to automate Mubu document management, Markdown round-tripping, and OPML or FreeMind exports through a Python CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate with the user's Mubu account and create, update, move, rename, export, or purge content when commanded.

Mitigation: Review the skill before installing, use precise prompts, and require explicit confirmation before account-changing or destructive actions.

Risk: The server security summary says the documentation understates and misstates account-changing and local-file-writing powers.

Mitigation: Treat Mubu writes and local export, cache, or trash file changes as expected capabilities; inspect planned commands and choose export paths carefully.

Risk: Cached access can remain available through the local Mubu token file.

Mitigation: Clear ~/.mubu_token manually when cached access should be revoked.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/liuboacean/skills/mubu-integration)
- [Artifact README](README.md)
- [Artifact skill instructions](SKILL.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, OPML or FreeMind XML, shell commands, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may describe or trigger remote Mubu account actions and local cache, trash, or export file changes when the skill is executed with user credentials.]

## Skill Version(s):

1.3.11 (source: server release evidence and artifact package version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
