## Description:

Temu 全球站电商广告 Ads API skill that helps agents call LinkFox-forwarded Partner Global Ads interfaces for campaigns, creatives, bidding, budgets, reports, and related ad operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to manage Temu Global advertising through LinkFox, including ad creation, modification, ROAS prediction, reporting, logs, and account or token setup guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires LinkFox and Temu credentials and may use locally saved Temu access tokens.

Mitigation: Use only with intended LinkFox and Temu accounts, protect LINKFOX_AGENT_API_KEY or LINKFOXAGENT_API_KEY, and protect or delete ~/.linkfox/temu-access-tokens.json when it is no longer needed.

Risk: The generic proxy and ad create or modify scripts can make business-impacting advertising changes, including budget, ROAS, pause, open, and delete actions.

Mitigation: Review the exact API type and JSON payload before execution, and confirm create, pause, delete, budget, and ROAS changes with the account owner.

Risk: Full gateway responses and local LinkFox output files may contain sensitive advertising or business data.

Mitigation: Store outputs in an appropriate workspace, avoid sharing raw response files unnecessarily, and remove local linkfox output files when retention is not required.

Risk: Gateway URL environment variables can redirect calls away from the default LinkFox gateway.

Mitigation: Verify LINKFOX_TOOL_GATEWAY, TEMU_API_BASE_URL, and STORE_API_BASE_URL before running scripts, especially in shared or automated environments.

Risk: Onboarding and billing helpers may guide account registration or payment-plan order creation.

Mitigation: Use billing flows only when remediation is intended, validate plan and payment details, and do not submit orders without user approval.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-ads-global)
- [API reference](artifact/references/api.md)
- [Temu access token authorization](artifact/references/access-token.md)
- [Partner Global Ads catalog](artifact/references/partner-global-catalog.md)
- [Ads API documentation index](artifact/references/apis/README.md)
- [Onboarding and billing guidance](artifact/references/onboarding.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance, shell commands, and JSON API responses saved to local files or printed to stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized unless --inline is used; full responses are written under linkfox/<date>/<session>/data.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
