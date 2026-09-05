## Description:

Google Tag Manager API integration with managed OAuth for managing GTM accounts, containers, workspaces, tags, triggers, variables, environments, container versions, and user permissions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Google Tag Manager resources through Maton-managed OAuth. It supports read/list workflows by default and can help prepare confirmed changes such as creating tags, updating triggers, publishing container versions, configuring environments, or managing user permissions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on Google Tag Manager resources through Maton-managed OAuth or API access.

Mitigation: Install it only for intended GTM administration, review connection scope, and prefer OAuth with read-only access where possible.

Risk: Write actions can change tags, triggers, workspaces, containers, environments, versions, or user permissions.

Mitigation: Require explicit user confirmation before POST, PUT, PATCH, or DELETE operations, including the target resource, payload, and intended effect.

Risk: Publishing a container version makes changes live.

Mitigation: Confirm the exact container and version before publishing and verify identifiers with read/list calls first.

Risk: Changing account or container permissions can grant or revoke user access.

Mitigation: Confirm the affected email address, account or container, and permission level before modifying access.

Risk: Using a Maton API key instead of OAuth exposes a long-lived credential to the local environment.

Mitigation: Prefer OAuth, avoid printing or persisting API keys, and rotate any key that was exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/google-tag-manager-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Tag Manager API overview](https://developers.google.com/tag-platform/tag-manager/api/v2)
- [Google Tag Manager API reference](https://developers.google.com/tag-platform/tag-manager/api/reference/rest)
- [Google Tag Manager concepts](https://developers.google.com/tag-platform/tag-manager/api/v2/devguide)
- [Related API Gateway skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline bash, JSON, Python, and JavaScript examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and Google Tag Manager authorization.]

## Skill Version(s):

1.2.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
