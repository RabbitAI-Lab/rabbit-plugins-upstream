## Description:

Guides coding agents through WeChat Mini Program development, debugging, preview and upload workflows, CloudBase integration, and WeChat search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to build, modify, debug, preview, upload, and optimize WeChat Mini Program projects, including CloudBase-backed projects when the project explicitly uses CloudBase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview, upload, publish, CloudBase write, and MCP configuration steps can affect real Mini Program or CloudBase resources.

Mitigation: Review those steps before approval, especially when account login, appid, environment IDs, upload keys, or write operations are involved.

Risk: Using the wrong execution path can lead to failed debugging or unintended cloud operations.

Mitigation: Confirm project configuration, appid, environment ID, and tool availability before following Nightly DevTools, miniprogram-ci, or CloudBase MCP guidance.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Mini Program SEO & WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html)
- [WeChat Mini Program Search Optimization](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with inline code, JSON snippets, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend preview, upload, CloudBase, and MCP configuration steps that should be reviewed before execution.]

## Skill Version(s):

1.28.32 (source: server release metadata; artifact frontmatter reports 2.28.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
