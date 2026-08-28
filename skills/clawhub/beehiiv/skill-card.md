## Description:

beehiiv API integration with managed OAuth for managing newsletter publications, subscriptions, posts, custom fields, segments, tiers, and automations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and agents use this skill to manage beehiiv newsletter resources through the Maton CLI or SDK while keeping authentication and account connections user-approved.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can connect to a beehiiv account and perform write or delete actions through the Maton gateway.

Mitigation: Use OAuth, approve the exact account connection and write or delete action, and prefer read-only scopes when possible.

Risk: API-key fallback uses a long-lived Maton credential when the CLI cannot be used.

Mitigation: Prefer OAuth and avoid the API-key fallback unless necessary; never print, persist, or pass the key on a command line.

Risk: Multiple Maton profiles or beehiiv connections can make the target account ambiguous.

Mitigation: Specify the intended profile and connection before acting, especially before POST, PUT, PATCH, or DELETE requests.

## Reference(s):

- [beehiiv Skill on ClawHub](https://clawhub.ai/byungkyu/skills/beehiiv)
- [Maton](https://maton.ai)
- [beehiiv Developer Documentation](https://developers.beehiiv.com/)
- [beehiiv API Reference](https://developers.beehiiv.com/api-reference)
- [Maton Docs](https://docs.maton.ai)
- [Maton CLI Manual](https://cli.maton.ai/manual)
- [API Gateway Skill](https://clawhub.ai/byungkyu/api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Maton CLI, SDK, or raw HTTP examples for beehiiv API operations.]

## Skill Version(s):

1.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
