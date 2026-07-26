## Description: <br>
Checks outpatient medical records for inconsistencies between the chief complaint and history of present illness, then returns whether a defect is present and the reason when applicable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control teams and healthcare workflow developers use this skill to review de-identified outpatient records for a specific consistency issue between chief complaint and HPI fields. Its output is intended to support clinician review, not replace medical judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive medical-record text may be sent to a configurable model endpoint. <br>
Mitigation: Use only de-identified records and route requests through an approved endpoint before running the skill. <br>
Risk: The skill can write QC results, and optional prepared text, to local files. <br>
Mitigation: Use controlled output paths, restrict access to generated files, and avoid --save-prepared unless the debug artifact is explicitly needed. <br>
Risk: The required app key is sensitive credential material. <br>
Mitigation: Provide the app key at runtime through a secure channel and do not store it in the repository or generated artifacts. <br>
Risk: The result is a medical quality-control aid and may be wrong or incomplete. <br>
Mitigation: Require review by a licensed clinician before relying on the output for clinical or operational decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-chief-complaint-hpi-inconsistent) <br>
- [Unisound publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [HiVoice MaaS API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [UTF-8 text result saved to a file and printed to stdout] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns either no defect or defect plus a reason; file output path is configurable.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
