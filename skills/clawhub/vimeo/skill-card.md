## Description:

Helps agents access a connected Vimeo account to manage videos, showcases, folders, and related content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Users and developers can use this skill to retrieve and manage videos, showcases, and folders in their connected Vimeo account. With explicit approval, they can also set up scheduled or cross-app actions that operate on Vimeo content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Content changes or deletion may affect the wrong Vimeo resource.

Mitigation: Confirm each write or deletion with the user, including the exact resource ID and intended effect.

Risk: Persistent automations can continue making changes or forwarding event data after setup.

Mitigation: Get explicit approval for each automation and destination; keep destinations on Maton-controlled hosts unless a third-party URL is specifically approved, and remove unused automations.

Risk: A long-lived API key may be exposed when using direct HTTP access.

Mitigation: Prefer OAuth login, avoid displaying or storing API keys, and remove unused connections.

## Reference(s):

- [ClawHub Vimeo skill](https://clawhub.ai/byungkyu/skills/vimeo)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Vimeo API reference](https://developer.vimeo.com/api/reference)
- [Vimeo authentication](https://developer.vimeo.com/api/authentication)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Guidance]

**Output Format:** [Markdown with inline commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include results from the connected Vimeo account.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
