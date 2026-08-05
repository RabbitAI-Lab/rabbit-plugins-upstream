## Description:

酷狗 helps agents use Kugou Music to search songs, provide recommendations and charts, manage favorites and playlists, and present playable music links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[shamo88](https://clawhub.ai/user/shamo88)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to let an assistant work with a Kugou Music account for song search, personalized recommendations, charts, favorites, listening history, statistics, and playlist creation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles reusable Kugou account secrets and QR login state.

Mitigation: Prefer QR login when the client can render the QR image, avoid pasting base64 secrets into chats or logs, and treat any provided secret as account access material.

Risk: Installation can write the skill into multiple local agent environments.

Mitigation: Review the installation target before running install commands, and avoid broad install modes unless all target environments are intended.

Risk: Music commands can act on account data such as favorites, recent plays, statistics, and playlists.

Mitigation: Confirm user intent before account-changing actions such as playlist creation, and require reauthentication when login state expires.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/shamo88/skills/kugou-skill)
- [Publisher profile](https://clawhub.ai/user/shamo88)
- [Authentication commands](references/auth.md)
- [Music commands](references/music.md)
- [Output format](references/output-format.md)
- [Installation commands](references/install.md)
- [Update commands](references/update.md)
- [Error handling](references/error-handling.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and user-facing music links; CLI command results are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Music commands require a Kugou login; song lists should include playable Markdown links.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
