## Description: <br>
病人端术后康复今日康复任务。参考 CareKit 的 daily tasks/scheduling 部分，构建日常康复执行任务能力。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and care-workflow builders use this skill to turn an existing post-operative rehabilitation plan into the current day's task list, completion summary, and patient-facing reminders. It is intended to display and record scheduled tasks, not to adjust rehabilitation intensity or create a rehabilitation plan. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical rehabilitation task details may be sent to the configured remote medical-model API. <br>
Mitigation: Use only with appropriate consent, privacy review, and appkey handling, and avoid sending real patient data unless the deployment has approved the remote processing path. <br>
Risk: Broad parsing of PDFs, Office files, spreadsheets, text, and images can expose the runtime to untrusted document content. <br>
Mitigation: Prefer JSON inputs for routine use, and sandbox or separately approve document and OCR parsing before enabling untrusted files. <br>
Risk: The scanner guidance flags use in real patient or regulated healthcare settings for review. <br>
Mitigation: Require clinical, security, and compliance review before installing in patient-facing or regulated healthcare workflows. <br>


## Reference(s): <br>
- [CareKit](https://github.com/carekit-apple/CareKit) <br>
- [ClawHub Skill Page](https://clawhub.ai/unisound-llm/skills/unisound-today-rehab-task) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Guidance] <br>
**Output Format:** [UTF-8 JSON containing structured task data and Markdown patient-facing reminder text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill filters supplied rehab tasks by date, summarizes completion status, and uses a configured remote medical-model API when tasks are present.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
