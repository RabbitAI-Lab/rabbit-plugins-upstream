## Description:

AI 投标文件写作 helps users interpret Chinese tender documents, generate editable .docx bid files, and run compliance or similarity self-checks through the Bailian Bid service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bidding teams and their agents use this skill to understand tender requirements, prepare bid-document drafts, and check submissions for compliance or similarity risks before filing. It is designed for mainland-China bidding workflows and Chinese tender documents.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm the user understands and accepts the upload and retention behavior before use, and process only files the user intentionally provides.

Risk: The App Key authorizes the account and can affect billing through point-consuming bid generation.

Mitigation: Keep the App Key out of chat, store it only in the local config.json credential file, and avoid forwarding credential-bearing links.

Risk: Generated bid documents and compliance reports may be incomplete or contain items requiring human judgment.

Mitigation: Treat generated .docx files and reports as drafts for review, especially retained placeholders, compliance findings, and final filing decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-gov)
- [Bailian Bid service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage and operations reference](references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance plus local file paths, JSON task results, HTML or Word reports, and generated .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated report labels and bid-workflow terminology are primarily Simplified Chinese; local outputs are written to the configured output directory.]

## Skill Version(s):

1.0.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
