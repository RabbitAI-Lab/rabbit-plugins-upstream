## Description:

Provides agent guidance and Python commands for managing Shopee AMS affiliate marketing campaigns, products, affiliates, commission rates, and performance reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Shopee sellers and store operators use this skill to inspect and manage authorized store affiliate marketing workflows, including Open Campaign product enrollment, Targeted Campaign setup, affiliate lists, commission rates, and performance reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform live Shopee AMS campaign changes, including bulk product changes and campaign termination.

Mitigation: Use it only in trusted workspaces and require manual confirmation before executing bulk add/remove, campaign update, or termination commands.

Risk: Saved responses and stdout may contain API keys, shop performance data, campaign data, or other sensitive store information.

Mitigation: Treat generated linkfox data files and terminal output as sensitive, restrict workspace access, and clean up retained response files according to the store operator's data policy.

Risk: Configurable credential-bearing endpoints can send credentials or store data to an unintended service if overridden incorrectly.

Mitigation: Avoid endpoint overrides unless the operator controls and trusts the destination endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-ams)
- [Shopee Open Platform AMS documentation](https://open.shopee.com/documents/v2/v2.ams.get_open_campaign_added_product?module=127&type=1)
- [API reference](artifact/references/api.md)
- [Onboarding reference](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with Python command examples and JSON API responses saved to local files or printed to stdout.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts persist full responses under ./linkfox/<date>/<session>/data and may summarize large responses unless --inline is used.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
