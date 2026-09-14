## Description:

Supports Chinese bid-document workflows by interpreting tender files, generating .docx bid documents, reviewing compliance risks, and comparing bid documents for similarity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to upload tender and bid files to the 百炼®标书 service for interpretation, bid drafting, compliance review, and similarity checks. It is intended for document preparation and internal review support, not as a legal determination of compliance, collusion, or bid eligibility.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uploads tender and bid documents to an external service for processing.

Mitigation: Confirm the exact files, destination service, and user consent before upload, especially when files contain pricing, commercial, or personal information.

Risk: The skill uses an API key tied to account access and paid word balance.

Mitigation: Have the user configure credentials locally; do not request, echo, or transmit API keys, phone numbers, SMS codes, or credential-bearing links in chat.

Risk: Paid generation, review, and similarity checks can consume account word balance.

Mitigation: Confirm billing impact and user-selected generation scope before submitting paid tasks, and explain that estimates may differ from final platform settlement.

Risk: Generated bid content and compliance findings may be incomplete, inaccurate, or legally insufficient.

Mitigation: Treat outputs as drafting and review support; require human review before submission and avoid presenting similarity checks as legal findings.

Risk: Arbitrary output paths could overwrite important local files.

Mitigation: Confirm output paths before writing files and prefer the skill's normal generated-output directory unless the user explicitly chooses another location.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-insight)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 总调度](references/api.md)
- [鉴权、任务与可用字数接口](references/api-auth.md)
- [智能解读与标书制作 API](references/api-bid-workflow.md)
- [标书审查 API](references/api-compliance.md)
- [标书查重 API](references/api-duplicate.md)
- [知识库字段说明](references/knowledge-fields.md)
- [执行细节（操作手册）](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Natural-language guidance, structured status summaries, JSON results, HTML or Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local report paths, short-lived download links, progress updates, risk summaries, and generated bid files.]

## Skill Version(s):

3.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
