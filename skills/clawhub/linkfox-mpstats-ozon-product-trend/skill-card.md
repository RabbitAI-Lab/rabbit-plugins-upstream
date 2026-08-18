## Description:

Returns daily time-series metrics for a single Ozon Russia SKU, including sales, price, stock, rating, and optional search visibility signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, marketplace analysts, and agent developers use this skill to inspect one Ozon SKU's day-by-day sales, price, stock, rating, and visibility patterns. It supports trend validation, seasonality checks, and factual anomaly review without providing buying advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a LinkFox API key and contacts LinkFox network services, with environment variables that can change service endpoints.

Mitigation: Install only if comfortable sharing requests with LinkFox services, keep the API key scoped to the intended account, and avoid custom endpoint environment variables unless the destination is controlled and trusted.

Risk: The bundled onboarding flow can guide phone/SMS login, generate API keys, list paid plans, and create payment orders after a plan and payment method are selected.

Mitigation: Prefer self-service account setup on the official LinkFox site when possible, and verify the selected plan, payment method, and order details before approving any payment action.

Risk: The skill writes complete marketplace responses and cache data to local storage, which may include commercially sensitive product research.

Mitigation: Run the skill in an appropriate workspace, avoid using sensitive SKU research where local persistence is unacceptable, and review or delete generated linkfox output files when no longer needed.

Risk: The skill can report feedback to LinkFox when results or user reactions indicate an issue or improvement.

Mitigation: Review feedback content for sensitive business details before allowing outbound feedback reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-trend)
- [LinkFox publisher profile](https://clawhub.ai/user/linkfox-ai)
- [MPSTATS Ozon product trend API reference](references/api.md)
- [Authentication and billing onboarding](references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, JSON files, guidance]

**Output Format:** [Markdown guidance with JSON API responses, saved JSON data files, tables, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Full marketplace responses are saved under a local linkfox session directory; small responses are also printed to stdout, while larger responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
