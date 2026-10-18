## Description:

Analyzes aquatic pet videos or video URLs through a remote service and returns health findings, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium enthusiasts and caretakers use this skill to assess visible health concerns in fish and other aquatic pets from video and review current or historical health reports. Its findings are informational and do not replace a veterinarian's diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted aquarium media or URLs are processed by a remote service.

Mitigation: Only submit material you are comfortable sharing with the service; review the publisher and service before installing.

Risk: The skill automatically associates work with an internal identity and may create or reuse local account and token records when accessing report history.

Mitigation: Review local credential storage and access to past reports before use; install only if you trust the publisher.

Risk: Video-based health findings can be incomplete or mistaken.

Mitigation: Treat results as informational and consult an aquatic veterinarian for diagnosis or treatment decisions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured health report with optional JSON and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports report-detail options, historical report listings, and optional file output.]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata; bundled SKILL.md states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
