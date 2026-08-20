## Description:

百炼标书智能写作工具 uses an App Key to call the 百炼®标书 open API for tender interpretation, package extraction, bid document generation, and optional compliance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and agents supporting mainland-China tender workflows use this skill to interpret tender documents, extract bid packages, generate editable bid documents, and review bid compliance when users provide local files and an App Key.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Tender and bid files may contain commercial, pricing, and personal information and are uploaded to the third-party 百炼标书 service for processing.

Mitigation: Confirm the user understands and agrees before upload, and avoid using the skill for documents that cannot be shared with that service.

Risk: The App Key is an account credential stored locally and could be exposed if pasted into chat or copied into shared logs.

Mitigation: Have the user write the App Key only to the local config file, keep the file permissions restricted, and never echo or request the key in conversation.

Risk: The security evidence notes that the API endpoint can be redirected beyond the stated official service scope.

Mitigation: Verify the configured API base is the official 百炼标书 endpoint before use and avoid untrusted ZCM_BASE or config base values.

Risk: Bid generation can consume the App Key account's credits.

Mitigation: Check the account balance and confirm the user intends to generate a bid document before submitting generation work.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-bailian)
- [百炼标书 platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage reference](references/usage.md)

## Skill Output:

**Output Type(s):** [guidance, text, markdown, shell commands, configuration, files]

**Output Format:** [Plain text guidance plus generated DOCX, HTML, and Word report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs and platform labels are primarily Simplified Chinese; generated bid documents and reports are written to local files.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
