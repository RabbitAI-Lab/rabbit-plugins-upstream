## Description:

上传招标/投标文件，AI 一站式完成智能解读（废标红线/评分标准/控标洞察）、成品投标文件(.docx)生成、标书审查（分级风险+雷同检测）和标书查重（2-3份投标文件相似/雷同风险检查）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and bidding users use this skill to interpret tender documents, generate editable bid documents, review bids for compliance risks, and compare bid files for similarity signals before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Use the skill only after confirming the user has authority to process the files and accepts cloud processing and account-based storage.

Risk: The API key grants account access and could be exposed if pasted into chat or shared in links.

Mitigation: Have the user create the local API-key config file themselves and do not request, echo, or forward credentials in conversation.

Risk: Bid generation can consume the account's available word balance.

Mitigation: Warn users before generation and report account word-balance information when the skill provides it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-ace)
- [Execution guide](references/usage.md)
- [Open API contract reference](references/api.md)
- [Knowledge field reference](references/knowledge-fields.md)
- [百炼标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with generated files including HTML reports, Word reports, DOCX bid documents, and JSON similarity results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include local report paths, short-lived bid-document download links, structured risk summaries, progress updates, and account word-balance notices.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
