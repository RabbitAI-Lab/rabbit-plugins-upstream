## Description:

智能标书编制 helps agents analyze tender files, generate editable bid documents, and review bid submissions for compliance through the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and employees working on tender responses use this skill when they provide local tender or bid files and need structured interpretation, bid-document generation, or compliance review. The skill is suited to document-heavy bidding workflows where uploads to the 百炼®标书 cloud service and account-credit use are acceptable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents can contain commercial, pricing, and personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Use the skill only after the user understands and accepts the cloud upload, account-based processing, and server retention described in the skill documentation.

Risk: The App Key authorizes the user's 百炼®标书 account.

Mitigation: Keep the App Key out of chat and store it only in the local skill config.json file with restricted permissions.

Risk: A custom base URL setting could change where documents and credentials are sent.

Mitigation: Review any custom ZCM_BASE or stored base setting before use and prefer the documented production endpoint unless the user intentionally configured another endpoint.

Risk: Generated bid documents may consume account credits.

Mitigation: Check the account balance and confirm the user's intent before submitting bid-document generation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-studio)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance plus generated HTML, Word, and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local App Key configuration and user-provided tender or bid files; bid generation may consume account credits.]

## Skill Version(s):

1.0.11 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
