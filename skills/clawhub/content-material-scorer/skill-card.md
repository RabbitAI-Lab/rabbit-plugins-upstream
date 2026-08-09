## Description:

用 5 维评分体系对短视频和口播素材打分评级，帮助创作者和内容运营判断素材应立即生产、排期生产或丢弃。

This skill is ready for commercial/non-commercial use.

## Publisher:

[shiyan521](https://clawhub.ai/user/shiyan521)

### License/Terms of Use:

MIT

## Use Case:

External creators, short-video hosts, and content operations teams use this skill to screen incoming clips, quotes, user language, and content ideas with a repeatable Chinese scoring workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private information or unpublished third-party product details could be exposed if users paste raw material into an AI thread or cloud candidate table.

Mitigation: Review, redact, or anonymize private and third-party details before using the skill output in shared tools or cloud tables.

Risk: The scoring workflow may over-rank material that lacks a clear hook or cannot be safely desensitized.

Mitigation: Apply the hard exclusion, quick exclusion, and desensitization checks before assigning an A tier or production priority.

## Reference(s):

- [5 维评分细则](references/score-rubric.md)
- [素材候选表模板](assets/candidate-table-template.md)
- [ClawHub Skill Page](https://clawhub.ai/shiyan521/skills/content-material-scorer)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown scoring record with five dimension scores, weighted total, A/B/C tier, main angle, and priority.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a configurable speaker/topic filter, a five-dimension weighted rubric, and optional candidate table fields.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
