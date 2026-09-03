## Description:

Analyzes fixed-camera home or office video to identify hand-rubbing, nail-biting, and pacing behaviors, then returns behavior counts, durations, an anxiety-behavior index, and self-care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, counselors, and developers can use this skill to review fixed-camera video for anxiety-related behavioral indicators and trend-oriented self-awareness reports. It is positioned as visual behavior monitoring and does not provide diagnosis, clinical scale scoring, medication advice, or treatment plans.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private home, office, school, or counseling-room video may be processed by remote services.

Mitigation: Use only with explicit informed consent from recorded people, avoid unnecessary third-party sharing, and confirm that external processing is acceptable for the setting.

Risk: Anxiety-related behavior scores can be misunderstood as a medical diagnosis or clinical assessment.

Mitigation: Present outputs as visual behavior statistics and self-awareness prompts only; do not equate high index values with an anxiety disorder diagnosis or treatment recommendation.

Risk: Local identity and token persistence can create continuing account linkage across sessions.

Mitigation: Review local storage behavior before deployment, restrict workspace access, and clear stored identity or token data when account continuity is not intended.

Risk: Common movements such as warming hands, eating, or walking to retrieve objects can be confused with anxiety-related behavior.

Mitigation: Interpret results with scene context and longer time windows, and avoid alerts based on isolated brief events.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown summaries and JSON-style structured analysis results, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, historical-report tables, behavior timelines, anxiety-behavior index values, and self-care suggestions.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
