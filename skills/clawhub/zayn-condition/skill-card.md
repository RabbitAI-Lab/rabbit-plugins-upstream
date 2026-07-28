## Description: <br>
Standardizes product condition descriptions using packaging, appearance, labels, testing, and warranty evidence to classify items as new, new old stock, pulled, refurbished, used, or related states. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, RFQ, and quotation teams use this skill to normalize condition terminology, identify evidence gaps, and produce customer-facing condition wording for product quotes. It is intended as a structured decision aid, with final condition, warranty, pricing, stock, lead-time, and customer acceptance claims kept under human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Condition, warranty, price, stock, lead-time, or customer-acceptance claims may be overstated if draft analysis is treated as final. <br>
Mitigation: Keep human verification for final commercial claims and use the skill as a structured draft decision aid. <br>
Risk: Sensitive serial, customer, supplier, or product details may be included in RFQ evidence. <br>
Mitigation: Provide only necessary product and supplier details and redact sensitive serial or customer data when possible. <br>
Risk: Missing or conflicting evidence can cause incorrect condition labels, such as treating pulled or refurbished items as new. <br>
Mitigation: Require the parameter status table, preserve conflicts and unknowns, and avoid converting unverified information into confirmed facts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-condition) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Guidance, Markdown] <br>
**Output Format:** [Markdown with structured sections and a parameter status table] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Formal analysis requires a product object, at least one condition evidence item, and the customer's minimum acceptable condition standard.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation lists internal rule version 0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
