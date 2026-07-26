## Description: <br>
Helps patients view an existing post-operative rehabilitation plan by organizing the current phase, goals, tasks, precautions, and a patient-facing summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients and care-plan applications use this skill to view an existing post-operative rehabilitation plan, summarize the current phase and tasks, and provide plan context to related recovery workflows. It does not create new rehabilitation prescriptions or replace guidance from a rehabilitation professional. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rehabilitation-plan content may contain sensitive health information and is sent to a remote medical-model API. <br>
Mitigation: Use the skill only when the endpoint is approved for the data involved and users understand that plan content is transmitted for model inference. <br>
Risk: Broad PDF, Office, spreadsheet, text, and image input support can invoke native converters or OCR on untrusted files. <br>
Mitigation: Prefer JSON input when possible and sandbox document conversion for untrusted PDF, Office, spreadsheet, or image files. <br>
Risk: Command-line appkeys are sensitive credentials. <br>
Mitigation: Handle appkeys as secrets and avoid exposing them in shell history, logs, or shared command examples. <br>
Risk: Generated rehabilitation summaries could be mistaken for new medical instructions. <br>
Mitigation: Use the output as a view of an existing plan and keep professional rehabilitation guidance as the authority for care decisions. <br>


## Reference(s): <br>
- [CareKit](https://github.com/carekit-apple/CareKit) <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-rehab-plan-view) <br>
- [Publisher profile](https://clawhub.ai/user/unisound-llm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON] <br>
**Output Format:** [UTF-8 JSON containing structured plan data and Markdown patient-facing text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes plan_id, current_phase, phase_goal, task_summary, precautions, and generated text.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
