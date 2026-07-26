## Description: <br>
Checks outpatient medical records for missing blood pressure or blood glucose control details in the past medical history and returns either no defect or a defect reason. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control users and developers use this skill to review outpatient medical-record text for a specific past-medical-history rule: hypertension history without blood-pressure control information or diabetes history without blood-glucose control information. It supports plain text and, through its unified runner, common document and table inputs before writing a local UTF-8 result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical-record text may contain sensitive patient data and is sent to the configured LLM service. <br>
Mitigation: Use the skill only when authorized for the records and LLM service, and de-identify patient data before execution. <br>
Risk: The app key is required for LLM access and could be exposed if stored in source control or logs. <br>
Mitigation: Provide the key at runtime, keep it out of repositories, and avoid sharing command histories or logs that contain it. <br>
Risk: Changing --base could route record text to an unapproved endpoint. <br>
Mitigation: Restrict --base to an approved HiVoice MaaS or organization-approved endpoint before use. <br>
Risk: The result and optional prepared text can be written to local storage. <br>
Mitigation: Choose a secure output path and use --save-prepared only when intentionally retaining preprocessed sensitive text. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-pmh-missing-bp-glucose) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [HiVoice MaaS OpenAI-compatible chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, configuration] <br>
**Output Format:** [UTF-8 text result, with Markdown documentation and inline bash examples for setup and execution] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs either no defect or defect plus a reason; results are printed and saved to a local file.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
