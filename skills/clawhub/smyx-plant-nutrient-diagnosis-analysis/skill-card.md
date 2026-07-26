## Description: <br>
Diagnoses likely plant nutrient deficiencies from leaf images or videos, returning structured findings, confidence scores, fertilization direction guidance, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and gardening or agriculture operators use this skill to analyze plant leaf media for likely nutrient deficiencies and retrieve prior diagnosis reports. It supports smart planters, home gardening, greenhouses, and plant factory workflows where users need diagnostic guidance without exact fertilizer concentration recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads plant media and report metadata to the publisher's remote service. <br>
Mitigation: Use only with media that may be shared with the publisher's service, and avoid sensitive workspace or personal data in inputs. <br>
Risk: The skill can create or reuse a local account identity and store tokens or report context in the workspace. <br>
Mitigation: Review token storage and user separation before using it in shared workspaces. <br>
Risk: Historical report retrieval can be triggered automatically and may expose prior report data. <br>
Mitigation: Review who can invoke history queries and confirm the workspace is appropriate for report retrieval. <br>
Risk: Nutrient deficiency symptoms can overlap with plant disease or multiple simultaneous deficiencies. <br>
Mitigation: Treat results as reference guidance and combine them with plant context, soil testing, and qualified agricultural advice. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrient-diagnosis-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON structured diagnosis report with confidence scores, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report to a user-specified output file.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
