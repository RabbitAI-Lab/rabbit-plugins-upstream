## Description:

PC Build Assistant helps agents produce desktop PC build plans, upgrade suggestions, compatibility checks, and hardware guidance using China-market CNY references for gaming, creator, local AI, and compact builds.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to plan or review DIY desktop PC configurations, compare upgrades, complete part lists, and answer desktop hardware selection questions with CNY price references and compatibility checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hardware prices, stock, compatibility details, and exchange rates can change before purchase.

Mitigation: Verify current retailer listings, manufacturer specifications, warranty terms, and local availability before buying parts.

Risk: China-market CNY references may not match a user's local SKUs, warranty coverage, prices, or stock.

Mitigation: Treat CNY builds as reference configurations and confirm equivalent local models, retailers, warranty terms, and final prices.

Risk: Part recommendations could be mistaken for purchase or payment automation.

Mitigation: Use the skill for planning and review only; users should make all ordering and payment decisions manually.

## Reference(s):

- [Compatibility Checks](references/compatibility.md)
- [English Usage](references/english-usage.md)
- [Game Performance Reference](references/game-performance.md)
- [Hardware FAQ](references/hardware-faq.md)
- [Hardware Scope](references/hardware-scope.md)
- [Pricing Rules](references/pricing.md)
- [Request Routing](references/routing.md)
- [Scenario Rules](references/scenarios.md)
- [Component Selection Policy](references/selection-policy.md)
- [Workflow Modes](references/workflows.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or concise structured text with part lists, prices, totals, compatibility conclusions, tradeoffs, and purchase verification notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers should preserve CNY price references, avoid unsupported model, price, FPS, or compatibility claims, and keep ordering or payment decisions outside the skill.]

## Skill Version(s):

0.0.35 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
