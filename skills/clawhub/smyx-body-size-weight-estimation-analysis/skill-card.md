## Description:

Estimates livestock body length and body weight from side-view videos or frames, tracking fattening progress in a contactless manner. | 通过视频视觉估测体长、体重，追踪育肥进度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and livestock managers use this skill to estimate body length, body height, girth, body weight, and fattening stage from clear side-view livestock images or videos. It also supports cloud-backed retrieval of account-linked historical analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded media or URLs, internal identifiers, and account-linked history may be sent to cloud services.

Mitigation: Use only with data whose cloud processing is acceptable, and avoid sensitive farm footage unless the publisher and service handling are trusted.

Risk: The skill can silently create or reuse a local identity and store service tokens locally.

Mitigation: Review local workspace access and token storage expectations before installing in shared environments.

Risk: Weight and growth-stage results are estimates based on visual inputs.

Mitigation: Treat results as operational reference only and confirm important weighing or production decisions with established farm processes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)
- [API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Structured text or JSON with Markdown report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report export links and historical report tables.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
