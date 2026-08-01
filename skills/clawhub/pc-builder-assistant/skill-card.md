## Description: <br>
Provides desktop PC build planning, upgrade completion, compatibility checks, and hardware guidance using bundled China-market component data, local validation scripts, and English or Chinese user-facing responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT No Attribution <br>


## Use Case: <br>
Consumers, PC builders, and hardware advisors use this skill to produce desktop parts lists, upgrade paths, compatibility reviews, game FPS references, and hardware-selection explanations. It is scoped to desktop PCs and uses CNY price references for the China market rather than guaranteed local availability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: China-market CNY prices, stock, warranty terms, and exact model variants may not match the user's local buying options. <br>
Mitigation: Recheck current prices, stock, warranty, exact SKUs, and retailer availability before purchase; present CNY references as market references, not local retail quotes. <br>
Risk: Physical compatibility can depend on incomplete or changing vendor details such as case clearance, GPU length, cooler height, PSU fit, fan placement, BIOS support, and cable space. <br>
Mitigation: Run the bundled compatibility checks for complete builds and list any remaining down-to-order verification items for the user. <br>
Risk: The skill can advise on purchases but does not provide transactional safeguards. <br>
Mitigation: Do not use it to place orders, handle payment, or treat recommendations as guaranteed availability. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gongyu0918-debug/skills/pc-builder-assistant) <br>
- [Compatibility checks](references/compatibility.md) <br>
- [English usage](references/english-usage.md) <br>
- [Game performance](references/game-performance.md) <br>
- [Hardware FAQ](references/hardware-faq.md) <br>
- [Hardware scope](references/hardware-scope.md) <br>
- [Pricing](references/pricing.md) <br>
- [Routing](references/routing.md) <br>
- [Scenarios](references/scenarios.md) <br>
- [Selection policy](references/selection-policy.md) <br>
- [Workflows](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown or plain text with structured parts lists, compatibility findings, price notes, and concise guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference local validation scripts and bundled hardware data internally; final user-facing answers should avoid internal status labels and should include price-date and compatibility caveats when recommending parts.] <br>

## Skill Version(s): <br>
0.0.33 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
