## Description:

标书检查工具 helps an agent use the Bailian Biaoshu cloud API to interpret tender documents, extract packages, generate bid document drafts, and optionally review bid compliance after the user provides local files and configures an App Key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chichihaixiaojian666](https://clawhub.ai/user/chichihaixiaojian666)

### License/Terms of Use:

MIT-0

## Use Case:

External users and bid teams use this skill to turn local tender and bid files into structured tender analysis, bid document drafts, and compliance review reports through the Bailian Biaoshu service. The agent should confirm data-upload consent before sending business, pricing, or personal data to the cloud API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender and bid documents may contain business, pricing, or personal data and are uploaded to the Bailian Biaoshu cloud service.

Mitigation: Confirm user consent before upload and install only when the user is comfortable with cloud processing under their App Key account.

Risk: The local config.json stores the App Key credential for the service account.

Mitigation: Keep the App Key out of chat, store it only in the local config file, and remove config.json when the skill should no longer retain credentials.

Risk: Using an unexpected API base URL could send tender data to the wrong endpoint.

Mitigation: Verify the API base URL remains the expected official Bailian Biaoshu domain before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chichihaixiaojian666/skills/biaoshu-writer-review-pro)
- [Bailian Biaoshu service](https://biaoshu.zhiliaobiaoxun.com/)
- [API contract reference](references/api.md)
- [Usage guide](references/usage.md)

## Skill Output:

**Output Type(s):** [text, markdown, files, configuration, guidance]

**Output Format:** [Markdown responses plus generated HTML, Word, and DOCX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include tender analysis summaries, absolute local file paths, HTML or Word reports, and generated bid document .docx files.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
