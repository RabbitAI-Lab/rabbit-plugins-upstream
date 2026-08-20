## Description:

A Simplified Chinese bid-document assistant for mainland-China tender workflows that interprets tender files, drafts commercial bid documents, and reviews bid compliance through the 百炼®标书 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and bid writers use this skill to analyze tender documents, generate editable commercial bid files, and review bid submissions for compliance risks before submission.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial or personal information and are uploaded to 百炼®标书 servers under the user's App Key account.

Mitigation: Use the skill only after the user understands and accepts the upload, retention, and account association described in the release evidence.

Risk: The App Key is a full account credential that could be exposed through chat, logs, screenshots, or credential-bearing links.

Mitigation: Keep the App Key out of conversation, store it only in the local config file, and do not share generated links that contain credential parameters.

Risk: Changing the service endpoint can redirect sensitive tender files to an unintended destination.

Mitigation: Use the default 百炼®标书 endpoint unless the user deliberately trusts a configured ZCM_BASE or --base endpoint.

Risk: Generated bid content and compliance findings may be incomplete, stale, or dependent on the user's available company materials.

Mitigation: Have qualified staff review generated .docx files, risk findings,待填项, and compliance reports before submission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-assistant-business)
- [Usage guide](references/usage.md)
- [API contract reference](references/api.md)
- [百炼®标书 service](https://biaoshu.zhiliaobiaoxun.com/)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Markdown responses with generated .docx bid documents, HTML or Word reports, and local output paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a locally stored App Key; tender and bid files are uploaded to 百炼®标书 servers for processing.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
