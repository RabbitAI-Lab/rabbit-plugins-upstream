## Description:

Helps agents use LinkFox's gateway to work with Temu Partner EU promotion APIs for activity lookup, candidate goods lookup, goods enrollment, enrollment status checks, enrolled goods queries, and promotion goods updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and agent developers use this skill to query Temu EU promotion activities and manage promotion enrollment workflows through LinkFox scripts and gateway calls. It is intended for commercial ClawHub use where the user already trusts LinkFox with the required account and Temu seller credentials.

### Deployment Geography for Use:

Europe (Temu Partner EU)

## Known Risks and Mitigations:

Risk: The skill requires LinkFox account keys and Temu seller access tokens, and can store Temu tokens locally.

Mitigation: Install only when LinkFox is trusted with these credentials, avoid passing tokens in shared command lines or transcripts, and review local credential files after use.

Risk: The skill includes broad proxy and file-download helpers in addition to dedicated promotion scripts.

Mitigation: Prefer the dedicated promotion scripts for normal workflows and review arbitrary proxy or download requests before execution.

Risk: The bundled onboarding and payment-order flow can involve account setup, billing, and payment actions.

Mitigation: Use onboarding only when authentication or billing errors require it, and require user confirmation before initiating payment-related commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-promotion-eu)
- [API reference](references/api.md)
- [Temu access token authorization](references/access-token.md)
- [Partner EU promotion catalog](references/partner-eu-catalog.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [Promotion API documentation index](references/apis/README.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API request or response data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts write full gateway responses to local JSON files and print either full JSON or summaries depending on response size.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
