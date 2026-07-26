## Description: <br>
Structures Chinese outpatient follow-up medical record text into fine-grained fields such as present illness, history, diagnosis, and treatment plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, clinical operations teams, and agents can use this skill to convert Chinese outpatient follow-up records into a consistent field-by-field text structure for review or downstream record workflows. It is an extraction aid and does not provide diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends medical record text to a configured remote model service. <br>
Mitigation: Use it only where that data transfer is approved, and prefer test or de-identified inputs unless the publisher adds verified de-identification controls. <br>
Risk: Output and save-prepared options can create sensitive local files. <br>
Mitigation: Treat generated files as sensitive medical records and store, share, or delete them according to the user's data-handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-followup-record) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [Internal medical model API endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [UTF-8 text with field:value lines; optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns missing fields as 未提及 and normalizes some absent-history values to 无.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
