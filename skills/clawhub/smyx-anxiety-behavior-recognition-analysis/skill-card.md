## Description:

Using a fixed camera at home or in the office, the system analyzes daily videos of an individual (e.g., adult, adolescent) and detects anxiety-related behaviors: hand rubbing (repeated rubbing of both hands), nail biting (hand approaching mouth with biting motion), and pacing (repeated back-and-forth walking in a small area).

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals, counselors, and care teams can use this skill to review fixed-camera video for hand-rubbing, nail-biting, and pacing patterns, then view behavior counts, duration, trends, and self-care prompts. The results are for behavioral self-awareness and should not be treated as a mental health diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared accounts can mix sensitive reports between users.

Mitigation: Avoid shared-user deployments until sender isolation is fixed.

Risk: Export-only mode still runs analysis, and configured API secrets are mishandled.

Mitigation: Avoid private footage until export-only handling and API-secret handling are fixed.

Risk: Video can contain sensitive information about people, including adolescents.

Mitigation: Get informed consent from everyone depicted and review the service's retention policy before uploading.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior report with JSON data and Markdown summaries or report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include behavior counts and duration, an anxiety-behavior index, event timeline, baseline comparison, and self-care suggestions.]

## Skill Version(s):

1.0.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
