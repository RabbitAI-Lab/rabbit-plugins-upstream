## Description: <br>
Selects the primary diagnosis and primary surgery from provided candidate lists for an inpatient record using patient-record summaries and an internal medical LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Medical coding and record-review teams use this skill to select primary diagnosis and primary surgery values from supplied candidate lists for inpatient records. The output supports insurance coding or medical-record front-page assistance and is not medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patient-record text can be sent to a remote LLM endpoint. <br>
Mitigation: Use only in an approved medical-data environment, de-identify records before use, confirm the base endpoint is trusted and HTTPS, and protect the appkey. <br>
Risk: Prepared record text or output files can be written locally when optional save/output flags are used. <br>
Mitigation: Avoid local saved files unless storage permissions, retention rules, and access controls are appropriate. <br>
Risk: The generated selection could be mistaken for clinical diagnosis or treatment advice. <br>
Mitigation: Use the output only as coding or medical-record assistance and require appropriate human review before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-primary-diagnosis-surgery-selection) <br>
- [Default internal medical LLM API base](https://maas-api.hivoice.cn/v1) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, text] <br>
**Output Format:** [JSON object with main_diagnosis and main_surgery fields.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires patient-record text or structured JSON, supplied candidate diagnoses and surgeries, an appkey, and a trusted HTTPS LLM endpoint.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
