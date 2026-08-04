## Description: <br>
Identifies likely plant leaf diseases from leaf images or videos by analyzing lesion features and returning structured diagnosis results with confidence scores and general care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to analyze plant leaf media for likely disease type, symptom features, confidence scoring, structured reports, and report-history lookup. It is aimed at plant factories, greenhouses, home gardening, horticulture, and farm inspection workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded plant images or videos are sent to the publisher's cloud service. <br>
Mitigation: Do not submit sensitive media or private/internal URLs unless the publisher and retention model are trusted. <br>
Risk: Report history is associated with an automatically managed identity, and auth tokens may be stored in a workspace SQLite database. <br>
Mitigation: Review identity handling and token storage before installation; isolate the workspace when using untrusted or sensitive data. <br>
Risk: AI plant-disease outputs can be uncertain and are not a substitute for expert diagnosis or regulated treatment advice. <br>
Mitigation: Use results as preliminary guidance and consult a plant pathology or local agricultural expert before acting on severe cases or applying treatments. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-plant-leaf-disease-identification-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Structured JSON or Markdown text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include disease labels, symptom features, confidence scores, general care guidance, and cloud report export links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
