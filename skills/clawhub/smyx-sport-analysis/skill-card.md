## Description:

Conducts video safety risk analysis for participants in outdoor sports competitions, long-distance running, marathons, etc.; identifies sports injuries and sudden health risks, outputs professional analysis reports, and provides timely warnings to ensure sports safety.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Event operations teams, medical support staff, and agents use this skill to analyze outdoor sports videos for falls, injuries, physical distress, posture issues, environmental hazards, and historical risk reports. Its outputs are safety-reference reports and alerts, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says this version can send media and credentials over insecure HTTP.

Mitigation: Review before installation and do not use with private videos or real user identities until HTTPS is the default and development endpoints are removed.

Risk: The security evidence says the skill silently manages identity and can store reusable tokens in a local workspace database.

Mitigation: Use only test identities until identity flows are disclosed, gated, and token storage is reviewed or removed.

Risk: The skill produces sports safety guidance that could be mistaken for medical judgment.

Mitigation: Treat reports as safety-reference material and require professional medical review for injuries, distress, or emergency response decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sport-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with structured JSON analysis results and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, analysis-type selection, historical report listing, and optional output file writing.]

## Skill Version(s):

1.0.13 (source: server release evidence; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
