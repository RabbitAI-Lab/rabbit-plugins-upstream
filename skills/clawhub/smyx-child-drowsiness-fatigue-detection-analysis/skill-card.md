## Description:

Analyzes a child's face in video for visual signs of drowsiness and returns fatigue metrics, a score, and rest guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Teachers and parents can review video-based signs of drowsiness during study or class and use the report to inform decisions about offering a break. The results are visual fatigue estimates, not a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Children's recordings are sent to LifeEmergence, and the no-analysis option is not yet safe to rely on.

Mitigation: Delay use of recordings until the no-analysis behavior is fixed; obtain consent for remote processing, confirm retention and deletion terms, and verify the actual destination because --api-url does not change it.

Risk: Account credentials may not be adequately protected.

Mitigation: Confirm credential storage and protection before connecting an account.

Risk: Provider-side storage and access controls, as well as analysis accuracy, remain unverified.

Mitigation: Treat fatigue results as advisory and confirm provider storage and access controls before sending recordings.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis results, JSON, Markdown]

**Output Format:** [Structured JSON analysis report; Markdown table for history results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include fatigue metrics and score, fatigue level, drowsiness events, a rest prompt, summary, and report link.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
