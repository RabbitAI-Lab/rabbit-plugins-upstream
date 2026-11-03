## Description:

Estimates livestock body measurements and weight from side-view images or videos to help track fattening progress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock producers and farm teams use the skill to estimate body length, height, girth, weight, and fattening stage from side-view images or videos, and to review earlier analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared-account handling may expose reports between users.

Mitigation: Use a release that fixes sender isolation before shared use.

Risk: Selected photos and videos are uploaded to Life Emergence for analysis.

Mitigation: Obtain consent before upload and avoid sending sensitive imagery.

Risk: The configuration-only option may still upload media, and credentials remain on the local machine.

Mitigation: Do not rely on --export-env-only to prevent uploads; avoid using unrelated secrets as the API key and protect locally stored credentials.

## Reference(s):

- [Livestock estimation API reference](references/api_doc.md)
- [Analysis API details](skills/smyx_analysis/references/api_doc.md)
- [Skill introduction and demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured estimation reports with body measurements, estimated weight, fattening stage, and report links; historical reports can be listed in Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual estimates are for progress reference; image quality, animal pose, occlusion, and a known-size reference affect usefulness.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
