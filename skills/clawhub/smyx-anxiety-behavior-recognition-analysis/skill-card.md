## Description:

Analyzes camera video for hand-rubbing, nail-biting, and pacing, and presents anxiety-related behavior trends and self-care suggestions without providing a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and counselors use the skill to review video-based counts and trends for hand-rubbing, nail-biting, and pacing as an aid to self-awareness, not as a medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive video and identity-linked metadata may be sent to a cloud service.

Mitigation: Obtain informed consent from everyone recorded and confirm the configured service and its data handling before use.

Risk: The skill may silently create or reuse an identity and store account tokens locally.

Mitigation: Check how to switch or delete the local identity and tokens, uploaded videos, and historical reports before installation.

Risk: Anxiety-related behavior reports could be misused for covert monitoring or mistaken for a diagnosis.

Mitigation: Avoid covert, workplace, or school monitoring; treat visual behavior indicators as self-awareness aids rather than clinical conclusions.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [JSON analysis report or Markdown summary and historical report table]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior counts, durations, trends, index, self-care suggestions, and report links where available]

## Skill Version(s):

1.0.7 (source: server-resolved ClawHub release; bundled frontmatter lists 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
