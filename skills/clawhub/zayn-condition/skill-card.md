## Description: <br>
根据包装、外观、标签、测试和保修信息，规范判断全新、库存新件、拆机、翻新或二手等成色状态。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees and external business users use this skill to standardize product-condition descriptions for RFQ and quotation workflows. It helps assess packaging, appearance, labels, testing, warranty, mixed-batch, and source evidence before producing customer-facing condition language. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process business RFQ details such as product models, supplier definitions, serial numbers, warranty status, and customer requirements. <br>
Mitigation: Provide only information appropriate for the agent to analyze and redact sensitive commercial or identifying details when they are not required. <br>
Risk: Incomplete or conflicting product-condition evidence can lead to incorrect condition labels. <br>
Mitigation: Use the documented parameter status table and keep missing, conflicting, or unverified facts marked as preliminary or pending confirmation. <br>
Risk: Overstating originality, packaging, warranty, or newness can mislead customers. <br>
Mitigation: Base external wording on human-confirmed facts and preserve risk warnings when evidence does not support a firm condition claim. <br>


## Reference(s): <br>
- [CONDITION() source rules](artifact/SKILL.md) <br>
- [CONDITION() README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-condition) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured tables and concise prose] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a parameter completeness conclusion, parameter status table, recommended condition definition, evidence, open confirmations, external phrasing, risk warnings, and customer confirmation items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
