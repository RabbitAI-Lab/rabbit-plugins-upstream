## Description: <br>
Helps agents assess condition labels for hardware, equipment, spare parts, and used products from packaging, appearance, labels, serial numbers, tests, repair records, and warranty evidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external users use this skill to structure product-condition reviews for RFQ and quotation workflows, including required evidence, unresolved questions, recommended condition wording, and customer confirmation items. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Users may treat the skill's decision-support output as final confirmation of product facts, warranty status, compatibility, pricing, inventory, or customer acceptance. <br>
Mitigation: Require human confirmation of product facts, warranty status, compatibility, pricing, inventory, and customer acceptance before relying on the output. <br>
Risk: Incomplete or conflicting evidence can lead to overconfident condition labels. <br>
Mitigation: Use preliminary analysis when minimum inputs are missing, preserve conflicts and unknowns, and list the evidence needed before producing a formal condition recommendation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-condition) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>
- [Changelog](artifact/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with a parameter status table, evidence summary, condition recommendation, risk notes, and customer confirmation items] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a product object, at least one condition evidence item, and the customer's minimum acceptable condition before formal analysis.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
