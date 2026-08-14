## Description:

Searches and filters Amazon products with Sorftime data across 14 marketplaces, including category, brand, seller, price, sales, ranking, and historical monthly snapshot queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, e-commerce operators, and marketplace analysts use this skill to discover products, compare competitors, analyze category, brand, and seller portfolios, and retrieve Sorftime product search results through LinkFox.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles Amazon query data, session identifiers, API keys, phone/OTP onboarding, and billing flows.

Mitigation: Install only if you trust LinkFox/Sorftime, keep endpoint environment variables pointed at trusted LinkFox hosts, and avoid phone-login or payment commands unless you explicitly intend to use them.

Risk: API keys and full product-search responses may be printed or saved locally.

Mitigation: Treat printed API keys and saved response files as sensitive, restrict access to generated linkfox data directories, and avoid inline output for sensitive or large responses.

Risk: Feedback reporting can send details about skill behavior or user intent.

Mitigation: Review the feedback behavior before deployment and avoid sending sensitive user content in feedback reports.

## Reference(s):

- [Sorftime Product Search API Reference](artifact/references/api.md)
- [Authentication and Billing Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-amazon-product-query)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON API responses, and saved JSON result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Large responses are summarized unless inline output is requested; complete responses are saved under a session-scoped linkfox data directory and repeated queries may use a 24-hour local cache.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
