## Description:

Analyzes fixed-camera home, office, counseling-room, or school video to detect hand rubbing, nail biting, and pacing, then reports behavior counts, durations, trends, and a non-diagnostic anxiety-behavior index.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Users, caregivers, and counselors can use this skill to turn consented fixed-camera video into structured behavior statistics and self-care prompts. It is positioned as visual behavior monitoring support, not as medical diagnosis, clinical scoring, or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes sensitive camera and mental-health-related video.

Mitigation: Use only with clear consent from every recorded person, avoid workplace, school, private, or health-related footage without appropriate authorization, and retain only the minimum necessary derived metrics.

Risk: Server evidence reports unsafe default transport for sensitive uploads and report retrieval.

Mitigation: Do not use shipped defaults until endpoints are HTTPS-only, allowlisted, and reviewed for secure upload, token, identity, and report-link handling.

Risk: Persistent identity, token, upload, report-link, and history handling may expose sensitive behavioral data.

Mitigation: Require a documented data-retention and deletion process, protect credentials, and confirm who can access generated reports before deployment.

Risk: Behavior recognition can confuse ordinary movements with anxiety-related behavior or be misread as a diagnosis.

Mitigation: Present results as visual behavior indicators only, combine short events with context and trends, and avoid diagnostic, medication, or treatment claims.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured text or Markdown report, with JSON available through the command-line detail setting]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior event counts, durations, an anxiety-behavior index, trend comparison, self-care suggestions, and report links.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
