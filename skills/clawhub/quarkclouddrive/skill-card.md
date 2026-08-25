## Description:

quarkclouddrive helps agents operate Quark Drive files through a Node-based CLI, including upload, download, sharing, save-as, search, photo organization, and file summary or question answering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[quarkdrive](https://clawhub.ai/user/quarkdrive)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to authenticate with Quark Drive and manage cloud-drive files, links, media organization, and document understanding tasks from chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify a user's Quark Drive files after authorization.

Mitigation: Install and authorize only for accounts where the user is comfortable allowing upload, read, share, move, copy, organize, and analysis operations.

Risk: The installer uses a remote update and download path.

Mitigation: Review the publisher, release metadata, and security verdict before installing or updating.

Risk: The skill requires raw prompt text and a session identifier for service-quality tracking.

Mitigation: Avoid using the skill with prompts containing sensitive information unless that telemetry behavior is acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/quarkdrive/skills/quarkclouddrive)
- [Publisher profile](https://clawhub.ai/user/quarkdrive)
- [Quark Drive](https://pan.quark.cn)
- [Authorization and account management](references/auth.md)
- [File operations](references/file-ops.md)
- [File search](references/file-search.md)
- [File upload](references/file-upload.md)
- [File sharing](references/file-share.md)
- [Save shared links](references/file-saveas.md)
- [Photo organization](references/file-organize.md)
- [Assistant capabilities](references/assistant.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with shell command guidance and NDJSON-derived results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and an authorized Quark Drive account for account-scoped operations.]

## Skill Version(s):

1.0.14 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
