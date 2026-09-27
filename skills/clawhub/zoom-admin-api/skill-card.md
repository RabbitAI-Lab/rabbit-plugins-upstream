## Description:

Zoom Admin API integration with managed OAuth for managing users, meetings, webinars, recordings, and account settings with admin-level access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and operations teams use this skill to perform approved Zoom Admin API tasks through Maton-managed OAuth, including listing users, managing meetings or webinars, reviewing recordings, and checking account or user settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Admin-level Zoom access can affect account-wide users, meetings, webinars, recordings, and settings.

Mitigation: Use this skill only for tasks that truly require Zoom Admin access, prefer narrower Zoom integrations for personal meeting tasks, and confirm every write, deletion, or authorization change before execution.

Risk: Functions, triggers, and destinations can run or forward data continuously until removed.

Mitigation: Review each function, trigger, and destination before enabling it, require explicit approval, use least-privilege connections, and remove automation when it is no longer needed.

Risk: OAuth or API-key credentials could be exposed through improper handling.

Mitigation: Prefer Maton OAuth, do not print or persist credentials, avoid raw API-key workflows unless the CLI cannot be installed, and rotate any credential that was exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoom-admin-api)
- [Maton Homepage](https://maton.ai)
- [Maton Docs](https://docs.maton.ai)
- [Maton API Reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [Zoom API Overview](https://developers.zoom.us/docs/api/)
- [Zoom Meeting API Reference](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/)
- [Zoom User API Reference](https://developers.zoom.us/docs/api/rest/reference/user/methods/)
- [Zoom Account API Reference](https://developers.zoom.us/docs/api/rest/reference/account/methods/)
- [Zoom Rate Limits](https://developers.zoom.us/docs/api/rate-limits/)
- [Related API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user-approved Zoom OAuth authorization.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
