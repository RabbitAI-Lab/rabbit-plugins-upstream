## Description:

Guides agents through WeChat Mini Program development, including project structure, debugging, previews, publishing, CloudBase integration, message push, and search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to build, modify, debug, preview, test, publish, optimize, and promote WeChat Mini Program projects. It is also used for CloudBase mini program workflows when the project explicitly uses wx.cloud, Tencent CloudBase, or related cloud development features.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide agents toward authenticated developer tools that deploy cloud functions, manage cloud resources, create previews, and upload experience builds.

Mitigation: Review tool confirmations, verify project path, appid, and CloudBase environment before writes, and stop when the user declines or does not approve a tool action.

Risk: Secrets or access credentials could be exposed if stored in project files while configuring Mini Program, CloudBase, or CI workflows.

Mitigation: Use interactive login or approved credential mechanisms, and avoid writing secrets, private keys, or short-lived download URLs into source files.

## Reference(s):

- [CloudBase Mini Program Integration](artifact/references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](artifact/references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](artifact/references/wxide-vs-cloudbase-mcp.md)
- [Message Push and Customer Service Auto-Reply](artifact/references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](artifact/references/seo-search-optimization.md)
- [Common Mini Program Pitfalls](artifact/references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html)
- [WeChat Mini Program Search Optimization](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents toward authenticated developer tools for previews, cloud operations, and experience build uploads.]

## Skill Version(s):

1.28.44 (source: server release metadata; artifact frontmatter reports 2.32.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
