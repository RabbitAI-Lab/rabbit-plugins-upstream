## Description:

Searches the MPSTATS Ozon Russia database by Russian keyword or SKU and returns product identity details such as product ID, title, brand, seller, image URL, and product URL.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External e-commerce operators, market researchers, and developers use this skill to identify Ozon Russia products from Russian keywords or SKU lists. It is intended as an entry point before detail, brand, category, seller, or trend drill-down skills are used for business metrics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can handle LinkFox account setup, phone/SMS login, and API-key generation.

Mitigation: Run onboarding only when the user explicitly chooses that path, use the documented LinkFox endpoints, and avoid exposing the resulting API key in chat, logs, or shared files.

Risk: The onboarding flow can list paid plans, create subscription orders, and generate payment QR codes.

Mitigation: Require explicit user confirmation of plan ID, payment method, and price before creating an order, and do not poll or continue purchase steps unless requested.

Risk: The search script stores full API responses and local cache files under a linkfox workspace/session directory.

Mitigation: Tell users where response files are written, avoid running searches for sensitive queries unless needed, and delete cached or saved response files when they are no longer required.

Risk: The skill may submit feedback automatically when it detects mismatches, dissatisfaction, praise, or improvement opportunities.

Mitigation: Prefer explicit consent before sending feedback and keep feedback content limited to the minimum necessary behavior description.

Risk: The search endpoint consumes LinkFox credits and the skill notes dynamic charging.

Mitigation: Explain the expected credit cost before calls, avoid automatic retry or broad exploratory searches, and ask the user before additional paid searches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-search)
- [MPSTATS Ozon product search API reference](artifact/references/api.md)
- [Authentication and billing onboarding guide](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [JSON API responses, saved JSON files, concise text or Markdown summaries, and shell commands for authentication or billing setup when needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search responses are saved under a local linkfox session data directory; large responses are summarized unless inline output is requested; repeated calls may use a 24-hour local cache.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
