## Description:

易中标投标文件智能写作助手 helps agents use the BaiLian bid-document API to interpret tender files, generate editable bid documents, and review bid submissions for compliance risks after the user provides local files and configures an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to process Chinese tender and bid workflows: summarize tender requirements, identify scoring and disqualification issues, draft .docx bid documents, and produce compliance review reports. It is intended for tasks where the user has provided local tender or bid files and accepts upload to the BaiLian cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid files may contain business, pricing, or personal data and are uploaded to biaoshu.zhiliaobiaoxun.com for processing.

Mitigation: Confirm user consent before upload and install only when this cloud processing and account-linked retention model is acceptable.

Risk: The App Key authorizes the user's BaiLian account and is stored locally in the skill directory.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and reset it through the service if exposure is suspected.

Risk: Bid document generation consumes account points and long-running jobs may continue after the agent-side command times out.

Mitigation: Check the account balance before generation, confirm point charges with the user, and resume existing jobs instead of resubmitting generation requests.

Risk: Changing optional endpoint configuration can redirect uploads away from the default production service.

Mitigation: Avoid setting custom base endpoint values unless the user intentionally wants a different endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-insight)
- [Publisher profile](https://clawhub.ai/user/chichihaixiaojian666)
- [BaiLian bid platform](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, shell commands, configuration, guidance]

**Output Format:** [Agent-facing guidance, progress text, local file paths, HTML or Word reports, and generated .docx bid documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a locally stored App Key; uploads user-selected tender and bid files to biaoshu.zhiliaobiaoxun.com; bid generation consumes account points.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
