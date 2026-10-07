## Description:

Analyzes fixed-camera video for hand rubbing, nail biting, and pacing, and returns behavior statistics and self-awareness guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and counselors use this skill to review video-based patterns of hand rubbing, nail biting, and pacing for self-awareness and follow-up; its output is not a clinical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive home or office video and anxiety-behavior reports are sent to configured cloud services.

Mitigation: Obtain informed consent from everyone recorded and confirm service account, privacy, and retention terms before upload.

Risk: Report history is linked to a cloud identity with local token storage and limited user control.

Mitigation: Avoid history lookup until identity, stored tokens, and remote reports can be deleted or reset as needed.

Risk: Observed behaviors and the anxiety-behavior index may be mistaken for a diagnosis.

Mitigation: Treat results as self-awareness cues, not a diagnosis or treatment recommendation; seek qualified clinical assessment when needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured behavior report or historical report list]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior counts, an anxiety-behavior index, self-care suggestions, and report links.]

## Skill Version(s):

1.0.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
