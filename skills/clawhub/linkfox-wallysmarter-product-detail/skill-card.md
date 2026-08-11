## Description:

Retrieves Walmart product details through WallySmarter, including current product attributes, price history, and sales trend data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, analysts, and developers use this skill to look up a single Walmart product by ItemId and review current attributes, price history, and estimated sales trends. It can also guide LinkFox API key setup and paid credit workflows when authentication or billing blocks product lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a paid LinkFox/WallySmarter API workflow and can guide account login, API-key generation, billing order creation, and payment QR handling.

Mitigation: Install and run it only when the user expects a paid LinkFox workflow; prefer self-service signup and payment, and review any generated order or payment details before proceeding.

Risk: Custom LinkFox gateway or account API environment variables can redirect requests to endpoints chosen by the local environment.

Mitigation: Use default LinkFox endpoints unless the custom endpoint is trusted, and review environment variables before sending API keys or product queries.

Risk: Product responses, cache files, API setup details, payment QR files, and feedback content may be stored locally or sent to LinkFox services.

Mitigation: Avoid submitting sensitive product or account information unless necessary, and review or clear local LinkFox data and cache paths when the session is complete.

Risk: The security scan verdict is suspicious because the advertised lookup behavior is bundled with account, billing, feedback, and local storage behaviors.

Mitigation: Review the skill behavior before deployment and restrict use to environments where LinkFox account, billing, and feedback workflows are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-wallysmarter-product-detail)
- [WallySmarter API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration guidance]

**Output Format:** [Markdown guidance with JSON API responses and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The product lookup script writes full API responses to local LinkFox data and cache paths; large responses are summarized in stdout.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
