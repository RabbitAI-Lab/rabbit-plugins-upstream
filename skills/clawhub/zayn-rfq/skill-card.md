## Description: <br>
Analyzes a received RFQ to judge demand authenticity, information completeness, investment value, risk, and recommended next handling steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, sourcing, and quotation teams use this skill to evaluate an incoming RFQ before investing sourcing or engineering effort. It helps identify missing facts, transaction signals, quotation boundaries, risk, and whether to respond, ask follow-up questions, or pause. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: RFQ inputs may contain sensitive customer, pricing, sourcing, or project details. <br>
Mitigation: Use redacted examples when possible and avoid providing unnecessary confidential details. <br>
Risk: The skill's analysis could be mistaken for a binding quotation, inventory promise, delivery commitment, or compatibility confirmation. <br>
Mitigation: Require human review of pricing, stock, delivery, warranty, and compatibility boundaries before acting on or sharing the output. <br>
Risk: Incomplete or conflicting RFQ details can lead to overconfident qualification decisions. <br>
Mitigation: Use the required parameter status table, mark missing or conflicting facts, and limit incomplete cases to clearly labeled preliminary analysis. <br>


## Reference(s): <br>
- [Skill rules](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, analysis, guidance] <br>
**Output Format:** [Markdown with structured RFQ assessment sections and parameter status tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human review before treating outputs as quotations, inventory commitments, compatibility confirmations, or customer-facing promises.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation describes draft rules v0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
