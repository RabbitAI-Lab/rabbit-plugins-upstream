## Description: <br>
Provides patient-side chronic disease abnormal indicator alerts using caller-supplied thresholds for measurements such as blood glucose, blood pressure, and heart rate. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Healthcare product teams and chronic-care workflow builders use this skill to flag abnormal patient measurements, explain threshold-based alert reasons, and generate follow-up guidance for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medical measurements and extracted document text may be sent to an external LLM service. <br>
Mitigation: Confirm users understand the disclosure, minimize submitted health data, and prefer structured JSON or CSV inputs over rich medical documents unless necessary. <br>
Risk: Generated causes, severity language, and recommendations may be incorrect or clinically inappropriate. <br>
Mitigation: Require human clinical review before relying on the generated analysis, and keep the skill framed as alerting support rather than diagnosis or treatment. <br>
Risk: Broad document and image input support can expose more sensitive content than needed for an indicator alert. <br>
Mitigation: Use narrow input files containing only the required indicator fields, and avoid uploading PDFs, office documents, or images unless their contents have been reviewed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-abnormal-indicator-alert) <br>
- [Open Wearables](https://openwearables.io/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [UTF-8 JSON containing structured alert data plus Markdown natural-language analysis.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a caller-provided appkey, caller-supplied threshold_profile values, and may send medical measurements or extracted document text to the named external medical LLM service.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
