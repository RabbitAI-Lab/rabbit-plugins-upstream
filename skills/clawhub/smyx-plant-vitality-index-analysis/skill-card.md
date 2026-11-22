## Description:

Analyzes plant images, environmental data, and growth metrics to produce a 0–100 vitality score and trend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, home gardeners, and plant-monitoring operators use this skill to assess plant vitality from images and optional environmental or growth data, including its recent trend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a mismatch between the plant-analysis description and account, credential, and video-analysis capabilities, along with unsafe credential handling and ignored export-only behavior.

Mitigation: Review the implementation and proceed only if you trust the service receiving media and identity data and are comfortable with local credential storage and account registration.

Risk: The security scan was partial because a referenced local path was missing, so it does not cover every referenced resource.

Mitigation: Review the missing referenced resource and other included resources before relying on the scan assessment.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-vitality-index-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured vitality report with score, grade, trend, and report link]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single images may provide a score without a trend; results are for care reference and can vary with image angle and lighting.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
