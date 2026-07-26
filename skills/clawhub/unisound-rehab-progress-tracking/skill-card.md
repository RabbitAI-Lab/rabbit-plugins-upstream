## Description: <br>
Tracks post-operative rehabilitation progress for patients by summarizing task completion, pain trends, functional assessment trends, phase progress, and attention items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External patient-facing rehabilitation workflows can use this skill to turn rehab task records, pain scores, and functional assessments into structured progress summaries and Markdown analysis. It is scoped to trend display and attention items, not treatment-effect judgment or replacement of clinician assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive rehabilitation data is sent to a remote medical model API. <br>
Mitigation: Use only with clear user notice, appropriate consent, and approved data-processing terms for the hivoice medical model API. <br>
Risk: Patient-facing medical-style analysis may be interpreted as clinical assessment. <br>
Mitigation: Keep outputs scoped to trend summaries and attention items, and require clinician review for treatment decisions or changes to rehabilitation plans. <br>
Risk: Document conversion and OCR support can process PDFs, office files, spreadsheets, and images. <br>
Mitigation: Run conversion in a controlled environment with trusted files and maintained optional dependencies or external tools. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-rehab-progress-tracking) <br>
- [Unisound-LLM publisher profile](https://clawhub.ai/user/unisound-llm) <br>
- [rehabilitation-analyzer progress analysis reference](https://agent-skills.md/skills/huifer/WellAlly-health/rehabilitation-analyzer) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, JSON, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [UTF-8 JSON containing structured rehab metrics and Markdown natural-language analysis] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts JSON and optional document, table, text, and image inputs; requires an app key for the remote hivoice medical model API.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
