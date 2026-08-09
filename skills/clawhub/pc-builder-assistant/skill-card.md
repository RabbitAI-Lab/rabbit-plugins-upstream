## Description:

PC Build Assistant helps agents produce China-market desktop PC build recommendations, upgrade plans, compatibility checks, and hardware guidance with CNY price references and explicit scope limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to plan DIY desktop PC builds, complete or upgrade configurations, check component compatibility, and answer desktop hardware selection questions. It is scoped to desktop PCs and uses China-market CNY references rather than claiming local availability elsewhere.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bundled prices are references and may be stale or differ from current retailer availability.

Mitigation: Verify current market prices, stock, warranty terms, and local equivalents before purchasing.

Risk: Compatibility conclusions depend on available component fields and may leave physical fit, cabling, fan placement, or lane-sharing items unresolved.

Mitigation: Run the bundled strict compatibility check for full builds and list unresolved review items for manual confirmation before ordering.

Risk: The skill is scoped to desktop PC planning and does not perform purchases, remote control, security isolation, laptop selection, or server procurement.

Mitigation: Keep use within desktop PC planning and route out-of-scope requests to appropriate tools or human review.

## Reference(s):

- [Compatibility Checks](artifact/references/compatibility.md)
- [English Usage](artifact/references/english-usage.md)
- [Game Performance](artifact/references/game-performance.md)
- [Hardware FAQ](artifact/references/hardware-faq.md)
- [Hardware Scope](artifact/references/hardware-scope.md)
- [Pricing Rules](artifact/references/pricing.md)
- [Request Routing](artifact/references/routing.md)
- [Scenario Rules](artifact/references/scenarios.md)
- [Selection Policy](artifact/references/selection-policy.md)
- [Workflow Modes](artifact/references/workflows.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with component tables, compatibility findings, price references, and concise hardware guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses bundled local data and scripts for candidate lookup, game FPS samples, power budgets, and compatibility checks; final user-facing output should avoid internal script status details.]

## Skill Version(s):

0.0.38 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
