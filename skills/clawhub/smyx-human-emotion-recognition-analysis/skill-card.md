## Description:

Analyzes face images and videos for emotional states, intensity, and unusual emotion markers, and retrieves past analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can analyze face photos or videos for emotion feedback and review historical reports. Results are informational and should not be used as a mental-health diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos or URLs and emotion reports are sent to a cloud service and may contain sensitive personal information.

Mitigation: Review the service's privacy and retention terms before use; avoid regulated or highly sensitive media unless those terms are acceptable.

Risk: The skill silently creates or reuses a local identity and stores authentication tokens in a workspace database.

Mitigation: Use a dedicated workspace and restrict access to its stored data and tokens.

Risk: Emotion findings may be mistaken for a mental-health diagnosis.

Mitigation: Treat results as informational only and seek qualified professional advice for persistent concerns.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-human-emotion-recognition-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Structured emotion analysis report or Markdown report list; optional JSON result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include emotion scores, unusual emotion markers, and report links.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
