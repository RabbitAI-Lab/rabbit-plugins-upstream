## Description: <br>
Uses visual AI on frontal face images or videos to produce structured emotion-recognition reports with intensity scores, anomaly flags, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze face images or videos for emotion categories, intensity, trends, and report history in human-computer interaction or mental-health monitoring workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends face images or videos and inferred emotion reports to a vendor cloud service. <br>
Mitigation: Use only with appropriate consent, avoid highly sensitive subjects unless necessary, and review organizational privacy requirements before deployment. <br>
Risk: History lookup and generated report links may expose sensitive emotion-analysis results. <br>
Mitigation: Restrict who can invoke history lookup, treat report links as sensitive, and avoid sharing reports outside the intended audience. <br>
Risk: The skill can create a local SQLite database and persist account tokens in the workspace data area. <br>
Mitigation: Run it in an isolated workspace when possible and review or clear local data before sharing the environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API reference](references/api_doc.md) <br>
- [SMYX analysis API reference](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON reports with optional Markdown tables for history lookup] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include emotion scores, anomaly markers, recommendations, and report links.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
