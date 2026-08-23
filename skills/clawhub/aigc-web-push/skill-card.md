## Description:

支持通过 AI 生成文章和图文卡片，并推送到微信公众号（无需泄露公众号 Secret，无需配置 IP 白名单）或经由云电脑推送至全球任意站点；兼容其它技能产出的文章、图片与视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[lihengdao](https://clawhub.ai/user/lihengdao)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, operators, and developers use this skill to generate article or card-style HTML, adapt prose to read less like AI output, and publish HTML, image links, or video URLs to WeChat Official Accounts or configured cloud-computer targets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or deleting account content can affect real WeChat or cloud-computer targets.

Mitigation: Require explicit user confirmation of the target account or instance, publish mode, and cleanupDrafts action before running push or cleanup commands.

Risk: config.json contains credential-like routing data such as openId, skillKey, accounts, and instances.

Mitigation: Treat config.json as sensitive, keep it out of logs and repositories, and install the skill only if the user trusts the pcloud.ac.cn service with publishing content and routing data.

Risk: A custom apiBase can route publishing data to an untrusted or plain HTTP endpoint.

Mitigation: Use the default HTTPS endpoint or another verified HTTPS endpoint, and avoid plain HTTP or untrusted apiBase values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lihengdao/skills/aigc-web-push)
- [Configuration wizard](https://app.pcloud.ac.cn/design/aigc-web-push.html)
- [Cloud computer management](https://app.pcloud.ac.cn/design/#/manage?tab=server)
- [PCloud Open Access Service API endpoint](https://api.pcloud.ac.cn/openAccessService)
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [Skill usage guide](artifact/SKILL.md)
- [HTML design specification](artifact/design.md)
- [Example configuration](artifact/config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with HTML, JSON configuration, and Node.js shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or route HTML, image URL lists, video URLs, and push commands that rely on a local config.json.]

## Skill Version(s):

3.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
