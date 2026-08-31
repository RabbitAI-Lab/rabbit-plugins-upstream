## Description:

Zoom Admin API integration with managed OAuth for managing users, meetings, webinars, recordings, and account settings with admin-level access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, IT administrators, and operators use this skill to administer an authorized Zoom workspace through Maton's OAuth-backed gateway. It supports read/list workflows and, with explicit user confirmation, write operations such as creating, updating, or deleting Zoom resources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can administer users, meetings, webinars, recordings, and account settings in the authorized Zoom account.

Mitigation: Install it only for intended Zoom administration, connect only the intended account, and review every write, delete, scheduling, access, or recording action before approval.

Risk: Multiple Maton or Zoom connections can make the target account ambiguous.

Mitigation: Specify the intended connection when more than one account is available and verify account context before modifying resources.

Risk: Long-lived API keys and provider-issued tokens can leak if surfaced in prompts, logs, files, or shell history.

Mitigation: Use OAuth where possible, rely on the CLI credential store, and avoid printing, logging, exporting, or persisting credentials.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/byungkyu/skills/zoom-admin-api)
- [Publisher Profile](https://clawhub.ai/user/byungkyu)
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

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, API calls, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, Maton authentication, and a user-authorized Zoom connection.]

## Skill Version(s):

1.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
