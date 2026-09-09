## Description:

Detects whether anyone has fallen within a target area, supports video stream analysis, and is suitable for real-time safety monitoring of elderly people living alone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and safety-monitoring operators use this skill to analyze local or network video for possible fall events, receive structured detection results, and query historical fall-detection reports. The results are safety alerts and should be confirmed by a person before emergency or care decisions are made.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private monitoring media and historical report queries are sent to external services.

Mitigation: Review the provider's data handling, retention, and access controls before using real home-monitoring footage.

Risk: The skill can create or reuse internal identities and stores credentials locally.

Mitigation: Run only in an approved environment, isolate credentials, and rotate or remove locally stored tokens when testing is complete.

Risk: The evidence reports plaintext development API endpoints.

Mitigation: Remove development HTTP configuration and require production HTTPS endpoints before deployment with sensitive footage.

Risk: The security guidance flags unrelated payment-skill installation instructions in API error handling.

Mitigation: Review and remove unrelated billing or payment guidance before publishing or installing the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fall-detection-video-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Fall Detection Video Analysis API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured analysis results, report links, and optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May call external provider APIs to analyze videos or retrieve historical reports.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
