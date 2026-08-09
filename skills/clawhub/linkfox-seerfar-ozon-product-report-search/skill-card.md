## Description:

Screens the Seerfar Ozon product database by sales, revenue, price, conversion, rating, brand, seller, fulfillment, and related metrics, returning product-level report rows for product selection and competitive analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to screen Ozon products by performance, pricing, conversion, logistics, listing-age, brand, and seller metrics. It supports product selection, competitor product analysis, best-seller discovery, and SKU-level product report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses LinkFox credentials and may help create or retrieve API keys.

Mitigation: Use dedicated credentials where possible, avoid exposing API keys in shared logs or prompts, and rotate keys if they may have been disclosed.

Risk: The skill can guide paid credit purchases and payment QR generation.

Mitigation: Confirm the user's intent and expected credit cost before purchase or repeated API use.

Risk: Full product-report responses may contain business-sensitive data and are saved locally.

Mitigation: Treat stdout and local linkfox data directories as sensitive, and delete cached response files when reports are no longer needed.

Risk: Environment URL overrides can change the service endpoints used by the scripts.

Mitigation: Use the default service URLs in normal use and review any override variables before execution.

## Reference(s):

- [Seerfar Ozon Product Report Search API Reference](artifact/references/api.md)
- [Authentication and Credits Onboarding](artifact/references/onboarding.md)
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-product-report-search)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and persisted JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full API responses are saved under local linkfox session data paths; large responses print summaries unless inline output is requested.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
