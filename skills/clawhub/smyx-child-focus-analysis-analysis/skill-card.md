## Description: <br>
Analyzes child study-area video from a smart desk lamp or tabletop camera to estimate face orientation, gaze direction, fidgeting actions, per-minute focus scores, distraction periods, and low-focus alerts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, teachers, and developers can use this skill to review child study-session videos and receive visual focus metrics, distraction-event summaries, historical report tables, and report links. The results are auxiliary learning-behavior observations and do not replace direct caregiver or educator judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child study-area videos and video URLs may be sent to a configured cloud service. <br>
Mitigation: Use only media that is necessary for the task, confirm guardian or school consent before processing, and avoid unrelated or sensitive background content. <br>
Risk: Historical child-behavior reports and generated report links may expose sensitive information. <br>
Mitigation: Share report links only with authorized users and treat exported reports as sensitive records. <br>
Risk: The skill may create or reuse a local identity and store service tokens in the workspace. <br>
Mitigation: Review workspace access controls before installation and remove local identity or token data when it is no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown text with structured analysis fields, distraction-event summaries, report links, and optional JSON-style detail.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write results to a user-specified output file; historical reports are returned as a Markdown table.] <br>

## Skill Version(s): <br>
1.0.6 (source: ClawHub release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
