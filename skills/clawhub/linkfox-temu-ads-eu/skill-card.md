## Description:

Temu Europe Ads API helper that routes Partner EU advertising operations through the LinkFox gateway for ad creation, modification, reporting, ROAS prediction, ad detail lookup, eligible goods lookup, and operation logs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to call Temu Partner EU advertising APIs through LinkFox, including campaign creation, budget or ROAS changes, ad reporting, product eligibility checks, and logs. It also guides LinkFox and Temu token setup for authenticated API use.

### Deployment Geography for Use:

Europe (Partner EU)

## Known Risks and Mitigations:

Risk: The skill can create or modify live Temu ads, budgets, and ROAS targets through a broad LinkFox proxy integration.

Mitigation: Use only trusted LinkFox and Temu accounts, and confirm every live ad creation, modification, deletion, or budget change before running scripts.

Risk: The skill handles LinkFox API keys and Temu access tokens, including optional local token storage.

Mitigation: Avoid plaintext token storage on shared machines, keep token files private, and do not print raw tokens into logs or shared transcripts.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox gateway.

Mitigation: Leave endpoint override variables unset unless the operator intentionally controls and trusts the target service.

Risk: The security summary flags broad proxy, response logging, credential storage, and payment or onboarding capabilities for review.

Mitigation: Review the skill before installing when only a narrow Temu EU Ads helper is needed, and limit use to the specific operations required.

## Reference(s):

- [API reference](references/api.md)
- [Temu accessToken authorization and retrieval](references/access-token.md)
- [Partner EU Ads catalog](references/partner-eu-catalog.md)
- [Ads API documentation index](references/apis/README.md)
- [Authorization and billing onboarding](references/onboarding.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses; scripts save full JSON responses to local files and print inline JSON or summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires LinkFox and Temu credentials for live API calls; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
