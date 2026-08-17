## Description:

标书全流程制作 helps agents interpret user-provided tender documents, generate technical and commercial bid .docx files, and review bid documents for compliance using the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users, bid teams, and their agents use this skill to process provided tender and bid files, produce bid-document drafts, and surface compliance issues before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive commercial or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user awareness and consent before upload, process only files the user explicitly provides, and direct users to review vendor retention and account controls.

Risk: The App Key is a full account credential for the vendor service.

Mitigation: Keep the App Key out of chat and environment variables; store it only in the local skill config file with restricted permissions.

Risk: Bid generation consumes points from the App Key account.

Mitigation: Check account balance and confirm the intended generation step before creating bid documents.

Risk: Generated results and uploaded files may remain available in the vendor account for a limited retention period.

Mitigation: Tell users that results are associated with their App Key account and should be managed or removed through the vendor platform when appropriate.

## Reference(s):

- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)
- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-flow)
- [百炼®标书 Platform](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown responses with absolute local file paths, plus generated HTML, Word, and DOCX files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include bid interpretation summaries, generated bid documents, compliance risk reports, and follow-up guidance.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
