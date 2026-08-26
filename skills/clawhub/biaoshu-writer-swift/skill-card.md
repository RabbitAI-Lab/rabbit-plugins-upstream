## Description:

标书自动撰写工具 helps users interpret tender documents, generate formatted .docx bid drafts, and review bid files for compliance using the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to analyze tender files, generate editable bid documents, and review bid submissions for compliance risks. The skill is intended for cases where the user explicitly provides local tender or bid files and asks for interpretation, drafting, or compliance review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercial, pricing, and personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Use the skill only with user-selected local files after the user understands and accepts the cloud processing and account-based retention.

Risk: The App Key can access account-scoped bid workflows and limited company knowledge-base fields.

Mitigation: Keep the App Key in the local skill configuration, never place it in chat, and rotate it immediately if exposed.

Risk: Generated bid documents and compliance findings may contain待填项, incomplete semantic review status, or recommendations that require domain judgment.

Mitigation: Require human review before bid submission and clearly distinguish final results from partial or pending compliance review output.

Risk: Bid-document generation consumes account credits and long-running generation should not be resubmitted blindly.

Mitigation: Confirm generation intent before starting, monitor job progress, and resume existing jobs instead of submitting duplicates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-swift)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)
- [Open API contract reference](references/api.md)
- [Usage and operation reference](references/usage.md)
- [Knowledge-base field reference](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown text with generated HTML or Word reports and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local file paths for interpretation reports, compliance reports, and generated bid documents; requires a user-managed App Key and user-selected local files.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
