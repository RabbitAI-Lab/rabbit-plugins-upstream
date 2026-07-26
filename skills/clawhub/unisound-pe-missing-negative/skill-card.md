## Description: <br>
Checks outpatient medical records for diagnoses whose relevant physical-examination findings are missing, then returns either no defect or a defect with the reason. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control developers and healthcare operations teams use this skill to check de-identified outpatient record text for missing physical-examination findings related to selected diagnoses. It is an assistive review aid and should not replace clinician review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical-record text is sent to the configured HiVoice MaaS endpoint and should be treated as sensitive. <br>
Mitigation: Use only de-identified records that are allowed to be sent to that endpoint, and handle outputs according to the applicable retention policy. <br>
Risk: Prepared debug files and result files can contain sensitive clinical content. <br>
Mitigation: Avoid --save-prepared unless needed for debugging, and delete generated files when they are no longer required. <br>
Risk: The skill provides assistive quality-control findings, not medical diagnosis or treatment advice. <br>
Mitigation: Have a licensed clinician review final conclusions before relying on them in clinical workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-pe-missing-negative) <br>
- [HiVoice MaaS chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, guidance] <br>
**Output Format:** [UTF-8 plain text: either 无缺陷 or 有缺陷 followed by a reason.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes the quality-control result to an output file; optional preprocessing can save prepared text for debugging.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
