## Description: <br>
Analyzes office workstation images or video to estimate sitting duration and posture metrics, then produces prolonged-sitting and posture warning reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, workplace health teams, and developers use this skill to analyze office workstation footage for prolonged sitting, forward-head posture, back curvature, shoulder asymmetry, and screen-distance warnings. It returns visual posture and activity monitoring results with directional health reminders, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads sensitive workplace video to a cloud service. <br>
Mitigation: Use only where employees have been notified and consented, and where organizational policy allows the named cloud service, retention, and access controls. <br>
Risk: The skill silently manages persistent identity, tokens, and cloud report history access. <br>
Mitigation: Review identity and token storage before installation, limit access to approved operators, and avoid exposing internal identifiers in user-facing output. <br>
Risk: Network video URLs can send third-party or sensitive footage to the analysis service. <br>
Mitigation: Use trusted video sources that the organization controls and avoid arbitrary third-party URLs unless source ownership and retention rules are clear. <br>
Risk: Posture warnings could be mistaken for medical advice. <br>
Mitigation: Present results as visual posture and activity reminders only, and direct users with pain or medical concerns to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-office-worker-posture-warning-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON text containing structured posture metrics, warning labels, reminders, history lists, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include exported report image links and cloud history query results.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
