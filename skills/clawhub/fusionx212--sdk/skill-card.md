## Description:

fetch-price lets agents search live UK marketplace listings for physical products and return normalized GBP price, condition, marketplace, and direct purchase URL data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fusionx212](https://clawhub.ai/user/fusionx212)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill when a user wants to find, compare, price-check, or buy a physical product available in the UK. It is suited for live marketplace lookup with budgets or availability constraints, not digital goods, services, non-UK marketplaces, or historical price research.

### Deployment Geography for Use:

United Kingdom

## Known Risks and Mitigations:

Risk: Returned purchase URLs may include affiliate tracking that is not clearly disclosed in the main skill listing.

Mitigation: Disclose monetized links to users and review returned URLs before presenting them in policy-sensitive or regulated contexts.

Risk: User product queries are sent to fetch-price.com.

Mitigation: Avoid sending personal, confidential, or sensitive details in product queries.

Risk: Install dependencies are not pinned.

Mitigation: Install in a separate environment and review dependency versions before production use.

Risk: FETCH_PRICE_API_KEY is used for authenticated API access.

Mitigation: Keep the API key private and provide it through environment variables or managed secret storage.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/fusionx212/skills/sdk)
- [fetch-price MCP documentation](https://fetch-price.com/docs/mcp)
- [fetch-price pricing](https://fetch-price.com/pricing)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Normalized JSON product listing data with product, price, currency, condition, marketplace, URL, and optional metadata fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are live marketplace data; purchase URLs should be presented unchanged and may include affiliate tracking.]

## Skill Version(s):

1.0.0 (source: server release metadata, pyproject.toml, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
