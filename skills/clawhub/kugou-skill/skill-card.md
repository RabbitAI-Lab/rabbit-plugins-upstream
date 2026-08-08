## Description:

酷狗 is a Kugou Music agent skill for searching songs, getting recommendations, viewing charts and listening history, managing favorites, and creating playlists through the kugou-cli command line tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shamo88](https://clawhub.ai/user/shamo88)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to access Kugou Music account features, including song search, personalized recommendations, charts, favorites, recent plays, listening statistics, and user-confirmed playlist creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a user's Kugou account, including music history, favorites, and playlist creation.

Mitigation: Install and use it only when that account access is intended, and confirm before creating playlists or changing account-linked content.

Risk: Base64 login secrets are saved locally and grant account access.

Mitigation: Prefer QR login when possible; if a secret is used, handle it like a password and avoid exposing it in chat logs, shell history, or shared files.

Risk: Installation and update behavior may modify local agent skill directories or install newer npm package code.

Mitigation: Review the package before installation, disable or avoid update checks where appropriate, and require user confirmation before running update or install commands that change local tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/shamo88/skills/kugou-skill)
- [Authentication commands](references/auth.md)
- [Music commands](references/music.md)
- [Install commands](references/install.md)
- [Update commands](references/update.md)
- [Output format](references/output-format.md)
- [Error handling](references/error-handling.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Music results should be presented as Markdown links; CLI command stdout is JSON and errors are emitted to stderr.]

## Skill Version(s):

0.1.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
