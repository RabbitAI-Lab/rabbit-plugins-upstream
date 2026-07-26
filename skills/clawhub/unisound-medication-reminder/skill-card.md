## Description: <br>
Generates medication reminder schedules for chronic disease management from structured medication details or parsed document inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients, caregivers, and health-management workflows use this skill to turn medication names, doses, frequencies, reminder times, and active date ranges into a three-day reminder plan. It only formats reminder information and does not judge medication suitability, adjust prescriptions, or provide clinical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends medication details and parsed document contents to a remote medical model endpoint. <br>
Mitigation: Use it only when users are comfortable sharing that information with the configured endpoint, and avoid sending unnecessary personal or clinical details. <br>
Risk: Broad document parsing for Office, PDF, spreadsheet, text, and image inputs can expose sensitive file contents or process untrusted files. <br>
Mitigation: Prefer JSON or simple text from trusted sources, and isolate runtime processing before using untrusted Office, PDF, or image files. <br>
Risk: Generated text may be mistaken for medical advice. <br>
Mitigation: Treat output as reminder formatting only, and rely on qualified medical professionals for medication decisions or prescription changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-medication-reminder) <br>
- [MedTimer reference app](https://f-droid.org/en/packages/com.futsch1.medtimer/) <br>
- [Remote medical model endpoint](https://maas-api.hivoice.cn/v1/chat/completions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration] <br>
**Output Format:** [UTF-8 JSON with structured reminder data and Markdown reminder text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey for the remote medical model and supports optional parsed document inputs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
