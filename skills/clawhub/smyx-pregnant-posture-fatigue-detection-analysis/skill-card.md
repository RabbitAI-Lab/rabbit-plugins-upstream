## Description:

Analyzes home-camera footage for prolonged standing and frequent bending during pregnancy, and produces fatigue-risk reminders and reports for health reference rather than diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Expectant families and developers of pregnancy-support applications use this skill to review posture and activity in home-camera footage, receive rest reminders, and consult previous analysis reports. Results are health guidance, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive pregnancy-camera footage and report history are sent to a cloud service.

Mitigation: Obtain the pregnant person's explicit consent before sending footage or retrieving reports.

Risk: A persistent local user identity and stored tokens may expose personal reports in shared workspaces.

Mitigation: Avoid shared workspaces unless the local user database and stored tokens are understood and protected.

Risk: Broad history queries may reveal more personal reports than intended.

Mitigation: Request report history explicitly and limit queries to the needed scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pregnant-posture-fatigue-detection-analysis)
- [API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Structured analysis report and plain-language reminders]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include posture metrics, fatigue alerts, suggested rest actions, and report links; not a medical diagnosis.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
