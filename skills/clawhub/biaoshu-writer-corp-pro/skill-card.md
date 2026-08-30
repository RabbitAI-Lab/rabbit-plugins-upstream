## Description:

面向招投标全流程的智能投标文件助手，可在用户提供本地招标或投标文件并配置 App Key 后，调用百炼®标书开放 API 完成招标解读、投标文件生成和合规审查。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and proposal writers use this skill to analyze tender files, generate editable bid documents, and review submitted bid files for disqualification or compliance risks. It is intended for workflows where the user explicitly selects local tender or bid documents and understands they will be processed by the 百炼®标书 cloud service.

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before upload, use only user-selected local files, and disclose that service-side results are retained temporarily under the App Key account.

Risk: The App Key is an account credential that can authorize service access and spending.

Mitigation: Keep the App Key in the local config file, never request or echo it in chat, and do not share URLs that include credential parameters.

Risk: Bid generation consumes account points and long-running jobs may continue after a local client timeout.

Mitigation: Precheck account balance, explain that generation is the spending step, and resume by job ID instead of resubmitting duplicate work.

Risk: Generated bid content or compliance review output may include unresolved placeholders, partial results, or issues requiring human judgment.

Mitigation: Require manual review before submission, preserve unresolved fields as placeholders, and clearly label partial compliance results when the service reports them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-corp-pro)
- [百炼®标书平台](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage and operation guide](references/usage.md)
- [Knowledge base fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown or text guidance with local file outputs such as HTML reports, Word .docx documents, and JSON command results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are primarily zh-CN bidding artifacts; generated reports and bid documents are written to local paths and may also be available in the linked cloud account.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
