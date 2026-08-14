## Description:

招标文件解析助手 uses an App Key to call the 百炼®标书 cloud API to interpret tender files, extract packages, generate editable bid documents, and optionally review bid compliance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid-preparation teams use this skill to analyze tender documents, decide whether to bid, generate editable .docx bid files, and check completed bids for disqualification and compliance risks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain business, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm user awareness and consent before upload, use only user-selected local files, and avoid using the skill for documents that cannot be sent to the named service.

Risk: The App Key is a full account credential and may expose the user's account if pasted into chat or embedded in shared links.

Mitigation: Have the user create the local config.json themselves, never ask them to paste or repeat the App Key, and do not forward links containing App Key or bind_key parameters.

Risk: Custom API base settings can redirect uploaded documents and credentials to an unintended endpoint.

Mitigation: Use the default biaoshu.zhiliaobiaoxun.com endpoint unless the user explicitly trusts and controls the alternate endpoint.

Risk: Generated bid content and compliance findings may be incomplete or inaccurate for a particular tender.

Mitigation: Treat generated bid files, reports, and risk findings as drafts for human review before submission.

Risk: Bid generation consumes the App Key account's points and long-running jobs can continue after a local tool session times out.

Mitigation: Check balance before submission, avoid duplicate generation requests, and resume using the existing job handle when possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-read-pro)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown/text responses plus generated HTML reports and Word .docx files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uploads user-selected tender and bid documents to 百炼®标书; generated task results and .docx outputs may remain available through that service for about 7 days.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
