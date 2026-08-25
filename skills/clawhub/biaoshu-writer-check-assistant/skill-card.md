## Description:

Checks bid documents through the 百炼®标书 service, with support for tender interpretation and bid document generation when users provide local files and consent to upload them for processing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External procurement and bidding teams use this skill to interpret tender documents, generate editable bid documents, and check bid files for rejection risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files can contain commercial, pricing, and personal data and are uploaded to the 百炼®标书 service for processing.

Mitigation: Confirm user consent before upload and review the service's retention, account, and billing behavior for the App Key being used.

Risk: The App Key grants access to the user's service account and could be exposed if pasted into chat or forwarded in credential-bearing links.

Mitigation: Have the user store the App Key only in the local config file, never echo it in chat, and avoid forwarding any links that include credential parameters.

Risk: The scanner noted a local project cache path broader than the declared write scope.

Mitigation: Review local persistence before deployment and set ZCM_HOME to an approved storage location when cache placement must be constrained.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-check-assistant)
- [百炼®标书服务](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [执行细节（操作手册）](references/usage.md)
- [知识库字段说明](references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [Analysis, Files, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Plaintext or Markdown summaries with generated HTML/Word reports and editable .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts are written to local output paths; tender and bid files are uploaded to the 百炼®标书 service under the user's App Key.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
