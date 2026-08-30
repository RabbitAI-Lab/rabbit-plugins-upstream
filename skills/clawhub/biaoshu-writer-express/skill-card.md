## Description:

Automates Chinese bid-document workflows by using the BaiLian Biaoshu API to interpret tender files, generate editable .docx bid documents, and produce compliance review reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Procurement, proposal, and bid-response teams use this skill to analyze tender documents, draft bid packages, and check completed bids for compliance risks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain sensitive commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use the skill only after the user understands and accepts third-party processing and account-level retention of uploaded files and generated results.

Risk: The App Key grants account access for API calls and billing.

Mitigation: Store the App Key only in local config.json, never paste it into chat, and avoid forwarding any URL that contains key or bind_key parameters.

Risk: Bid generation consumes account credits and long-running jobs can continue after a local client interruption.

Mitigation: Check account balance before generation, use idempotent or resumable job handling when retrying, and avoid resubmitting generation jobs unnecessarily.

Risk: Generated bid content and compliance findings can be incomplete, rely on account knowledge-base data, or leave placeholders where facts are unavailable.

Mitigation: Review generated .docx files, reports, placeholder fields, and compliance findings before relying on them for a real submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-express)
- [BaiLian Biaoshu platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](artifact/references/api.md)
- [Usage reference](artifact/references/usage.md)
- [Knowledge-base field reference](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Plain-language summaries and Markdown responses, plus generated .docx bid documents and HTML or Word reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided local tender or bid files, an App Key stored in local config.json, and writes generated artifacts under the configured output directory.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
