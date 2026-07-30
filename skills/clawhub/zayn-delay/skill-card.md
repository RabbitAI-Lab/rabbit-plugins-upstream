## Description: <br>
在订单出现延期风险时，区分预警与已延期状态，并设计事实清楚、不过度承诺的客户沟通和解决方案。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Order and delivery teams use this skill when an order or project has delivery-delay risk. It helps separate early warnings from confirmed delays, identify customer-safe facts, and draft solution-oriented communication without overcommitting to unverified dates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer-facing delivery commitments may be inaccurate if users provide unverified dates, progress, or solution details. <br>
Mitigation: Use confirmed order, delivery, and solution facts only, and review any customer-facing commitments before sending. <br>
Risk: Users may include more customer, order, or internal responsibility information than the workflow needs. <br>
Mitigation: Provide only the order, customer, and internal responsibility details needed for the delay-risk communication task. <br>
Risk: The documentation is primarily Chinese, which may create operational fit or review issues for teams working in other languages. <br>
Mitigation: Confirm that operators understand the Chinese workflow or localize and review the prompts before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-delay) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Usage template](artifact/examples.md) <br>
- [Test criteria](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance] <br>
**Output Format:** [Markdown text with a parameter status table, delay assessment, risk notes, recommendations, customer-facing draft, and internal next steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires confirmed delivery facts before formal analysis; incomplete inputs should produce only a clearly labeled preliminary analysis.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence; artifact documents draft rule version v0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
