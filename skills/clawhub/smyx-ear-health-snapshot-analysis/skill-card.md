## Description: <br>
Analyzes pet ear or head-shaking/scratching media and returns visual observations about ear-canal redness, discharge, earwax accumulation, abnormality alerts, and non-diagnostic care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External pet owners, boarding-center staff, and veterinary intake teams use this skill to analyze pet ear media, review structured visual observations, and decide whether further owner check-up or veterinary attention is warranted. It is intended for health monitoring and pre-screening, not for medical diagnosis or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media or URLs may be sent to the provider's cloud service for analysis. <br>
Mitigation: Review data handling expectations before installation and avoid submitting media unless cloud processing is acceptable for the deployment. <br>
Risk: The skill can automatically create or reuse a local identity and store tokens in a workspace SQLite database. <br>
Mitigation: Run the skill in an appropriate workspace, protect local storage, and review token handling before use with sensitive accounts. <br>
Risk: Report-history requests can fetch prior cloud reports with limited user control. <br>
Mitigation: Limit use of history-query language to contexts where cloud report retrieval is expected and appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown report or JSON details, depending on requested detail level] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and history tables; visual findings are not medical diagnoses.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; SKILL.md frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
