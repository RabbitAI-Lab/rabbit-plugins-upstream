## Description: <br>
基于真实业务证据判断客户是否值得继续投入，并给出当前适合的投入等级和验证动作。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and customer-management teams use this skill to decide whether a customer merits continued investment. It requires customer materials, a stated analysis goal, and at least one reliable business evidence item before producing an investment recommendation and verification actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer and business records may contain sensitive commercial relationship or transaction details. <br>
Mitigation: Use only records the user is authorized to analyze and prefer desensitized inputs where practical. <br>
Risk: Insufficient, conflicting, or unverified evidence could lead to an overconfident customer qualification decision. <br>
Mitigation: Require the parameter status table, preserve conflicts and unverified facts, and request missing critical information before issuing a formal conclusion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-qualify) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [README.md](artifact/README.md) <br>
- [examples.md](artifact/examples.md) <br>
- [tests.md](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured sections and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes parameter completeness, parameter status, evidence strength, positive signals, risk signals, investment recommendation, missing information, and next steps.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
