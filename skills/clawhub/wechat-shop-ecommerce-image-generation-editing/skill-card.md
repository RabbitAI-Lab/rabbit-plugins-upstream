## Description:

为微信小店、视频号、社群和朋友圈生成与编辑商品卡、私域海报、直播预告及复购图片，并 supports reference images with AI Hive generation and download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External merchants, operators, and creators use this skill to generate or edit product cards, private-domain posters, livestream covers, social sharing images, and repeat-purchase reminder visuals for WeChat commerce workflows. The workflow helps prepare prompts and CLI calls while leaving sensitive details such as QR codes, prices, dates, contact information, and compliance checks for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected product or reference images are uploaded to AI Hive for generation.

Mitigation: Use only approved product media and avoid private customer data, credentials, chats, or unrelated local files as reference images.

Risk: The workflow stores or reads an AI Hive API key locally.

Mitigation: Prefer environment variables or a protected local config file, and confirm local credential storage is acceptable before use.

Risk: Generated commerce images can include inaccurate claims or platform-sensitive content if prompts are not reviewed.

Mitigation: Keep QR codes, prices, dates, benefits, contact details, and compliance-sensitive text as human-added elements, then review against current WeChat Shop, Channels, and advertising rules before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/wechat-shop-ecommerce-image-generation-editing)
- [AI Hive API base URL](https://ai-hive.iclip.cn/api)
- [AI Hive API key setup page](https://ai-hive.iclip.cn/chat)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash command examples; CLI output includes JSON task responses and downloaded image files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an AI Hive API key, uploads user-selected reference media, submits image-generation tasks, polls task status, and downloads PNG results unless --no-download is used.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
