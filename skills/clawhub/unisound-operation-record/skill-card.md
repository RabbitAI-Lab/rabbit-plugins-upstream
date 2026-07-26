## Description: <br>
Generates structured surgical operation records from preoperative, intraoperative, and postoperative clinical materials by calling an internal medical model. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical documentation teams and developers can use this skill to convert de-identified surgical case materials into a structured operation record for clinician review and recordkeeping. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles highly sensitive medical text and sends prepared clinical content to a remote medical model endpoint. <br>
Mitigation: Use only when authorized for the relevant clinical data, and de-identify records before use. <br>
Risk: Prepared or generated output files may contain sensitive medical record content, especially when using --save-prepared or output options. <br>
Mitigation: Avoid saving prepared text unless intentionally needed, and store generated outputs only in approved secure locations. <br>
Risk: Generated operation records may be incomplete or clinically inaccurate if source materials are incomplete or the model output is wrong. <br>
Mitigation: Require review by a qualified clinician before using the generated record for care, filing, or dispute-related purposes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-operation-record) <br>
- [Hivoice medical model chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files] <br>
**Output Format:** [UTF-8 surgical operation record text, with optional JSON or file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires de-identified clinical input and an appkey for the configured Hivoice medical model endpoint.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
