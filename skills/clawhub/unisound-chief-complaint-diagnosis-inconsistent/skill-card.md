## Description: <br>
Checks whether the body location in a Chinese outpatient record's chief complaint is inconsistent with the preliminary diagnosis, then returns no defect or a defect reason. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control teams and developers use this skill to screen de-identified outpatient EMR text for one documented consistency rule before clinician review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical record text is sent to the configured HiVoice MaaS or compatible endpoint. <br>
Mitigation: Use the skill only where that processing is authorized, and de-identify records before submission. <br>
Risk: Output files and optional prepared-text files can contain sensitive healthcare data. <br>
Mitigation: Store outputs in protected locations and avoid --save-prepared except for controlled debugging. <br>
Risk: The default timeout can wait indefinitely during an external model call. <br>
Mitigation: Set a finite timeout for production runs. <br>
Risk: The result is an auxiliary quality-control signal, not a medical diagnosis or treatment recommendation. <br>
Mitigation: Require final review by an appropriately qualified clinician. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-chief-complaint-diagnosis-inconsistent) <br>
- [HiVoice MaaS chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [UTF-8 plain text result: no defect, or defect plus a reason.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes the quality-check result to a configured output path; prepared input text is only saved when --save-prepared is used.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
