## Description:

Helps agents generate Amazon Ads authorization URLs, list authorized advertising profiles, check token status, and refresh Amazon Ads access tokens through LinkFox APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, agencies, and advertising operators use this skill to connect Amazon Ads accounts to LinkFox workflows, discover marketplace profiles, and keep authorization status current for downstream advertising skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon Ads authorization data and requires a LinkFox API key.

Mitigation: Install only when LinkFox is trusted for this data, and keep LINKFOX_TOOL_GATEWAY, AMAZON_ADS_BASE_URL, and related endpoint variables pointed at trusted LinkFox hosts.

Risk: Authorization and token-related responses can be written to local LinkFox output or cache files, and inline output may expose sensitive values.

Mitigation: Avoid --inline and raw curl token examples unless needed, rely on status-only token helpers where possible, and review or delete local LinkFox output/cache files after sensitive authorization work.

Risk: The bundled onboarding flow includes SMS login and payment or order commands.

Mitigation: Treat onboarding and billing commands as optional, user-initiated account setup steps rather than routine Amazon Ads authorization operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-ads-auth)
- [API reference](references/api.md)
- [Onboarding and billing guide](references/onboarding.md)
- [Amazon Ads console](https://advertising.amazon.com/)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write complete responses to local LinkFox session files and summarize large responses on stdout; token-status helpers remove raw access and refresh tokens from displayed output.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
