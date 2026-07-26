## Description: <br>
Generates chronic-disease follow-up reminders, overdue status, and next-step suggestions from visit dates, follow-up intervals, disease type, and notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients, care managers, or workflow operators use this skill to calculate follow-up dates, identify overdue visits, and produce reminder guidance for chronic-disease follow-up workflows. It supports reminder workflows and does not replace clinician scheduling, diagnosis, or clinical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive patient follow-up details and free-text notes are sent to a remote medical model endpoint. <br>
Mitigation: Use minimal structured inputs, avoid uploading full medical records unless necessary, and confirm privacy and consent requirements before use. <br>
Risk: Broad document and OCR ingestion can expose more patient information than the reminder task requires. <br>
Mitigation: Prefer JSON or concise key-value inputs and review extracted text before sending it to the remote model. <br>
Risk: Generated reminder text could be mistaken for clinical advice. <br>
Mitigation: Review generated text before relying on it and keep the skill limited to follow-up reminders rather than diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-followup-reminder) <br>
- [Simple app features: appointments and overdue patients](https://docs.simple.org/readme/simple-app-features) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [UTF-8 JSON containing structured reminder fields and Markdown natural-language text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey and sends prepared patient follow-up data to the configured remote u2-med chat completions endpoint.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
