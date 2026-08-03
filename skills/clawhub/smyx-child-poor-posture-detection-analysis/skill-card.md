## Description: <br>
Analyzes child study-area images or video to estimate posture metrics such as Cobb angle and head tilt, produce structured posture results, and generate reminder text when poor posture persists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and product teams can use this skill to add child posture monitoring, reminder generation, and history-report lookup workflows to smart desk lamps, study desks, or classroom monitoring products. Results are visual posture estimates for habit reminders, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sensitive child posture video or image data to cloud services for analysis. <br>
Mitigation: Install and use only after confirming guardian consent, cloud upload terms, retention and deletion controls, and appropriate handling of child video data. <br>
Risk: History queries and report links may expose child posture reports or account-bound records. <br>
Mitigation: Confirm report-link access controls and account authorization before using history lookup or sharing generated report links. <br>
Risk: The skill silently manages persistent user or account state. <br>
Mitigation: Verify where identifiers, tokens, and posture reports are stored before deployment, and avoid real child videos until privacy and authorization controls are clear. <br>
Risk: Posture angles are visual estimates and may be wrong or incomplete. <br>
Mitigation: Use outputs for posture habit reminders only, and do not treat them as medical diagnosis or scoliosis assessment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-poor-posture-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown text with structured JSON-style analysis, voice reminder text, history-report lists, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export links and posture metrics such as estimated Cobb angle, head tilt, shoulder offset, and eye-to-desk distance.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
