## Description:

Analyzes images and video for smoking behavior in public spaces and provides detection reports, alerts, and management suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Facility and community managers use this skill to review images or video for potential smoking violations, receive alerts, and consult historical detection reports. Detection results support human decisions rather than serving as sole evidence for enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or media URLs are sent to a cloud service, where media and report history may be retained.

Mitigation: Use only approved media; confirm who operates the service, its retention policy, and how to delete stored media and reports before installation.

Risk: The skill manages identity internally and stores tokens locally, which could expose linked report history if the device or credentials are compromised.

Mitigation: Restrict access to the local account and token storage; confirm how identity, report access, and local account deletion are handled.

Risk: Automated smoking detections could be mistaken for confirmed violations.

Mitigation: Have a person review detections and follow local policies before taking action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured detection report or JSON; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, alerts, recommendations, and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
