## Description:

Estimates livestock body length and body weight from side-view videos or frames, tracking fattening progress in a contactless manner. | 通过视频视觉估测体长、体重，追踪育肥进度。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock producers and farm operators can estimate body measurements, weight, and fattening stage from side-view images or video to track growth. Results are reference estimates and should be considered alongside established weighing and farm-management procedures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan marks the release suspicious, citing reported credential handling, automatic account-related behavior, and network or analysis actions that may exceed its stated purpose.

Mitigation: Review credential and account flows and outbound requests before use; avoid providing sensitive credentials until those behaviors are understood.

Risk: The security scan was partial because a local reference was missing.

Mitigation: Obtain and review the missing referenced material, then reassess the skill before deployment.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis results with estimated body measurements, weight, fattening stage, confidence or usability notes, and report links; history listings use Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Estimates are for growth-tracking reference.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
