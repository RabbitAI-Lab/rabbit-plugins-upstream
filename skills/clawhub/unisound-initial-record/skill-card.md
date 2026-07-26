## Description: <br>
Generates structured initial outpatient medical record text from Chinese doctor-patient dialogue. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinicians, medical documentation teams, and developers can use this skill to transform de-identified Chinese doctor-patient dialogue into structured first-visit medical record text for review and downstream parsing. A licensed clinician should review the generated record before clinical use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive health dialogue and may send de-identified clinical text to a remote medical LLM endpoint. <br>
Mitigation: Use only de-identified dialogue, confirm the remote endpoint is approved for the data, and require clinician review before relying on generated records. <br>
Risk: Prepared dialogue or generated output may be written to local files when debugging or output options are used. <br>
Mitigation: Avoid --save-prepared unless persistence is intentional, store outputs under the applicable retention policy, and delete generated debug or output files when no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-initial-record) <br>
- [Skill-declared medical model API base URL](https://maas-api.hivoice.cn/v1) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Structured plain text with one medical-record field or subfield per line.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can print to stdout or write to an output file; --save-prepared can persist preprocessed dialogue for debugging.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
