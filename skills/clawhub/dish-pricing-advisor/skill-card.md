## Description: <br>
Analyzes restaurant menu costs, prices, sales, and menu-engineering signals to produce data-grounded pricing, promotion, rework, and delisting recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monsterdt](https://clawhub.ai/user/monsterdt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External restaurant owners, franchise investors, menu operators, and menu-development teams use this skill to turn menu, cost, pricing, and sales data into practical profit and portfolio actions. It helps identify which dishes should be repriced, promoted, reworked, or removed based on menu engineering, BCG classification, price elasticity, sales analysis, and full-cost pricing signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive business inputs such as menu costs, prices, sales, and operating-cost figures. <br>
Mitigation: Use it only with data the restaurant is comfortable providing, and avoid unnecessary sensitive detail when a lower-granularity analysis is sufficient. <br>
Risk: Pricing and delisting recommendations could materially affect menus, POS records, financial assumptions, or operations if applied automatically. <br>
Mitigation: Treat recommendations as decision support and require operator or finance review before changing prices, delisting items, or updating operational systems. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/monsterdt/skills/dish-pricing-advisor) <br>
- [Methodology reference](references/methodology.md) <br>
- [SkillHub listing](references/skillhub_listing.md) <br>
- [Sample menu input](references/sample_menu.json) <br>
- [Sample joint-dashboard input](references/sample_joint.json) <br>
- [Sample joint-dashboard report](references/sample_joint_report.md) <br>
- [Sales entry page](references/sales_entry.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown reports with JSON or CSV inputs and optional JSON outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Deterministic analysis based on user-provided menu, cost, price, sales, and operating-cost data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
