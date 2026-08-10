## Description:

WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, and optimizing mini program projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, preview, test, publish, and optimize WeChat Mini Program projects, including project structure, page/component files, tab bars, routing, assets, DevTools workflows, and CloudBase integration when the project uses it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recommended workflows can open WeChat Developer Tools, authenticate to WeChat or CloudBase, preview or upload builds, and modify cloud resources.

Mitigation: Review proposed tool calls, project paths, appid values, environment IDs, and confirmation prompts before approving execution.

Risk: Applying CloudBase-specific guidance to a mini program that does not use CloudBase can introduce unnecessary configuration or incorrect architecture.

Mitigation: Confirm the project uses CloudBase or wx.cloud before applying CloudBase auth, database, storage, or cloud function rules.

Risk: Using guessed wechatide tool names, flags, app IDs, or environment IDs can produce failed previews, uploads, or cloud operations.

Mitigation: Discover tool parameters with help output or bundled tool registries, and resolve appid and env values from project configuration or supported tooling.

## Reference(s):

- [CloudBase Mini Program Integration](artifact/references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](artifact/references/devtools-debug-preview.md)
- [Common Pitfalls in WeChat Mini Program Development](artifact/references/pitfalls.md)
- [WeChat IDE Skills vs CloudBase MCP / Skills](artifact/references/wxide-vs-cloudbase-mcp.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline code blocks and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include project file edits, CLI commands, preview/upload guidance, and CloudBase workflow recommendations depending on the user's request.]

## Skill Version(s):

1.28.28 (source: server release metadata; artifact frontmatter declares 2.26.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
