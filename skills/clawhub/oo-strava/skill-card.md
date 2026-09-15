## Description:

This skill supports Strava (strava.com) requests, including reading, creating, updating, uploading, favoriting, and exporting Strava data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Strava through the OOMOL oo CLI with server-managed credentials. It supports reading athlete, activity, club, route, segment, equipment, and training data, plus confirmed state-changing operations such as creating activities, updating profile or activity data, uploads, exports, and segment favorites.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute scripts from the network.

Mitigation: Review the oo CLI installation path before use and prefer a signed or version-pinned installer with checksum verification.

Risk: Connected Strava OAuth scopes may permit access or changes beyond the immediate task.

Mitigation: Connect only the Strava scopes needed for the intended workflow and reconnect when scopes are missing or expired.

Risk: Write actions can create, update, upload, favorite, or unfavorite Strava data.

Mitigation: Confirm the exact payload and expected effect with the user before running any write action.

## Reference(s):

- [Strava homepage](https://www.strava.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-strava)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from Strava connector actions.]

## Skill Version(s):

1.0.3 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
