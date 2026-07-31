## Description: <br>
Predicts expected yield of economic crops such as tomato, corn and potato by combining growth stage, nutrition status, environmental data and historical yield references. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze crop images, videos, or URLs and produce yield estimates, confidence information, influence factors, and report links for harvest planning, market matching, supply chain planning, and agricultural insurance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Crop images, videos, URLs, and identity data may be sent to lifeemergence.com services for processing. <br>
Mitigation: Use only non-sensitive crop media and review network processing requirements before installation or execution. <br>
Risk: The skill may automatically create or reuse a local account identity and read data/smyx-api-key.txt when present. <br>
Mitigation: Run the skill in an isolated workspace and avoid placing unrelated credentials in the workspace data directory. <br>
Risk: Authentication tokens may be stored in a workspace SQLite database. <br>
Mitigation: Restrict workspace access, rotate credentials if exposed, and remove the local database when the skill is no longer trusted or needed. <br>


## Reference(s): <br>
- [API 接口文档](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crop-yield-prediction-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, JSON, files, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON text, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include structured crop-yield analysis, expected yield range, confidence, influence factors, historical report listings, and report links.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
