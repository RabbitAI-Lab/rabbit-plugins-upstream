## Description:

Helps agents build, debug, preview, publish, optimize, and promote WeChat Mini Program projects, including CloudBase integration when explicitly relevant.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to create, modify, debug, preview, test, publish, and optimize WeChat Mini Program projects. It also guides CloudBase, WeChat Developer Tools Nightly, miniprogram-ci, and WeChat search optimization workflows when those topics are relevant to the project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview, upload, publishing, or CloudBase write actions can affect WeChat Mini Program projects or cloud resources.

Mitigation: Review WeChat, Tencent Cloud, preview/upload, and cloud-write prompts before approving them, and confirm project.config.json, appid, project path, and cloud environment values first.

Risk: Long-lived credentials or cloud secrets could be exposed if embedded in project files.

Mitigation: Use interactive WeChat, Tencent Cloud, or device-code login flows where available, and avoid storing Secret ID, Secret Key, private keys, or environment secrets in source-controlled files.

Risk: Generated code or configuration may rely on the wrong execution surface or environment.

Mitigation: Prefer WeChat Developer Tools Nightly and wechatide for daily mini program workflows when available, use documented fallbacks only when needed, and verify environment state before changing or deploying code.

## Reference(s):

- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP / Skills](references/wxide-vs-cloudbase-mcp.md)
- [Mini Program SEO & WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls in WeChat Mini Program Development](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code blocks, shell commands, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose user-directed WeChat DevTools, miniprogram-ci, and CloudBase actions that should be reviewed before execution.]

## Skill Version(s):

1.28.31 (source: server release metadata; artifact frontmatter reports 2.28.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
