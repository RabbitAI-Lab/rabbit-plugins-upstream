## Description: <br>
Uses real business evidence to judge whether a customer is worth continued investment and to recommend the current engagement level and validation actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zaynpeng](https://clawhub.ai/user/zaynpeng) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales and customer-management teams use this skill to qualify customers from provided customer profiles, business records, stated goals, and at least one reliable piece of evidence. It helps separate confirmed facts from weak signals, identify missing or conflicting information, and choose an appropriate next engagement action. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer qualification may involve sensitive business or customer information. <br>
Mitigation: Provide only data that is allowed to be processed, and prefer desensitized examples where possible. <br>
Risk: Qualification recommendations can influence sales or customer investment decisions. <br>
Mitigation: Use the skill output as decision support and have a person review final customer decisions. <br>
Risk: Weak, missing, or conflicting evidence could be mistaken for confirmed facts. <br>
Mitigation: Require a parameter status table, preserve conflicts and unverified items, and request missing information before issuing a formal conclusion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zaynpeng/skills/zayn-qualify) <br>
- [Skill rules](artifact/SKILL.md) <br>
- [README](artifact/README.md) <br>
- [Calling template](artifact/examples.md) <br>
- [Test criteria](artifact/tests.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, analysis] <br>
**Output Format:** [Structured Markdown analysis with a parameter status table, evidence assessment, investment recommendation, missing information, and next steps.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires user-provided customer evidence; asks for missing or conflicting information before a formal conclusion.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact docs state v0.1 draft rules) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
