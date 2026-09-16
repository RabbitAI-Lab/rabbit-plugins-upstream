## Description:

Identifies weed species and coverage density from field top-view images, and outputs a weed distribution heatmap dataset to support precision weeding decisions. | 通过田间图像识别杂草种类与覆盖密度，生成除草建议区域热力图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze field top-view images or videos for weed species, distribution areas, coverage density, weed-pressure levels, heatmap data, and report links for precision weeding decisions. The skill also supports cloud history lookup for prior weed-identification reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads field images or videos to the publisher's cloud service for analysis and report history.

Mitigation: Use only media approved for third-party cloud processing, avoid unrelated sensitive content in captures, and review organizational data-sharing requirements before installation.

Risk: The skill automatically creates or reuses an internal identity and may store reusable tokens in the workspace database.

Mitigation: Review token storage, access scope, and cleanup behavior before normal use; do not expose internal identity values in user-facing output.

Risk: The packaged configuration includes plaintext development endpoints and non-production service settings.

Mitigation: Switch the release configuration to HTTPS-only production endpoints and verify endpoint ownership before deployment.

Risk: The security guidance calls out packaging issues including a pet/video parameter mismatch and a YAML dependency issue.

Mitigation: Fix the parameter naming and dependency declaration before relying on the package in normal workflows.

## Reference(s):

- [Skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report text, JSON results, and Markdown tables for historical report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include weed species, density levels, distribution regions, heatmap data, weed-pressure level, and report export links.]

## Skill Version(s):

1.0.11 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
