## Description:

Estimates livestock body length and body weight from side-view videos or frames, tracking fattening progress in a contactless manner. | 通过视频视觉估测体长、体重，追踪育肥进度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to estimate livestock body length, body height, chest girth, body weight, and fattening stage from side-view livestock images, videos, or media URLs. The skill can also query cloud-hosted historical analysis reports tied to the current identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media, supplied URLs, report queries, and identity-linked metadata may be sent to configured services.

Mitigation: Install only when the publisher and configured service endpoints are trusted and the data handling is acceptable for the deployment.

Risk: The skill silently creates or reuses an identity, stores tokens locally, and links cloud report history to that identity.

Mitigation: Run the skill under an approved account boundary, review local token handling before deployment, and clear or revoke stored credentials when access should end.

Risk: Visual body-size and weight estimates can be inaccurate when captures have poor side view, occlusion, poor lighting, motion blur, or no known-size reference object.

Mitigation: Use complete side-view captures with a visible known-size reference and treat outputs as reference estimates rather than final weighing or production decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Files, Guidance]

**Output Format:** [Markdown or JSON analysis reports with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include estimated body measurements, estimated weight, fattening stage, confidence or usability notes, report links, and historical report tables.]

## Skill Version(s):

1.0.10 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
