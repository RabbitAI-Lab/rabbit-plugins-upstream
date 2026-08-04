## Description: <br>
PC Build Assistant helps agents produce budget-aware desktop PC build plans, upgrades, compatibility checks, and hardware guidance using China-market CNY references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to plan DIY desktop PC builds, complete or upgrade existing configurations, check part compatibility, compare hardware tradeoffs, and produce concise buying guidance. It is scoped to desktops and China-market CNY reference pricing, not laptops, server procurement, ordering, payment, remote control, or security-isolation work. <br>

### Deployment Geography for Use: <br>
Global; price references are China-market CNY data. <br>

## Known Risks and Mitigations: <br>
Risk: China-market CNY reference prices may be stale, incomplete, or different from local retail availability. <br>
Mitigation: Check current market prices when the offline catalog is stale or incomplete, keep CNY totals separate from local prices, and tell users to verify local SKUs, warranty terms, stock, and store pricing before buying. <br>
Risk: The skill is not intended for purchasing, payment, remote control, laptops, server procurement, or security-isolation decisions. <br>
Mitigation: Keep recommendations to desktop planning, compatibility, and hardware guidance; redirect requests outside that scope instead of completing transactions or advising on unsupported procurement and security use cases. <br>
Risk: Hardware recommendations can be misleading if compatibility fields or current prices are missing. <br>
Mitigation: Present unresolved compatibility items as pre-purchase verification points and avoid claiming complete compatibility when required evidence is unavailable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant) <br>
- [Routing](references/routing.md) <br>
- [Selection policy](references/selection-policy.md) <br>
- [Compatibility](references/compatibility.md) <br>
- [Pricing](references/pricing.md) <br>
- [English usage](references/english-usage.md) <br>
- [Workflows](references/workflows.md) <br>
- [Hardware FAQ](references/hardware-faq.md) <br>
- [Hardware scope](references/hardware-scope.md) <br>
- [Scenarios](references/scenarios.md) <br>
- [Game performance](references/game-performance.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown responses with component tables, compatibility notes, CNY prices, tradeoffs, and verification items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use bundled component, case, display, price-floor, and game-FPS data; may ask the agent to check current prices when offline catalog data is stale or incomplete.] <br>

## Skill Version(s): <br>
0.0.34 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
