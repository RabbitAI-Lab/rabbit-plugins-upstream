## Description:

Temu 全球站（非 US/EU）价格/供货价 API，经 LinkFox 网关转发 5 个接口（定价单、推荐价、SKU 供货价列表、批量改价等），默认 site=global。

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External Temu sellers and agents use this skill to query and update Global-region product supply prices through LinkFox's Temu gateway. It helps inspect pricing orders, recommended prices, SKU supply prices, base price recommendations, and batch SKU price changes for semi-managed Temu stores.

### Deployment Geography for Use:

Global, excluding the US and EU Temu site flows described as separate skills

## Known Risks and Mitigations:

Risk: The skill can handle LinkFox and Temu credentials and can store Temu access tokens locally.

Mitigation: Use narrowly scoped store keys, keep token store files out of source control, and avoid printing or sharing unmasked tokens.

Risk: The skill can submit live Temu price-change requests through the LinkFox gateway.

Mitigation: Require explicit user confirmation and review request payloads before running price-change scripts.

Risk: The skill includes broad proxy and signed file-download helpers.

Mitigation: Prefer the documented task-specific scripts and review destination URLs or API types before using generic proxy or file-download commands.

Risk: The skill persists API responses and session data in local linkfox directories.

Mitigation: Treat generated response files as sensitive operational data and exclude linkfox output directories from commits and shared artifacts.

Risk: Onboarding helpers can create payment orders for LinkFox plans.

Mitigation: Ask for user approval before registration, billing, or payment-order actions and present any returned payment details without polling automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-price-global)
- [API reference](artifact/references/api.md)
- [Access token guide](artifact/references/access-token.md)
- [Onboarding and billing guide](artifact/references/onboarding.md)
- [Partner Global catalog](artifact/references/partner-global-catalog.md)
- [Price API document index](artifact/references/apis/README.md)
- [Temu Partner Global documentation](https://partner-global.temu.com/documentation?menu_code=fb16b05f7a904765aac4af3a24b87d4a)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request examples and shell command snippets; scripts emit JSON responses or summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are persisted under a local linkfox session data directory; large responses are summarized unless inline output is requested.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
