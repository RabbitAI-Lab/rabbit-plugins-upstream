## Description:

标书全流程制作 helps agents interpret tender files, generate technical and commercial bid .docx files, and run compliance and bid-risk reviews through the 百炼®标书 cloud service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

Bidding teams and their agents use this skill to process user-provided tender and bid files, produce tender interpretations and bid documents, and review compliance risks before submission. It is localized for Simplified Chinese mainland-China bidding workflows and requires users to provide local files and their own 百炼®标书 App Key.

### Deployment Geography for Use:

Global; localized for Simplified Chinese mainland-China bidding workflows.

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, or personal information and are uploaded to the 百炼®标书 cloud service for processing.

Mitigation: Confirm user awareness and consent before upload, use only the files the user explicitly provides, and avoid uploading unrelated local data.

Risk: The App Key controls the user's 百炼®标书 account and may expose billing or account access if shared in chat or links.

Mitigation: Keep the App Key out of conversation history, store it only in the local config file as instructed, and do not repeat or forward key-bearing URLs.

Risk: Generated bid documents and compliance findings may be incomplete, inaccurate, or unsuitable for final submission without review.

Mitigation: Have the user review generated .docx files, reports, risk findings, required fields, pricing, signatures, and compliance conclusions before submission.

Risk: Bid document generation can consume account credits.

Mitigation: Check the account balance and confirm the user's intent before generating bid documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-flow)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API reference](artifact/references/api.md)
- [Usage guide](artifact/references/usage.md)
- [Knowledge fields](artifact/references/knowledge-fields.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Agent guidance plus local HTML/Word reports and .docx bid documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated artifacts and platform labels primarily use zh-CN procurement terminology; outputs should be reviewed before bid submission.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
