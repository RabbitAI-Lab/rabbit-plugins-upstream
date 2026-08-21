## Description:

Manage Zoom meetings, cloud recordings, and account users through a fixed-whitelist Server-to-Server OAuth CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mebusw](https://clawhub.ai/user/mebusw)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, operators, and developers use this skill to list, inspect, create, and delete Zoom meetings, query cloud recordings, and look up account users from an agent while staying within a fixed action set.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zoom Server-to-Server OAuth credentials can grant account-level access to meeting metadata, cloud recordings, and deletion actions.

Mitigation: Use a dedicated Zoom app with minimum required scopes, keep .env and ~/.zoom-s2s-token.json private, and avoid enabling delete or recording scopes unless they are needed.

Risk: Deleting a meeting is destructive.

Mitigation: Show the meeting details to the user and obtain explicit confirmation before running delete_meeting with the required --yes flag.

Risk: Bypassing the documented CLI whitelist could expand access beyond the skill's intended Zoom operations.

Mitigation: Invoke only the documented CLI actions and do not modify the script, import internal functions, or construct arbitrary Zoom API requests with the same credentials.

## Reference(s):

- [Server-resolved source repository](https://github.com/mebusw/zoom-meeting-admin)
- [ClawHub skill page](https://clawhub.ai/mebusw/skills/zoom-meeting-admin)
- [Zoom Marketplace](https://marketplace.zoom.us/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill invokes a Python CLI that prints JSON responses from whitelisted Zoom API actions.]

## Skill Version(s):

1.0.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
