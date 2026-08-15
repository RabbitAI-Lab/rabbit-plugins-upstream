## Description:

Helps coding agents build, debug, preview, publish, optimize, and promote WeChat Mini Program projects, including project configuration, DevTools workflows, CloudBase integration, and WeChat search optimization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and coding agents use this skill to create, modify, troubleshoot, preview, and release WeChat Mini Programs. It is especially useful for projects that need correct Mini Program structure, WeChat Developer Tools or miniprogram-ci workflows, CloudBase integration, and crawler-friendly WeChat search behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview, upload, publish, and CloudBase workflows can affect real Mini Program or cloud resources.

Mitigation: Use the skill only in trusted projects, verify appid, project paths, and environment IDs, and require explicit confirmation before deployment, upload, publish, or cloud-write actions.

Risk: DevTools and cloud workflows may require WeChat or Tencent Cloud login.

Mitigation: Use official interactive login flows and avoid embedding credentials or hard-coding secret IDs, secret keys, temporary URLs, or environment identifiers into source files.

Risk: Incorrect assumptions about WeChat Mini Program APIs, CloudBase auth, or DevTools tool names can produce broken guidance or unsafe operations.

Mitigation: Check project.config.json, appid, miniprogramRoot, CloudBase usage, and available wechatide or miniprogram-ci parameters before proposing commands or code changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [Mini Program SEO and WeChat Search Optimization](references/seo-search-optimization.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Common Pitfalls](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program Search SEO](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program Integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with code, JSON, XML, CSS, and shell command snippets when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local file edits, DevTools or miniprogram-ci commands, CloudBase configuration, and release or SEO checklists; write, upload, preview, login, and cloud operations require project context and user confirmation.]

## Skill Version(s):

1.28.30 (source: ClawHub release metadata; artifact frontmatter reports 2.27.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
