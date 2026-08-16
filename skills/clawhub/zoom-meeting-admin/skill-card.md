## Description:

Manage Zoom meetings, cloud recordings, and account users via a Server-to-Server OAuth REST script.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage scheduled Zoom meetings, inspect meeting details, create recurring meetings, delete meetings after confirmation, query cloud recordings, and look up account users through a constrained Server-to-Server OAuth workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses account-level Zoom Server-to-Server OAuth credentials and caches an access token locally.

Mitigation: Use a dedicated least-privilege Zoom app, keep .env and token cache files chmod 600, and keep credentials out of prompts, logs, repositories, and shared environments.

Risk: Meeting creation and deletion can change live Zoom account state.

Mitigation: Require a separate human confirmation before creating or deleting meetings, and enable delete and recording scopes only when they are needed.

Risk: Evidence reports mismatches around API scope and meeting-creation confirmation.

Mitigation: Review or fix the api_call documentation and create_meeting confirmation mismatch before relying on this skill in a shared agent environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mebusw/skills/zoom-meeting-admin)
- [Server-resolved GitHub provenance](https://github.com/mebusw/zoom-meeting-admin)
- [Zoom Marketplace](https://marketplace.zoom.us/)
- [README.md](artifact/README.md)
- [README.zh-cn.md](artifact/README.zh-cn.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses from the Zoom helper script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.7+, network access to zoom.us and api.zoom.us, and local Zoom Server-to-Server OAuth credentials.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
