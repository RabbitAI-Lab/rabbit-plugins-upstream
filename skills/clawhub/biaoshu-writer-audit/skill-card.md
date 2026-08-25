## Description:

基于百炼®标书开放 API，帮助用户对招标文件和投标文件进行智能解读、投标文件生成和合规审查，并输出分级风险、依据、证据、修改建议及报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

投标团队、招采顾问和企业用户 use this skill to review tender and bid documents, identify compliance risks, generate bid-document drafts, and produce report files for follow-up editing or review.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Confirm user awareness and consent before upload, and process only files the user explicitly provides for the task.

Risk: The App Key is an account credential that can authorize use of the 百炼®标书 account.

Mitigation: Have the user store the App Key only in the local config file; do not request it in chat or share key-bearing recharge or bind links.

Risk: Bid-document generation can consume points from the App Key owner's account.

Mitigation: Check balance and confirm the user wants to proceed before generation tasks that may consume points.

Risk: Generated bid documents and compliance reports may contain incomplete, uncertain, or review-only findings.

Mitigation: Require human review before bid submission, preserve unresolved fields as fill-in items, and clearly label partial compliance results when semantic review is incomplete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-audit)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge-base fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Chinese-language text and Markdown guidance with generated HTML reports, Word reports, and .docx bid files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are scoped to user-selected tender and bid files; long-running jobs report progress and write local artifacts.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
