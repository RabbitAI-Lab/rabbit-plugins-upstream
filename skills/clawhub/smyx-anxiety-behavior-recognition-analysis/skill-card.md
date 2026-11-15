## Description:

Using a fixed camera at home or in the office, the system analyzes daily videos of an individual (e.g., adult, adolescent) and detects anxiety-related behaviors: hand rubbing (repeated rubbing of both hands), nail biting (hand approaching mouth with biting motion), and pacing (repeated back-and-forth walking in a small area).

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals can use the skill to review visible hand rubbing, nail biting, and pacing in fixed-camera footage, while counselors can use its summaries to support discussion of behavior patterns. It reports observed counts, durations, trends, and gentle self-awareness reminders; it does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video may be sent to an external service for analysis.

Mitigation: Obtain the subject's consent and confirm remote processing is acceptable before submitting footage; use the documented silhouette and face-mosaic protections for privacy-sensitive scenes.

Risk: Broad triggers, automatic account creation, and local credential storage may cause unexpected processing or associate history with a shared identity.

Mitigation: Review each run and its account association, protect access to locally stored credentials, and confirm report ownership before retrieving history.

Risk: A mode described as not analyzing video may still process the footage.

Mitigation: Treat that mode as active video processing until verified, and do not submit sensitive footage when processing is unacceptable.

## Reference(s):

- [API and behavior reference](references/api_doc.md)
- [Analysis API error codes](skills/smyx_analysis/references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior summaries and trends, with Markdown history tables, self-awareness reminders, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes behavior counts and durations and an anxiety-behavior index (0–100); visual behavior indicators are not a clinical diagnosis.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
