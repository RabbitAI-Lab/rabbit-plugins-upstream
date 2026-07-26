## Description: <br>
Analyzes close-up aquarium camera media to estimate fish gill opening and closing respiratory rate, flag abnormal respiration or hypoxia warnings, and return structured monitoring reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aquarium owners, aquaculture operators, public aquarium teams, and laboratory staff use this skill to analyze close-up fixed-camera fish videos or URLs, calculate respiratory BPM, review alert levels, and retrieve historical respiratory monitoring reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium videos or URLs may be sent to lifeemergence.com services and associated with an automatically resolved account identity. <br>
Mitigation: Use only media the operator is authorized to upload, disclose the remote processing path before deployment, and confirm report retention, deletion, and account revocation procedures. <br>
Risk: The skill may persist identity or token material locally through data/smyx-api-key.txt and shared SQLite storage. <br>
Mitigation: Run the skill in an isolated workspace, review local credential and database files before and after use, and rotate or revoke stored credentials when access is no longer needed. <br>
Risk: Respiratory alerts can influence animal-care decisions but are not veterinary diagnoses. <br>
Mitigation: Require human review of video quality, species, water temperature, and recommended actions; do not use the skill to prescribe medications or directly control aquarium equipment. <br>


## Reference(s): <br>
- [Fish respiratory rate API documentation](artifact/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Structured text or JSON analysis report, with Markdown tables for historical report listings and report export links when available] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs respiratory BPM, signal stability, abnormal respiration classification, alert level, recommended non-medication actions, disclaimers, and links to generated report exports.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
