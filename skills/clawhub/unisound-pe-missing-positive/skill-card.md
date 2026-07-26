## Description: <br>
Checks outpatient medical records for cases where the physical examination appears to omit major positive signs related to the diagnosis, using a configured HiVoice MaaS-compatible medical LLM. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and clinical quality-control teams use this skill to run a focused outpatient EMR check for missing diagnosis-related positive physical-exam signs. It reads de-identified record text or supported document formats, calls the configured medical LLM endpoint, and returns a local QC result for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Clinical text may be sent to the configured HiVoice MaaS or compatible endpoint. <br>
Mitigation: Use only de-identified records, confirm the endpoint is approved for the deployment environment, and review any custom base URL before execution. <br>
Risk: The appkey used for LLM access is a sensitive credential. <br>
Mitigation: Provide the appkey at runtime, keep it out of repositories and logs, and rotate it if exposure is suspected. <br>
Risk: Prepared text and QC outputs can contain clinical information when saved locally. <br>
Mitigation: Avoid saving prepared text unless local plaintext storage is acceptable, and protect generated output files according to clinical data handling requirements. <br>
Risk: The LLM-assisted QC result can be incomplete or incorrect. <br>
Mitigation: Treat results as quality-control assistance only and require review by qualified clinical staff before relying on conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-pe-missing-positive) <br>
- [HiVoice MaaS compatible chat completions endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, files, shell commands, guidance] <br>
**Output Format:** [UTF-8 plain text written locally and echoed to the console] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The QC result is either no defect or defect with a reason; optional preprocessing can save prepared clinical text locally.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
