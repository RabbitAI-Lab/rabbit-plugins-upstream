## Description:

This skill helps agents interpret mainland-China tender documents, generate editable bid documents, and run compliance reviews through the 百炼®标书 cloud API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and procurement teams use this skill to analyze Chinese tender files, create draft bid documents, and check submitted bid files for compliance and similarity risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain confidential commercial, pricing, or personal data and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Use the skill only after the user understands and approves cloud processing, account-based retention, and credit use.

Risk: A configurable API base can redirect sensitive documents and the App Key away from the claimed official service.

Mitigation: Before use, ensure ZCM_BASE is unset and config.json contains only expected App Key and output settings, not a custom base URL.

Risk: The App Key controls account access and billing; leaking it through chat, logs, or key-bearing links can expose the account.

Mitigation: Have the user write the App Key locally, do not ask them to paste it into chat, and never forward recharge or binding links that include key parameters.

Risk: Generated bid documents and compliance findings may be incomplete or need human judgment before submission.

Mitigation: Review generated .docx files, unresolved placeholders, risk findings, and compliance reports before relying on them for an actual bid.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-express)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Chinese-language guidance plus JSON summaries, HTML reports, Word reports, and .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local tender or bid file paths and a user-provided App Key; generated files are written under biaoshu-bailian-files/ unless configured otherwise.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
