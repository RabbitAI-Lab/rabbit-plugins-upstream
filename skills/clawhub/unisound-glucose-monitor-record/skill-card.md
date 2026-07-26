## Description: <br>
病人端慢病管理血糖监测记录。参考 Glucosio 的 blood glucose logging 部分，构建慢病管理基础记录能力。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to record and structure blood glucose measurements for chronic disease management workflows. It extracts values, units, measurement timing, measurement type, and notes, then returns a standardized blood glucose record with a short patient-facing summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive blood glucose records and text extracted from documents or images may be sent to a remote medical AI endpoint. <br>
Mitigation: Use only when that data sharing is acceptable; submit the minimum necessary record fields and avoid unrelated medical or personal information. <br>
Risk: Generated analysis, abnormal-value flags, and lifestyle suggestions may be mistaken for diagnosis or treatment advice. <br>
Mitigation: Treat generated text as informational only and require qualified clinical review for diagnosis, treatment, medication, or care decisions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/unisound-llm/skills/unisound-glucose-monitor-record) <br>
- [Glucosio F-Droid package](https://f-droid.org/packages/org.glucosio.android/) <br>


## Skill Output: <br>
**Output Type(s):** [json, markdown, shell commands, guidance] <br>
**Output Format:** [UTF-8 JSON containing structured record data and Markdown/natural-language text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey for the remote medical AI endpoint; can write output to stdout or a JSON file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
