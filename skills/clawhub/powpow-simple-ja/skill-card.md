## Description:

Publishes travel posts and stories to PowPow and creates chat-ready digital humans that can be pinned to PowPow's public map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[durenzidu](https://clawhub.ai/user/durenzidu)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to turn photos, text, or travel memories into PowPow posts and to create digital humans for public map placement. Agents use it to guide login, location resolution, draft composition, image handling, publishing, verification, and cleanup of the user's own test posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use a PowPow account session to publish public posts, upload selected images, expose selected locations on a public map, delete the user's own posts, and spend PowPow badges.

Mitigation: Confirm the exact account, content, images, location, and badge cost before running publishing or digital-human creation commands.

Risk: The skill handles PowPow login credentials and session tokens.

Mitigation: Use a safer first-party or isolated secret-entry flow when available, avoid storing passwords, and keep session state in the configured user state directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/durenzidu/skills/powpow-simple-ja)
- [PowPow homepage](https://global.powpow.online)
- [README](artifact/README.md)
- [Security design and platform API](artifact/references/security.md)
- [File structure](artifact/references/file-structure.md)
- [Product screenshots](artifact/references/screenshots.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, generated post drafts, JSON-like command results, and public PowPow URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 18+, a PowPow account session, and user confirmation before publishing or creating digital humans.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter and config list 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
