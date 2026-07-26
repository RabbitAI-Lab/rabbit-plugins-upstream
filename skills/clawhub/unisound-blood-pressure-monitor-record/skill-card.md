## Description: <br>
Records patient blood pressure measurements for chronic disease management, structures systolic pressure, diastolic pressure, heart rate, measurement time, and notes, and returns a brief Markdown analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to capture blood pressure readings from JSON, text, tables, documents, PDFs, or images and produce standardized health-record JSON. The skill also calls a remote medical model to generate patient-facing Markdown interpretation, reminders, and lifestyle guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive health measurements, timestamps, heart rate, and notes are sent to a remote medical model API. <br>
Mitigation: Use non-sensitive test data unless the publisher provides acceptable consent, retention, privacy, and remote-processing terms. <br>
Risk: The skill produces patient-facing analysis and lifestyle guidance from blood-pressure records. <br>
Mitigation: Review outputs before clinical use and do not treat the skill as a substitute for professional medical advice. <br>
Risk: Optional document, spreadsheet, PDF, and image inputs require local parsers or OCR tools. <br>
Mitigation: Process only trusted files in a controlled environment and install optional dependencies only when needed for those input formats. <br>


## Reference(s): <br>
- [HealthLog](https://healthlog.dev/) <br>
- [ClawHub release page](https://clawhub.ai/unisound-llm/skills/unisound-blood-pressure-monitor-record) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Text] <br>
**Output Format:** [UTF-8 JSON with structured blood-pressure data and a Markdown natural-language text field] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an appkey for the remote u2-med medical model API; optional prepared JSON can be saved for debugging.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
