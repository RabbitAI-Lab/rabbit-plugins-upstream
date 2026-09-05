## Description:

Helps users interpret tender documents, generate editable bid documents, review bid compliance, and compare bid files for similarity risk using the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and agents use this skill to analyze tender requirements, identify disqualification and scoring risks, draft .docx bid documents, review submissions for compliance issues, and run authorized similarity checks before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files can contain sensitive commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Confirm the user understands and accepts cloud processing and retention before upload, and limit processing to files the user explicitly provides.

Risk: The Api Key grants account access if exposed in chat, logs, screenshots, or copied links.

Mitigation: Require the user to store the key locally in config.json, never ask them to paste it in chat, and avoid forwarding key-bearing account links.

Risk: Similarity checks could be mistaken for a legal finding about collusion or bid validity.

Mitigation: Use duplicate-check results only as internal pre-submission risk signals and require confirmation that the user is authorized to process all compared files.

Risk: Generated bid drafts and compliance findings may be incomplete or incorrect for the final submission context.

Mitigation: Require human review of generated documents, risk findings, retained placeholders, and filing requirements before submission.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-insight)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/?ch=c666)
- [Open API contract](references/api.md)
- [Usage guide](references/usage.md)
- [Knowledge base fields](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Configuration guidance]

**Output Format:** [Markdown or plain text summaries plus generated HTML, Word, DOCX, and JSON artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided local files and a user-managed Api Key; generated documents and reports are processed by the cloud service and may expire there after about 7 days.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
