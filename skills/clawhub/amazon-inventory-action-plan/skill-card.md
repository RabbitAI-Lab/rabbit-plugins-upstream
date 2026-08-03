## Description: <br>
Turn Amazon inventory data into a prioritized operating plan for stockout recovery, restocking, inventory pacing, or overstock clearance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[techterrydev](https://clawhub.ai/user/techterrydev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers use this skill to diagnose stockout recovery, tight inventory, working inventory, and excess inventory situations, then plan prioritized operating actions. It helps coordinate inventory, demand, advertising, promotion, and clearance decisions while keeping purchase, pricing, promotion, advertising, and account changes subject to human approval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The user may provide business-sensitive inventory, sales, supplier, margin, or cash data. <br>
Mitigation: Provide only relevant inputs, redact account identifiers where possible, and keep identifiers separate from calculations unless they are needed for the recommendation. <br>
Risk: Inventory recommendations can affect purchases, pricing, promotions, advertising, liquidation, disposal, tax, compliance, or account operations. <br>
Mitigation: Treat outputs as planning guidance and require human review before taking any purchase, pricing, promotion, advertising, tax, compliance, or account action. <br>
Risk: Missing or uncertain demand, lead-time, inbound, or usable-stock data can make reorder or clearance decisions unreliable. <br>
Mitigation: Mark missing inputs as unknown, show coverage assumptions and confidence, and request the data needed before presenting quantity-sensitive decisions. <br>


## Reference(s): <br>
- [Server-resolved GitHub source](https://github.com/TechTerryDev/amazon-seller-skills/tree/main/skills/amazon-inventory-action-plan) <br>
- [ClawHub skill page](https://clawhub.ai/techterrydev/skills/amazon-inventory-action-plan) <br>
- [Publisher profile](https://clawhub.ai/user/techterrydev) <br>
- [AMZ Helper](https://amzhelper.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown action plan with tables, scenario outlooks, checkpoints, and approval notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces planning guidance only; it does not access Seller Central or execute account, pricing, promotion, advertising, ordering, fulfillment, tax, or compliance actions.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
