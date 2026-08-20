## Description:

Helps an agent manage Temu Partner EU product catalog operations through LinkFox gateway scripts and references, including product lookup, detail retrieval, SKU and stock queries, edits, deletion, listing status changes, compliance edits, category checks, property templates, external codes, and video cover retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operators use this skill to guide and execute Temu EU product-management workflows through LinkFox, including finding goods, inspecting details, changing stock or listing status, updating product fields, editing compliance data, and deleting products when explicitly intended.

### Deployment Geography for Use:

Europe (Temu Partner EU catalog operations)

## Known Risks and Mitigations:

Risk: The skill can mutate live Temu EU catalog data, including product deletion, stock changes, listing status changes, compliance edits, and full or partial product updates.

Mitigation: Require explicit human confirmation for destructive or high-impact operations, and review the target goodsId, skuId, operation type, and request payload before running a script.

Risk: The skill handles LinkFox and Temu credentials and may persist Temu access tokens locally.

Mitigation: Use least-privilege and short-lived tokens where possible, keep token files out of shared workspaces and source control, and avoid exposing tokens in command history or logs.

Risk: Custom gateway or endpoint environment variables could redirect requests away from the default LinkFox gateway.

Mitigation: Avoid overriding gateway or login endpoint environment variables unless the endpoint is trusted and intentionally configured.

Risk: The server security summary reports live catalog mutation, credential handling, billing flows, and local data persistence with insufficient guardrails.

Mitigation: Install only when the user trusts LinkFox and needs this Temu EU catalog-management capability; review and scan the skill before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-manage-product-eu)
- [API reference](artifact/references/api.md)
- [Partner EU manage product catalog](artifact/references/partner-eu-catalog.md)
- [Per-interface API references](artifact/references/apis/README.md)
- [Access token guide](artifact/references/access-token.md)
- [Onboarding and authentication recovery](artifact/references/onboarding.md)
- [Temu Partner EU documentation](https://partner-eu.temu.com/documentation?menu_code=7289390cfd724be4a196f11ebe45a896)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, JSON, files]

**Output Format:** [Markdown guidance with inline shell commands; scripts emit JSON responses or summaries and write response JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a LinkFox API key plus a Temu accessToken or stored storeKey; high-impact catalog changes should be explicitly confirmed by a human before execution.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
