## Description:

Google Photos lets an agent operate a user's OOMOL-connected Google Photos account for reading, creating, updating, uploading, organizing, and deleting photos and albums through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect Google Photos action schemas and run Google Photos read, write, upload, album, media item, and picker-session workflows through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unverified pipe-to-shell installers for the OOMOL CLI.

Mitigation: Review the install step before use and prefer a verified package manager or manually verified installer.

Risk: The skill can perform Google Photos write and destructive actions.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or destructive actions.

Risk: Connector action schemas may change over time.

Mitigation: Inspect the live action schema before constructing each request payload.

## Reference(s):

- [ClawHub Google Photos skill page](https://clawhub.ai/oomol/skills/oo-googlephotos)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Google Photos homepage](https://www.google.com/photos/about/)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands should inspect the live connector schema before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
