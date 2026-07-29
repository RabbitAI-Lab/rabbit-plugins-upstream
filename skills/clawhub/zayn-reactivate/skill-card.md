## Description: <br>
判断沉睡客户是否值得重新联系，并设计带有真实新价值、低回复负担和停止条件的激活方式。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and account-management users use this skill to decide whether dormant customers are worth re-contacting, identify a genuine new value to offer, and draft a low-burden reactivation approach with stop conditions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer-reactivation inputs can include personal, customer, or commercially sensitive information. <br>
Mitigation: Avoid pasting unnecessary sensitive data and provide only the minimum customer context needed for the analysis. <br>
Risk: Outreach recommendations could be used in ways that conflict with consent, opt-out, or anti-spam obligations. <br>
Mitigation: Review proposed contact plans against applicable consent, opt-out, and anti-spam requirements before contacting customers. <br>
Risk: The skill may be asked to infer current customer demand from stale history or weak evidence. <br>
Mitigation: Require at least one reliable evidence item, separate facts from assumptions, preserve conflicts for human verification, and avoid treating historical purchases as current demand. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-reactivate) <br>
- [Skill rules](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Examples](artifact/examples.md) <br>
- [Tests](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown analysis with a parameter status table, activation assessment, recommended outreach wording, next contact timing, and stop conditions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires customer background, cooperation history, last contact, activation goal, and at least one reliable evidence item before formal analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
