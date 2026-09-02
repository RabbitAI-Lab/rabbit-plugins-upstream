## Description:

Automatically detects smoking behavior in target areas from video streams, images, and video files, then reports detected violations and alerts for smoking-control safety management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, facility managers, and developers use this skill to analyze public-area image or video inputs for smoking behavior, produce structured detection reports, trigger violation alerts, and query cloud-hosted historical reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Smoking-detection media may be sent to a cloud service for analysis.

Mitigation: Use only with media that operators are authorized to process, document consent and retention expectations, and review service endpoints before deployment.

Risk: The skill can silently create or reuse identity context and query historical reports.

Mitigation: Limit deployment to trusted workspaces, verify report access controls, and make identity association behavior clear to operators.

Risk: Tokens or profile data may be stored locally in the workspace.

Mitigation: Review local credential storage before use, restrict filesystem access, and rotate credentials if the workspace is shared or exposed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-smoking-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Smyx Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown reports, JSON analysis payloads, report links, and optional saved text or JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports basic, standard, and json detail levels; local media inputs are documented with a 10 MB limit.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact SKILL.md frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
