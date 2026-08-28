## Description:

Guides agents through WeChat Mini Program development, including project structure, debugging, preview, publishing, CloudBase integration, message push, customer service auto-reply, and search optimization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, preview, deploy, publish, optimize, and promote WeChat Mini Program projects. It is especially relevant when work involves WeChat Developer Tools Nightly, wechatide, miniprogram-ci, CloudBase, wx.cloud, message push, customer service auto-reply, or WeChat search optimization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward IDE or CLI workflows that deploy cloud functions, modify cloud resources, or upload preview builds.

Mitigation: Review proposed actions before approving them in WeChat Developer Tools, wechatide, miniprogram-ci, CloudBase MCP, or related login and confirmation flows.

Risk: Generated Mini Program or CloudBase guidance could cause incorrect project configuration, broken previews, or unintended publishing behavior.

Mitigation: Check project.config.json, appid, miniprogramRoot, CloudBase environment IDs, and deployment gate requirements before preview, upload, publish, or cloud-resource changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Message Push & Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO & WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program SEO documentation](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program documentation](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline code, JSON examples, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents toward IDE, CLI, CloudBase, preview, upload, deployment, and publishing workflows that require user review or approval.]

## Skill Version(s):

1.28.43 (source: server release metadata; artifact frontmatter declares 2.32.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
