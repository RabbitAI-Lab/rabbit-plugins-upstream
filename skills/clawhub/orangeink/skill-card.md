## Description:

Helps draft and review simplified-Chinese WeChat articles, and turns Markdown into publish-ready HTML, a browser copy page, and a draft API request with static formatting checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aladooo](https://clawhub.ai/user/aladooo)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-language creators and developers use this skill to prepare, check, and format WeChat public-account articles from Markdown for editor paste or draft API integration. It does not publish articles or manage API credentials.

### Deployment Geography for Use:

Global (intended for Chinese-language WeChat public-account workflows)

## Known Risks and Mitigations:

Risk: The parity checker executes template scripts, including scripts from a caller-supplied HTML file or an optional remote template.

Mitigation: Use only trusted templates; leave OIMD_REMOTE_TEMPLATE unset unless remote template execution is explicitly accepted.

Risk: Static formatting checks cannot guarantee that an article will render or pass checks in the WeChat editor.

Mitigation: Review the generated page and self-check results in WeChat before publishing; fix reported errors first.

Risk: External images in draft API HTML may be filtered by WeChat.

Mitigation: Review the image list and upload images to WeChat's media library before submitting the draft.

## Reference(s):

- [orangeink release on ClawHub](https://clawhub.ai/aladooo/skills/orangeink)
- [Writing guide](references/writing-guide.md)
- [WeChat formatting rules](references/wechat-rules.md)
- [WeChat draft API notes](references/wechat-api.md)
- [WeChat draft/add API documentation](https://developers.weixin.qq.com/doc/service/api/draftbox/draftmanage/api_draft_add.html)
- [WeChat editor plugin specification](https://developers.weixin.qq.com/doc/subscription/guide/product/plugin_spec.html)

## Skill Output:

**Output Type(s):** [Markdown, HTML, JSON, Guidance]

**Output Format:** [Simplified-Chinese Markdown guidance, HTML article and copy page, draft request and validation metadata JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports static formatting checks and an image list; draft API integration and publication remain with the user.]

## Skill Version(s):

1.2.6 (source: server-resolved release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
