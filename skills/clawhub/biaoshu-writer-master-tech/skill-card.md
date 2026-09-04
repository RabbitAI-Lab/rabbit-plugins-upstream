## Description:

Assists bid teams with tender interpretation, bid document generation, bid compliance review, and similarity checks for Chinese procurement workflows using the BaiLian bid-document service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, proposal, and bid teams use this skill to analyze tender files, generate editable bid documents, review submissions for stated risks, and compare bid files for similarity before submission. It is oriented toward zh-CN mainland-China bidding terminology and workflows.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercial, pricing, personal, or regulated procurement information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use only when the user and organization are comfortable with that upload and have reviewed applicable confidentiality rules.

Risk: The BaiLian API key grants account access and may expose account data or balance if shared in chat.

Mitigation: Have the user write the key only to the local config.json file and never paste, repeat, or echo it in conversation.

Risk: Generated bid documents, compliance findings, and similarity checks can be incomplete or unsuitable for final submission without domain review.

Mitigation: Treat outputs as drafting and internal review aids, then have qualified bid, legal, or compliance reviewers verify them before submission.

Risk: Bid document generation may consume the BaiLian account's available word balance.

Mitigation: Confirm the user understands account-balance impact before generation and distinguish generation consumption from submission prechecks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-tech)
- [BaiLian bid-document service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract](artifact/references/api.md)
- [Usage guide](artifact/references/usage.md)
- [Knowledge fields](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Chinese-language text summaries, JSON results, HTML or Word reports, and editable .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include locally written reports under biaoshu-bailian-files/ and short-lived download links for generated bid documents.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
