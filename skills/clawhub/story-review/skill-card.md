## Description:

以多视角对抗式流程审查小说的结构、角色、文字与设定，并给出有原文依据的修改建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

小说作者可用此技能审查章节或稿件中的剧情结构、人物动机、表达和设定一致性，并获得引用原文的优先级问题与修改建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Review workflows can update tracking files, and generated tracking views can be replaced or removed.

Mitigation: Keep tracking files under version control; solo mode avoids automatic tracking corrections, though batch reviews still save progress.

Risk: The punctuation helper edits files when run in normalizing mode.

Mitigation: Always use --check when running it as a review precheck.

Risk: Separately installed reviewer agents and host permissions were not covered by the bundle inspection.

Mitigation: Confirm the deployed reviewer agents and host permissions before relying on them.

## Reference(s):

- [Quality rubric](references/quality-rubric.md)
- [Style resolution](references/style-resolution.md)
- [Solo review workflow](references/solo.md)
- [Tracking transaction protocol](references/tracking-transaction.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review report with cited findings and revision suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports findings without editing manuscript content; review-tracking files may be updated in applicable modes.]

## Skill Version(s):

1.1.45 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
