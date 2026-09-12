## Description:

Google Workspace Admin SDK integration with managed OAuth for reading and managing users, groups, organizational units, roles, and domain settings through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

IT administrators and authorized operators use this skill to inspect and manage Google Workspace directory resources through Maton while requiring explicit approval for write-capable administrative actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Google Workspace administration can change tenant-wide identity and access state, including users, groups, organizational units, roles, and domain settings.

Mitigation: Use a least-privileged Google admin account, restrict OAuth scopes to the current task, default to read/list calls, and require explicit approval showing the exact write target before execution.

Risk: Hosted functions and trigger destinations can establish persistent data flows that continue after setup.

Mitigation: Avoid broad hosted functions or trigger destinations unless the user understands the ongoing flow, approves the exact destination and payload, and keeps the scope narrow.

Risk: Raw HTTP fallback with a Maton API key can expose a long-lived credential if printed, persisted, or sent to the wrong host.

Mitigation: Prefer OAuth through the Maton CLI; when API-key fallback is unavoidable, keep the key in the runtime environment only, never print it, and send it only to api.maton.ai.

Risk: Server-resolved GitHub import provenance is unavailable for this release.

Mitigation: Consider independently verifying Maton package provenance before installation, as recommended by the security guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-workspace-admin)
- [Maton homepage](https://maton.ai)
- [Admin SDK overview](https://developers.google.com/admin-sdk)
- [Directory API users](https://developers.google.com/admin-sdk/directory/reference/rest/v1/users)
- [Directory API groups](https://developers.google.com/admin-sdk/directory/reference/rest/v1/groups)
- [Directory API members](https://developers.google.com/admin-sdk/directory/reference/rest/v1/members)
- [Directory API organizational units](https://developers.google.com/admin-sdk/directory/reference/rest/v1/orgunits)
- [Directory API domains](https://developers.google.com/admin-sdk/directory/reference/rest/v1/domains)
- [Directory API roles](https://developers.google.com/admin-sdk/directory/reference/rest/v1/roles)
- [Admin SDK guides](https://developers.google.com/admin-sdk/directory/v1/guides)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, API paths, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce high-impact administrative API calls that require explicit user approval before execution.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
