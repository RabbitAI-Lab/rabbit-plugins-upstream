## Description:

Analyzes outdoor sports videos for possible injuries and health risks, producing safety reports and alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event safety teams and organizers use video or image inputs to assess potential injuries, physical distress, posture, and environmental risks during outdoor sports events and to retrieve earlier reports. Results support, but do not replace, medical judgment or emergency care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports videos, images, URLs, and report queries are sent to external lifeemergence.com services.

Mitigation: Review the service and obtain consent before submitting sensitive participant footage or report queries.

Risk: The skill can silently create or reuse an identity and store account tokens in plaintext in the workspace data directory.

Mitigation: Run only in an approved isolated workspace; restrict access to stored tokens and review identity creation before installation.

Risk: Video-based health risk reports may be mistaken for medical diagnosis or urgent-care decisions.

Mitigation: Treat results as safety guidance only; seek qualified medical help immediately for suspected emergencies.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Sports analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured risk report or Markdown table of historical reports, with report links; optional JSON output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Risk observations, recommendations, and links to reports when available]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
