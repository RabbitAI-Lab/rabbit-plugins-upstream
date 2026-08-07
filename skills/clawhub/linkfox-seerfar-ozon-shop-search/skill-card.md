## Description:

Searches a specified Ozon seller's Seerfar product catalog and returns 30-day sales, price, rating, fulfillment, seller type, return/cancellation rate, and total shop sales.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace analysts and ecommerce operators use this skill to inspect one Ozon seller's product catalog, rank products by sales, price, rating, or listing time, and present shop-level sales context. It is intended for product catalog analysis after the user has a Seerfar seller or shop ID.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a LinkFox API key and can send requests through an environment-selected gateway.

Mitigation: Restrict API key scope where possible, review the LINKFOX_TOOL_GATEWAY setting before use, and avoid running the skill in environments where gateway overrides are not allowed.

Risk: The skill can consume paid LinkFox credits for shop-search calls and additional pagination.

Mitigation: Confirm cost-sensitive follow-up calls with the user, keep page size within the documented limit, and rely on the 24-hour cache for repeated identical requests.

Risk: Full Ozon shop-search responses are retained locally in LinkFox data and cache directories.

Mitigation: Treat saved responses as sensitive business data, limit where the skill is run, and periodically delete generated LinkFox session and cache files when retention is not needed.

Risk: Authentication or billing failures may trigger onboarding behavior that references downloading an additional LinkFox onboarding skill.

Mitigation: Review or disable onboarding-download behavior in controlled environments and require user authorization before installing additional skill content.

## Reference(s):

- [Seerfar Ozon shop-search API reference](references/api.md)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-shop-search)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown tables and guidance, shell command examples, stdout JSON or summaries, and saved JSON response files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key; default script behavior caches identical requests for 24 hours and stores full responses under LinkFox session data.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
