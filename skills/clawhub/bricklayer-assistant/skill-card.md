## Description: <br>
瓦匠全流程助手 helps masonry and tiling workers calculate materials, look up mortar ratios, estimate prices, plan tile layouts, follow workmanship and safety guidance, diagnose quality issues, and produce text or interactive HTML reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and construction practitioners use this skill for masonry and tiling planning, including material estimates, mortar mix guidance, local-price reference estimates, tile layout planning, workmanship checklists, troubleshooting, acceptance checks, and safety reminders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Construction calculations, procedures, and acceptance thresholds may not match local building-code requirements or site conditions. <br>
Mitigation: Treat outputs as estimates, verify local codes and project requirements, and consult a qualified professional for structural, waterproofing, electrical-adjacent, or safety-critical work. <br>
Risk: Price guidance is reference data and may be stale or inaccurate for a user's city, materials, labor market, and payment terms. <br>
Mitigation: Confirm current local prices, site conditions, quantities, and contract terms before using generated estimates for bidding or purchasing. <br>
Risk: Generated work guidance could be followed without appropriate personal protective equipment or tool safety checks. <br>
Mitigation: Apply the skill's safety checklist, use required PPE, and stop or escalate work when high-risk tasks exceed the user's qualification or site controls. <br>


## Reference(s): <br>
- [Calculation Reference](artifact/references/calculation-reference.md) <br>
- [Mortar Ratio Reference](artifact/references/mortar-ratio.md) <br>
- [Pricing Reference](artifact/references/pricing-reference.md) <br>
- [Tile Layout Guide](artifact/references/tile-layout.md) <br>
- [Workmanship Standards](artifact/references/workmanship-standards.md) <br>
- [Troubleshooting Guide](artifact/references/troubleshooting.md) <br>
- [Acceptance Checklist](artifact/references/acceptance-checklist.md) <br>
- [Safety Guidelines](artifact/references/safety-guidelines.md) <br>
- [Material Calculation Helper](artifact/references/bricklayer_calc.py) <br>
- [Project homepage](https://github.com/bettermen/bricklayer-assistant) <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/bricklayer-assistant) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text, interactive HTML reports, and JSON calculation output from the helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference a local Python calculation helper; simple queries can be answered directly without generating HTML.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
