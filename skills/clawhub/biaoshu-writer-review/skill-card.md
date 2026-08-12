## Description:

Calls the 百炼®标书 cloud API with a user-owned App Key to interpret tender documents, extract bid packages, generate editable .docx bid documents, and optionally run compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bid teams and procurement-support users use this skill to interpret tender files, generate bid documents, and review bid compliance through 百炼®标书 after confirming consent to upload tender and bid files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain commercial, pricing, or personal information and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before uploading files and only process files the user explicitly provides.

Risk: The App Key is a full account credential stored locally in the skill directory.

Mitigation: Have the user create the local config file themselves, never paste the App Key into chat, and keep credential file permissions restricted.

Risk: Generated results are retained under the App Key account and may be visible through the 百炼®标书 platform until they expire or are managed by the user.

Mitigation: Tell users that outputs are retained by the service account and direct them to manage history through the official platform.

Risk: Bid generation consumes credits from the App Key account.

Mitigation: Check account balance before submission and make clear that bid generation spends account credits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review)
- [百炼®标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [百炼®标书开放 API 契约参考](references/api.md)
- [后台操作手册](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files, guidance]

**Output Format:** [Markdown guidance plus generated HTML reports and Word documents.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated bid documents are .docx; interpretation and compliance reports can be HTML or Word. Cloud results may expire after about 7 days.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
