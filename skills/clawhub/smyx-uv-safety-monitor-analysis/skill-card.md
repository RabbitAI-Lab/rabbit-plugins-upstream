## Description:

Analyzes pet-area video for possible UV disinfection hazards and provides safety findings and recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and facility operators use this skill to analyze indoor camera footage for pets near active UV disinfection equipment and review safety alerts, recommendations, and past reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor camera footage or video URLs are sent to cloud analysis services.

Mitigation: Use only with footage you are authorized to share; review the service's retention and deletion terms before sending sensitive video.

Risk: Reports may be associated with a silently created or reused identity and persistent account tokens.

Mitigation: Review account controls and access permissions before installation or use.

Risk: Video-based UV lamp detection can be affected by ambient light and may miss a hazardous exposure.

Mitigation: Do not rely on video analysis alone to control a UV lamp; verify lamp status directly and use independent safety safeguards.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Structured report text and Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include risk alerts, recommendations, report links, and cloud report history.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
