## Description:

Helps agents manage authorized Shopee store livestream sessions, products, comments, metrics, and image uploads through LinkFox's Shopee Livestream integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, operators, and developers use this skill to create, start, update, monitor, and moderate Shopee livestream sessions for authorized stores.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can manage real Shopee livestream operations for authorized stores.

Mitigation: Install only if that operational scope is acceptable, and review proposed livestream actions before execution.

Risk: The onboarding flow may handle phone/SMS login, API key generation, billing orders, and payment QR codes.

Mitigation: Only provide SMS codes or approve payment and order commands for flows you explicitly initiated, and protect generated API keys.

Risk: Persisted local response files may contain shop or livestream data.

Mitigation: Review or clean the local linkfox response files after use according to the user's data-handling requirements.

## Reference(s):

- [Skill source](artifact/SKILL.md)
- [Shopee Livestream API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [Shopee Open Platform Livestream documentation](https://open.shopee.com/documents/v2/v2.livestream.upload_image?module=125&type=1)
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-livestream)

## Skill Output:

**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance]

**Output Format:** [JSON responses on stdout, persisted JSON response files, and concise Markdown-style operational guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Complete API responses are persisted under a local linkfox data directory; larger responses may be summarized on stdout.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
