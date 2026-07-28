## Description: <br>
Helps users screen Alibaba RFQs for whether they are worth opening, quoting, or spending quote quota on, while identifying commercial fit and execution risks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, sourcing, and Alibaba marketplace operators use this skill to triage RFQ listings, check required RFQ parameters, decide whether to quote, and choose one next action: quick response, further verification, or skip. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may influence commercial quoting decisions when RFQ information, company capability, compliance limits, or quote quota data is incomplete. <br>
Mitigation: Use the output as business decision support only, and verify RFQ facts, supply capability, compliance boundaries, and quota use before acting. <br>
Risk: Platform signals such as buyer verification, recommendations, or scarce quote slots can be mistaken for confirmed purchase intent. <br>
Mitigation: Keep platform signals secondary and require explicit demand evidence before treating an RFQ as high quality. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-ali-rfq-scan) <br>
- [Publisher profile](https://clawhub.ai/user/zaynpeng) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown analysis with a parameter status table, screening conclusion, risks, quota recommendation, and one next action.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not generate final quote fields, submit quotes, consume quote quota, or access accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact documentation states 0.2.0 draft content) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
