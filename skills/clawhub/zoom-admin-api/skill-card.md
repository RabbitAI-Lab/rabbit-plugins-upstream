## Description:

Zoom Admin API integration with managed OAuth for managing users, meetings, webinars, recordings, and account settings with admin-level access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to administer a Zoom workspace through Maton's OAuth-managed API gateway, including listing users, managing meetings and webinars, viewing recordings, and checking account settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin-level Zoom access can affect users, meetings, webinars, recordings, and account settings.

Mitigation: Use OAuth where possible, select the narrowest available Zoom scopes, default to read/list calls, and confirm every write, delete, or connection creation action with the user.

Risk: Using a Maton API key can expose a long-lived credential if it is printed, logged, persisted, or passed on a command line.

Mitigation: Prefer Maton OAuth login and the CLI credential store; use raw HTTP only when the CLI is unavailable, feed credentials through stdin, and rotate any key that was exposed.

Risk: Multiple Maton profiles or Zoom connections can cause actions to target the wrong account.

Mitigation: Specify the intended Maton profile and Zoom connection when more than one exists, and revoke unused connections when finished.

## Reference(s):

- [Zoom Admin Skill Page](https://clawhub.ai/byungkyu/skills/zoom-admin-api)
- [byungkyu ClawHub Profile](https://clawhub.ai/user/byungkyu)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoom API Overview](https://developers.zoom.us/docs/api/)
- [Zoom Meeting API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom User API Reference](https://developers.zoom.us/docs/api/rest/reference/user/methods/)
- [Zoom Account API Reference](https://developers.zoom.us/docs/api/rest/reference/account/methods/)
- [Zoom Rate Limits](https://developers.zoom.us/docs/api/rate-limits/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, configuration]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, valid authentication, and an authorized Zoom Admin connection.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
