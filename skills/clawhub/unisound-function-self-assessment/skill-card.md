## Description: <br>
Supports postoperative rehabilitation functional self-assessment by collecting questionnaire answers, calculating basic scores, and generating Markdown interpretation through a documented medical model API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients and care teams use this skill to capture postoperative rehabilitation self-assessment responses, compute basic item and total scores, and receive Markdown guidance for reviewing functional recovery. The skill is bounded to questionnaire collection, basic scoring, and supportive interpretation; it does not replace clinical evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/unisound-llm/skills/unisound-function-self-assessment) <br>
- [ResearchKit](https://github.com/ResearchKit/ResearchKit) <br>
- [Hivoice medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [UTF-8 JSON containing structured assessment data and Markdown text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey and sends assessment content to the documented hivoice.cn medical model endpoint; Office, PDF, and image inputs may run local conversion or OCR tools before API submission.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
