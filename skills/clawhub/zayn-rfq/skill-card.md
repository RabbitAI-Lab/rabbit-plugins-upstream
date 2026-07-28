## Description: <br>
分析一条已收到的询价，判断需求真实性、信息完整度、投入价值、风险和下一步处理方式。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and sourcing users use this skill to review an incoming RFQ, check whether the request has enough evidence to justify follow-up, identify missing or conflicting facts, and decide the next handling step. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Business inquiry details may include commercially sensitive customer, pricing, payment, quantity, and supply information. <br>
Mitigation: Provide only the RFQ details needed for analysis and avoid unnecessary confidential or personal data. <br>
Risk: Incomplete RFQ information could be mistaken for a confirmed buying signal or final project commitment. <br>
Mitigation: Use the skill's parameter status and missing-information checks before treating the analysis as a formal follow-up basis. <br>
Risk: The skill may surface quote boundaries, but it does not perform quoting, submission, or account-changing actions. <br>
Mitigation: Require human confirmation for final price, inventory, delivery, compatibility, and customer acceptance decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-rfq) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis with parameter status, evidence signals, missing information, risks, recommendations, quote boundaries, and downstream skill suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable code, persistence, credential use, or automatic external actions are present in the release evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
