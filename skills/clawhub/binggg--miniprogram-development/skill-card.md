## Description:

Guides agents through WeChat Mini Program project structure, debugging, preview and upload workflows, CloudBase integration, message push, customer-service replies, and WeChat search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to build, modify, debug, preview, publish, and optimize WeChat Mini Programs, including CloudBase-specific workflows when the project uses CloudBase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CloudBase fallback guidance tells agents to run unpinned npm tools during cloud authentication and environment operations.

Mitigation: Review the CloudBase fallback steps before installing tools; prefer WeChat Developer Tools Nightly or pinned, locally reviewed versions of mcporter and CloudBase MCP before logging in, selecting environments, deploying functions, or uploading a mini program.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [Message Push and Customer Service Auto-Reply](references/message-push-customer-service.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Mini Program Pitfalls](references/pitfalls.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program SEO Documentation](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Documentation](https://docs.cloudbase.net/integration/wechat-pay-miniprogram.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration fragments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file edits, CLI workflows, or review checklists depending on the user's Mini Program task.]

## Skill Version(s):

1.28.62 (source: server release metadata; artifact frontmatter version: 2.34.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
