## Description:

Analyzes fixed-camera home or office video to detect hand-rubbing, nail-biting, and pacing as anxiety-related behavior signals and returns behavior statistics, an anxiety-behavior index, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and mental-health support workflows can use this skill to analyze consented home, office, counseling-room, or school video for visual behavior statistics related to hand-rubbing, nail-biting, and pacing. The output is for behavior awareness and trend review, not medical diagnosis or treatment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home or office video can contain sensitive personal and mental-health-related information and may be sent to a configured cloud service.

Mitigation: Use only with explicit consent from filmed people, review the configured service and retention expectations, and prefer privacy-preserving capture such as face masking or metric-only storage where available.

Risk: Video URLs may expose third-party content or private-network resources to the analysis service.

Mitigation: Use trusted, authorized public URLs only and avoid private-network, internal, or third-party URLs.

Risk: Automatic identity creation, token persistence, and history lookup can link reports to a managed identity.

Mitigation: Review workspace data and token storage behavior before using history lookup, and run the skill in an isolated workspace when policy requires separation.

Risk: Behavior scores and alerts may be mistaken for a clinical anxiety diagnosis.

Mitigation: Present results as visual behavior statistics and self-awareness guidance only; do not use them as diagnosis, scale scoring, prescription, or treatment advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and JSON-formatted analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior counts, behavior durations, event timelines, an anxiety-behavior index, baseline comparison, self-care suggestions, and historical report links.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
