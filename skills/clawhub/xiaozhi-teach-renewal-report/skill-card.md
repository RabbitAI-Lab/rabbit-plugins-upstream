## Description:

用学员真实的学习记录做一份阶段报告，让续课变成家长看完事实后的自主选择。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT

## Use Case:

Independent teachers use this skill to draft evidence-based progress reports and renewal recommendations from one named student's learning records. It checks authorization before preparing parent-facing content and leaves review and sending to the teacher.

### Deployment Geography for Use:

China (mainland; use only in legally permitted training settings).

## Known Risks and Mitigations:

Risk: Reports use sensitive longitudinal learning records, potentially including information about minors.

Mitigation: Name the learner before reading records, limit access to relevant fields, verify applicable consent before creating parent-facing content, and have the teacher review every report before sharing.

Risk: Privacy controls and archive deletion depend on the host platform's access limits and separate record-management workflow.

Mitigation: Confirm the host enforces the documented access restrictions and use its separate archive-deletion process for learner-record deletion requests.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [Stage report templates](artifact/references/stage-report-templates.md)
- [Renewal communication scripts](artifact/references/renewal-communication-scripts.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown progress-report drafts, evidence summaries, renewal recommendations, and communication scripts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only the named learner's authorized, relevant records; unsupported figures or claims are omitted. Teacher review is required before sharing, and sending remains manual.]

## Skill Version(s):

2.12.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
