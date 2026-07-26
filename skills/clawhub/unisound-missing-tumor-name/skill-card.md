## Description: <br>
Checks outpatient EMR text for cases where tumor or cancer history is recorded without a specific tumor name, using a HiVoice MaaS medical LLM to output no defect or defect with a reason. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Clinical quality-control reviewers and developers use this skill to check de-identified outpatient medical records for missing tumor-name detail when tumor or cancer history is present. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical record fields are sent to an external LLM endpoint. <br>
Mitigation: Use only de-identified records and confirm the configured endpoint is acceptable for privacy and compliance requirements. <br>
Risk: The required appkey could be exposed if placed in repositories, shared commands, or logs. <br>
Mitigation: Keep the appkey out of repositories and logs, and pass it through controlled runtime configuration. <br>
Risk: The --save-prepared option can store preprocessed medical record text locally. <br>
Mitigation: Avoid --save-prepared unless local storage of the prepared record text is intentional and protected. <br>
Risk: The result is a quality-control aid and may be incorrect or incomplete. <br>
Mitigation: Have a qualified clinical reviewer confirm the final quality-control conclusion. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-missing-tumor-name) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [HiVoice MaaS chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code] <br>
**Output Format:** [UTF-8 text file and console text containing "无缺陷" or "有缺陷" with a reason.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes the quality-control result to a configured output path or the default ../runs/med-emr-qc/missing-tumor-name.txt path.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence; artifact _meta.json reports 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
