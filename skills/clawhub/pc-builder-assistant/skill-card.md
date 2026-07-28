## Description: <br>
PC Build Assistant helps agents produce desktop PC build plans, upgrade guidance, compatibility checks, and hardware Q&A using China-market CNY reference data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to ask an agent for desktop PC build recommendations, upgrade paths, compatibility reviews, and hardware-selection explanations. It is scoped to desktop hardware guidance and does not support laptops, server procurement, ordering, payment handling, remote control, or security-isolation work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Build recommendations may rely on China-market CNY reference prices or current availability checks that differ from a user's local retail market. <br>
Mitigation: Verify local stock, warranty terms, and final checkout prices before purchasing. <br>
Risk: A suggested desktop configuration may still require pre-purchase checks for fit, compatibility, and exact SKU details. <br>
Mitigation: Review the skill's compatibility conclusion and listed verification items before buying components. <br>


## Reference(s): <br>
- [Compatibility Checks](references/compatibility.md) <br>
- [English Usage](references/english-usage.md) <br>
- [Game Performance](references/game-performance.md) <br>
- [Hardware FAQ](references/hardware-faq.md) <br>
- [Hardware Scope](references/hardware-scope.md) <br>
- [Pricing Rules](references/pricing.md) <br>
- [Requirement Routing](references/routing.md) <br>
- [Scenario Rules](references/scenarios.md) <br>
- [Selection Policy](references/selection-policy.md) <br>
- [Workflows](references/workflows.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text with structured build lists and compatibility notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CNY reference prices, price dates, compatibility conclusions, trade-off notes, and pre-purchase verification items.] <br>

## Skill Version(s): <br>
0.0.29 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
