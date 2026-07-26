## Description: <br>
Helps manage long-term personal medication records by parsing medication inputs, organizing active and stopped medicines, and generating a medication summary. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patients, caregivers, and health application operators use this skill to turn medication records from JSON, tables, text, documents, or images into structured medication lists and a Markdown medication-management summary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medication records, notes, and parsed medical document content may be sent to a remote model API. <br>
Mitigation: Use only when users understand and authorize that transfer, minimize inputs to the needed medication fields, and avoid uploading full medical documents unless necessary. <br>
Risk: Generated medication summaries may be mistaken for clinical advice or used for medication changes. <br>
Mitigation: Treat the output as record-management support only and require users to consult a qualified clinician before changing medication use. <br>
Risk: Prepared JSON or output files can store sensitive medication information locally. <br>
Mitigation: Write outputs only to secured locations and manage review, retention, and deletion according to the user's health-data handling requirements. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-medication-record-management) <br>
- [MedTimer reference app](https://f-droid.org/en/packages/com.futsch1.medtimer/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Configuration, Guidance] <br>
**Output Format:** [UTF-8 JSON containing structured data and Markdown text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an app key for the configured HiVoice MaaS medical model endpoint; optional preprocessing can save prepared JSON when requested.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
