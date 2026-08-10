## Description:

Use for English and Chinese desktop PC build planning, upgrades, compatibility checks, configuration completion, hardware questions, and user-supplied local price catalogs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to plan desktop PC builds, review upgrades, complete partial configurations, check component compatibility, reason about hardware choices, and work with local price catalog overlays.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled or searched prices can be stale, region-specific, or unavailable at checkout.

Mitigation: Treat prices as references, verify current retailer pricing before purchase, and keep CNY catalog prices separate from user-provided local-currency overlays.

Risk: Compatibility conclusions can be incomplete when catalog fields or user-supplied hardware details are missing.

Mitigation: Run the bundled compatibility checks for complete builds and surface concrete unresolved items such as clearances, connectors, display outputs, or QVL details.

Risk: User-provided overlay data can contain wrong SKUs, currencies, dates, or specifications.

Mitigation: Validate overlay JSON, preserve exact SKU identity, use the same overlay consistently for queries and compatibility checks, and avoid mixed-currency totals.

Risk: Historical price lookup and stale-price fallback can require external web or fixed GitHub reads.

Mitigation: Use these lookups only for price evidence, avoid treating version history as a live quote, and verify final availability and compatibility before buying parts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant)
- [SKILL.md](SKILL.md)
- [English usage](references/english-usage.md)
- [Routing](references/routing.md)
- [Selection policy](references/selection-policy.md)
- [Workflows](references/workflows.md)
- [Compatibility](references/compatibility.md)
- [Pricing](references/pricing.md)
- [Hardware scope](references/hardware-scope.md)
- [Game performance](references/game-performance.md)
- [User catalog overlays](references/user-catalog.md)
- [Price history](references/price-history.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or concise text with structured PC part lists, price notes, compatibility findings, and verification items]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use bundled local catalogs, user-provided overlay JSON, and local Python tooling to support recommendations.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
