## Description:

Use for English desktop PC build planning, upgrades, compatibility checks, configuration completion, and user-supplied local price catalogs, with bundled China-market CNY price references and explicit user overlays kept currency-separated.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and developers use this skill to plan desktop PC builds, upgrades, component substitutions, compatibility checks, hardware-selection explanations, game FPS references, and user-supplied local catalog overlays. It is not intended for laptops, server procurement, ordering or payment, remote control, or security isolation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Component recommendations, compatibility findings, price references, and FPS references can be incomplete or stale.

Mitigation: Verify current prices, exact SKU specifications, compatibility constraints, and performance expectations before purchase.

Risk: The skill may run local Python helper scripts and read user-provided overlay or catalog files.

Mitigation: Review helper script behavior and only provide overlay/catalog files you intended the agent to use.

Risk: The skill is not designed for ordering, payment, remote control, server procurement, or security-isolation decisions.

Mitigation: Keep use limited to planning and advisory workflows, and use separate trusted processes for purchasing, remote administration, and security-sensitive decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [English usage](references/english-usage.md)
- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Workflows](references/workflows.md)
- [User catalog overlay](references/user-catalog.md)
- [User overlay schema](references/user-overlay.schema.json)
- [Game performance](references/game-performance.md)
- [Hardware scope](references/hardware-scope.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Price history](references/price-history.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and concise natural-language guidance, with local Python helper commands used by the agent as needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include component tables, reference prices, totals, compatibility findings, trade-offs, verification items, FPS references, and normalized user overlay data.]

## Skill Version(s):

0.1.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
