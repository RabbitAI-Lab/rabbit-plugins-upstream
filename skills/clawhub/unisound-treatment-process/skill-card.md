## Description: <br>
根据病程记录生成诊疗经过。输入病程记录文本，调用内部医疗大模型，输出结构化诊疗经过文本。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical documentation teams and healthcare developers use this skill to turn de-identified inpatient progress notes into a structured treatment-process summary for record archiving, medical-record-homepage completion, and case statistics. Physician review remains required before operational use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical-record text is sent to a remote model endpoint. <br>
Mitigation: Use only an endpoint approved for the relevant medical data and send de-identified records. <br>
Risk: Patient-derived text can be saved locally through output options or --save-prepared. <br>
Mitigation: Write outputs only to protected locations and avoid --save-prepared unless there is a secure retention plan. <br>
Risk: Generated treatment summaries may be incomplete or clinically inaccurate. <br>
Mitigation: Require review by a licensed physician before using the summary in clinical or administrative workflows. <br>
Risk: The appkey is a bearer credential for the model endpoint. <br>
Mitigation: Treat the appkey as sensitive and provide it through secure operational controls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-treatment-process) <br>
- [Unisound-LLM publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, files] <br>
**Output Format:** [UTF-8 treatment-process summary text, with optional saved text or JSON output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save preprocessed patient-derived text when --save-prepared is used; output directories are created automatically.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
