## Description:

Use AdaptlyPost to manage social posts, connected accounts, analytics, and inbox activity across 14 platforms, with user confirmation for public or destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tarasshyn](https://clawhub.ai/user/tarasshyn)

### License/Terms of Use:

MIT-0

## Use Case:

External users with AdaptlyPost accounts can draft, schedule, publish, and review social content and manage related account activity through AdaptlyPost. Each public post and sensitive inbox or account change requires explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports partial scan coverage and flags a LinkedIn organization lookup outside the declared scope.

Mitigation: Review the requested operation and documented scope before use; confirm each public post and sensitive inbox or account change, and use a dedicated revocable API token with only the permissions needed.

## Reference(s):

- [AdaptlyPost API reference](references/api-reference.md)
- [Platform-specific configuration reference](references/platform-configs.md)
- [AdaptlyPost](https://adaptlypost.com)
- [AdaptlyPost release on ClawHub](https://clawhub.ai/tarasshyn/skills/adaptlypost)

## Skill Output:

**Output Type(s):** [Text, API Calls, Guidance]

**Output Format:** [Natural-language responses with structured API data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include post drafts, account and analytics data, and inbox content.]

## Skill Version(s):

1.31.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
