## Description: <br>
This skill checks outpatient medical records for inconsistencies between physical examination findings and the history of present illness, using a HiVoice MaaS medical LLM to return no defect or a defect with reasons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control teams and healthcare software developers use this skill to screen de-identified outpatient medical records for a specific inconsistency between the history of present illness and physical examination sections. It supports review workflows by producing a concise defect status and reason, but the final conclusion should be reviewed by qualified medical staff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes medical records and sends record content to the configured HiVoice MaaS endpoint. <br>
Mitigation: Use it only where that endpoint is approved for the records being processed, and de-identify records before running the skill. <br>
Risk: The required appkey grants access to the medical LLM endpoint. <br>
Mitigation: Provide the appkey at runtime, keep it out of source control and logs, and rotate it if exposure is suspected. <br>
Risk: The scripts write result files locally and can optionally save prepared input text. <br>
Mitigation: Store, restrict, or delete generated files according to medical-data retention rules, and avoid --save-prepared unless it is needed for debugging. <br>
Risk: The output is an automated quality-control signal and may be wrong or incomplete. <br>
Mitigation: Treat results as review support and require qualified medical staff to make final clinical or quality decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-pe-hpi-inconsistent) <br>
- [HiVoice MaaS chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands] <br>
**Output Format:** [UTF-8 text with CLI status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes the quality-control result to a local text file; scripts/run.py can optionally write prepared input text when --save-prepared is used.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
