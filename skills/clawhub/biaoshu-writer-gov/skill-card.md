## Description:

喜鹊投标文件写作 helps agents analyze tender files, generate editable bid documents, and review compliance and similarity risks through the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and agents use this skill when they have local tender or bid files and need AI-assisted tender interpretation, editable .docx bid generation, or compliance and similarity review before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial or personal information and are uploaded to the 百炼®标书 service for processing.

Mitigation: Use the skill only after the user understands and accepts that upload, and process only files the user explicitly provides.

Risk: The App Key is a full account credential and could expose account access if shared in chat or embedded in links.

Mitigation: Keep the App Key out of conversation logs, store it only in the local config file, and rotate it if exposure is suspected.

Risk: Bid-document generation consumes credits from the App Key owner's account.

Mitigation: Confirm the user is aware of credit use before generation and rely on the skill's balance precheck before submission.

Risk: Custom service endpoint configuration can redirect document uploads if set to an untrusted endpoint.

Mitigation: Do not set custom endpoint overrides unless the endpoint is controlled or trusted by the user.

## Reference(s):

- [Usage Guide](references/usage.md)
- [API Reference](references/api.md)
- [ClawHub Skill Page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-gov)
- [百炼®标书 Service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Markdown responses with generated .docx bid documents and HTML or Word reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided local tender or bid files and a locally configured App Key; bid-document generation consumes account credits.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
