## Description:

凭 App Key 调用百炼®标书开放 API，帮助用户解读招标文件、生成成品投标文件，并对投标文件执行可选合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users working on mainland-China bidding workflows use this skill to process local tender and bid documents through the 百炼®标书 API for tender interpretation, bid-document generation, and compliance review. It is intended for Chinese tender documents and produces Chinese report labels and artifacts.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, and personal information and are uploaded to the 百炼®标书 cloud API for processing.

Mitigation: Confirm user consent before upload and advise users to review the provider's data retention and billing terms before use.

Risk: The App Key is a full account credential used for API access and account credit consumption.

Mitigation: Keep the App Key out of chat, store it only in the local skill config file with restricted permissions, and rotate it on the provider site if exposure is suspected.

Risk: Security evidence reports that API traffic can be redirected to a configurable host despite the skill metadata naming the official domain as the only network target.

Mitigation: Verify ZCM_BASE is unset and config.json does not contain a non-official base URL unless the user intentionally trusts that endpoint.

Risk: Generated bid documents and compliance findings may contain incomplete, uncertain, or provider-retained results.

Mitigation: Require human review before submission, especially for business facts, pricing, signatures, stamps, mandatory forms, and any reported high-risk or review-level compliance issues.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [API Contract Reference](references/api.md)
- [Usage Guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance plus local files such as HTML reports, Word reports, and DOCX bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include absolute local file paths, risk summaries, compliance findings, generated reports, and bid documents.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
