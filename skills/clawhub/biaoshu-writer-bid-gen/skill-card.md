## Description:

投标文件智能生成 helps agents use the 百炼®标书 open API to interpret tender documents, generate editable bid documents, and review bid submissions for compliance when users provide the relevant local files and consent to cloud processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents supporting bid teams use this skill to turn user-provided tender files into structured tender interpretations, generated bid documents, and compliance review reports. It is intended for workflows where the user has an App Key, understands that files are uploaded to the 百炼®标书 service, and wants concrete bid-document outputs rather than general procurement advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service.

Mitigation: Use the skill only after the user understands and accepts the upload, processing, and service-side retention described in the artifact and scanner guidance.

Risk: The local config.json stores an App Key that authorizes actions and credit usage for the associated account.

Mitigation: Keep config.json private, do not paste the App Key into chat, and avoid forwarding links that contain App Key or bind_key parameters.

Risk: Setting ZCM_BASE changes the API server used for document uploads and credential-bearing requests.

Mitigation: Leave ZCM_BASE unset unless the user intentionally trusts the alternate server.

Risk: Generated bid content and compliance findings may be incomplete or misleading if source documents, account knowledge-base material, or service results are incomplete.

Mitigation: Have qualified bid staff review generated documents, compliance reports, and any marked issues before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-bid-gen)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)
- [Open API base](https://biaoshu.zhiliaobiaoxun.com/api/open/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance, local configuration instructions, shell-command workflows, JSON/API responses, HTML or Word reports, and generated .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a local App Key configuration; uploads local tender or bid files to the 百炼®标书 cloud API; generated bid documents consume account credits; outputs are written under biaoshu-bailian-files/ or a user-selected output path.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
