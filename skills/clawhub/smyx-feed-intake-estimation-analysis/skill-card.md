## Description:

Estimates daily feed intake per livestock individual from continuous feeder videos by tracking the change of feed remaining in the trough, and outputs intake trend with anomaly alerts. | 通过食槽视频估算每日采食量变化，异常时预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock operators and developers use this skill to estimate feed intake from feeder-area images or videos, review intake trends, and surface anomaly alerts. The skill provides visual estimates and trend reporting, not feeding adjustment or ration-formulation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently handle local identity material, provision or log in to a remote account, and persist tokens in the workspace.

Mitigation: Review the identity and token behavior before installing, run it in a separate workspace, and use non-sensitive test media unless the Life Emergence API service and retention model are trusted.

Risk: Uploaded feeder media and generated historical reports are processed through a remote API service.

Mitigation: Use media appropriate for the API provider's retention and account model, and avoid uploading sensitive farm footage until those terms are acceptable.

Risk: Feed intake values are visual estimates and may be affected by camera angle, lighting, occlusion, or inconsistent trough setup.

Mitigation: Treat results as trend and anomaly signals, maintain stable capture conditions, and confirm feeding decisions against farm procedures and qualified nutrition guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-intake-estimation-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Feed intake API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown and JSON, with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include daily intake estimates, trend labels, anomaly alert levels, report links, and historical report tables.]

## Skill Version(s):

1.0.7 (source: server release metadata; SKILL.md frontmatter states 1.0.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
