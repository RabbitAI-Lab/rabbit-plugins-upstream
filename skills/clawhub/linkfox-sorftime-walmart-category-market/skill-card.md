## Description:

Uses Sorftime data to retrieve the Walmart US category tree, match natural-language category names to NodeIds, and inspect category market reports and Best Seller Top 80 results for known NodePaths.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace researchers, ecommerce operators, and agents use this skill to find Walmart US category nodes, resolve category names to related NodeIds, and summarize category-level market data before deeper product or keyword research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid LinkFox integration that can consume account credits.

Mitigation: Confirm the selected operation and expected request cost before running additional paid calls.

Risk: Onboarding and billing commands can handle API keys, phone/SMS login, and payment-order creation.

Mitigation: Prefer self-service API-key setup, keep LINKFOX endpoint variables trusted, and run billing commands only when intentionally managing payment or account access.

Risk: The skill saves complete API responses locally, which may include commercially sensitive research data.

Mitigation: Review saved files under the workspace linkfox directory and avoid inline output for large or sensitive responses unless needed.

Risk: Automatic feedback reporting can send issue or improvement context to LinkFox.

Mitigation: Do not include secrets or sensitive research details in feedback content.

## Reference(s):

- [Walmart category market API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-walmart-category-market)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and saved JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are saved as JSON files and summarized in stdout unless inline output is explicitly requested.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
