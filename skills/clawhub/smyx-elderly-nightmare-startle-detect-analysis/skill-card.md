## Description:

Analyzes nighttime bedroom video and audio to report startle-like movements and sounds, event timing, and frequency for elderly sleep monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Family caregivers and care teams use the skill to review possible nighttime sleep disturbances and share event summaries with a clinician; it does not provide a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bedroom video and audio can expose highly sensitive personal information.

Mitigation: Obtain the monitored person's informed consent and restrict access to recordings and reports.

Risk: Analysis is sent to configured cloud services, which may retain sensitive material.

Mitigation: Confirm the cloud provider and retention policy before use; limit retained footage to necessary short event clips.

Risk: The skill can access historical reports and silently create or reuse an internal account with locally stored tokens.

Mitigation: Require platform-controlled account identity and protect stored tokens and report access before installation.

Risk: Behavior alerts could be mistaken for a diagnosis or treatment advice.

Mitigation: Treat reports as observational data and refer concerning patterns to a sleep specialist; do not change medication based on the skill.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-elderly-nightmare-startle-detect-analysis)
- [Skill API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON analysis results or a Markdown event summary with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Event counts, timelines, and follow-up suggestions; not a medical diagnosis.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
