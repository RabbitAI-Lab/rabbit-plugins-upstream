## Description: <br>
Detects estrus behavior in female livestock from continuous barn videos, including mounting acceptance, standing reflex, restlessness, appetite drop, and vulva changes, and outputs an estrus recognition result with an optimal mating time window. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Farm operators, livestock reproduction specialists, and developers use this skill to submit barn images, videos, or URLs for estrus behavior detection. It returns structured recognition results, observed behavior lists, estrus-stage assessment, an optimal mating-time window, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Barn video files or submitted media URLs can be sent to Lifeemergence cloud services for analysis. <br>
Mitigation: Use the skill only when cloud processing is acceptable, and avoid private or signed media URLs unless sharing them with the backend service is intended. <br>
Risk: The skill can silently create or reuse an internal identity and store account tokens in the local workspace database. <br>
Mitigation: Review workspace data and database access before installation, and clear stored identity or token data before sharing the workspace. <br>
Risk: History queries can retrieve cloud report records tied to the current identity. <br>
Mitigation: Verify the active identity and workspace before running report-list actions, and restrict access to generated report outputs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-estrus-mating-behavior-detect-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with JSON-style structured results and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May upload local media or submit media URLs to Lifeemergence cloud APIs; history queries return report records tied to the current identity.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter is 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
