## Description:

A Simplified Chinese bidding assistant skill that uses the BaiLian bid-document API to interpret tender documents, generate technical bid documents, and run bid compliance reviews after the user provides local files and an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External bidding teams and agents working with mainland-China tender workflows use this skill to analyze tender requirements, draft technical bid deliverables, and review bid documents for compliance risks. It is intended for cases where the user has explicitly provided local tender or bid files and understands that the files are uploaded to the BaiLian bid-document service.

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Sensitive tender files, bid files, and the App Key can be sent to a configurable API endpoint if the base URL is changed.

Mitigation: Review endpoint configuration before use and keep ZCM_BASE or stored base settings pointed only at the trusted BaiLian production service.

Risk: Tender and bid materials may contain commercial, pricing, and personal information that is uploaded to the BaiLian service.

Mitigation: Confirm user consent before upload and avoid using the skill for documents that are not approved for third-party processing.

Risk: The App Key is an account credential and can expose account access or billing if copied into chat logs or links.

Mitigation: Keep the App Key in the local skill config file with restricted permissions, do not request or echo it in conversation, and do not forward links containing bind_key or App Key parameters.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-master-tech)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [BaiLian bid-document service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](artifact/references/api.md)
- [Usage reference](artifact/references/usage.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with background shell execution, JSON status summaries, HTML or Word reports, and generated .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are primarily Simplified Chinese and may include absolute local file paths for generated reports and bid documents.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
