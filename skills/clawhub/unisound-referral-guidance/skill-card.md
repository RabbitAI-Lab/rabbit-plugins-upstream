## Description: <br>
基层转诊指导。输入患者病情摘要，判断是否需要转诊、紧急程度、目标科室/医院级别，给出转诊前处置和随附材料清单（JSON + 自然语言摘要）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Community clinic and primary-care clinicians use this skill to turn a patient case summary into referral decision support, including urgency, target department or hospital level, pre-transfer actions, and required transfer documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patient summaries are sent to a remote LLM endpoint and may contain sensitive medical content. <br>
Mitigation: Use only de-identified patient summaries and confirm that the endpoint and app-key handling meet applicable privacy and medical compliance requirements before use. <br>
Risk: The skill provides referral decision support but does not replace clinical judgment. <br>
Mitigation: Have qualified clinicians review outputs before relying on them, and prioritize direct emergency care when the patient's condition is urgent. <br>
Risk: Optional output files may contain sensitive medical guidance or case details. <br>
Mitigation: Store generated output only in approved locations and handle it under the same controls used for sensitive clinical records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-referral-guidance) <br>
- [Remote medical LLM endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, guidance, configuration] <br>
**Output Format:** [JSON plus natural-language summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can print to stdout or write the referral guidance output to a file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
