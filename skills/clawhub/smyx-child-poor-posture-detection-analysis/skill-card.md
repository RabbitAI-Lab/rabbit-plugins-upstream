## Description: <br>
Analyzes child study-area video to estimate posture angles, detect hunching or head tilt, generate reminder text, and return structured posture reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and product teams can use this skill to analyze local or URL-based study-area videos for child posture monitoring workflows. It returns posture metrics, poor-posture classifications, voice-reminder text, session summaries, and report links for guardian-facing review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Child study-area videos, generated reports, and report history may be processed by configured cloud services. <br>
Mitigation: Confirm guardian consent, retention and deletion handling, and report-link access controls before use. <br>
Risk: The skill silently creates or reuses a persistent identity and stores related tokens locally. <br>
Mitigation: Use an appropriate workspace or account boundary, review local token storage, and rotate or delete stored credentials when access should end. <br>
Risk: Visual posture estimates can be inaccurate and are not a medical assessment. <br>
Mitigation: Present outputs as posture habit reminders only and route health concerns to qualified medical professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis) <br>
- [Primary API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Markdown text with structured JSON-style analysis content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include posture metrics, poor-posture type, duration, voice reminder text, event timestamps, snapshots, session summaries, and historical report records.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
