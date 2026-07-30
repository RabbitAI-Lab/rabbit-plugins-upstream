## Description: <br>
Compares candidate replacement options when the requested model, configuration, brand, condition, price, or lead time cannot be satisfied, highlighting differences, risks, and confirmation boundaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Procurement, sales, and quotation teams use this skill to compare proposed replacement products for RFQ workflows and identify which differences, risks, and acceptance points require customer or human confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Replacement comparisons can be mistaken for confirmed compatibility or approval. <br>
Mitigation: Keep compatibility, pricing, stock, lead-time, warranty, and customer acceptance decisions under human confirmation. <br>
Risk: Incomplete or conflicting RFQ details can produce misleading comparisons. <br>
Mitigation: Require verified product, quotation, and boundary details before relying on a formal comparison; otherwise label the result as preliminary. <br>


## Reference(s): <br>
- [Skill Rules](SKILL.md) <br>
- [README](README.md) <br>
- [Examples](examples.md) <br>
- [Tests](tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown analysis with parameter status, option comparison, risks, recommended wording, and a customer confirmation checklist] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided RFQ and product details; compatibility, pricing, stock, lead time, warranty, and acceptance decisions remain subject to human confirmation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact rules version v0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
