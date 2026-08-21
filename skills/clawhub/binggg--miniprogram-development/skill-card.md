## Description:

WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, optimizing, and promoting mini program projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[binggg](https://clawhub.ai/user/binggg)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build, modify, debug, preview, publish, optimize, and promote WeChat Mini Program projects. It also guides CloudBase mini program integration, WeChat Developer Tools Nightly workflows, miniprogram-ci fallbacks, and search indexing considerations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Preview, upload, publish, and CloudBase operations may use authenticated WeChat or Tencent Cloud tooling.

Mitigation: Review the proposed operation, target project, appid, environment, and destination before approving any authenticated action.

Risk: Generated mini program changes can fail if project configuration, required page files, or local asset paths are inconsistent.

Mitigation: Check project.config.json, miniprogramRoot, appid, page JSON files, and referenced assets before previewing, uploading, or publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/binggg/skills/miniprogram-development)
- [Publisher profile](https://clawhub.ai/user/binggg)
- [CloudBase Mini Program Integration](references/cloudbase-integration.md)
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md)
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md)
- [Mini Program SEO & WeChat Search Optimization](references/seo-search-optimization.md)
- [Common Pitfalls in WeChat Mini Program Development](references/pitfalls.md)
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html)
- [WeChat Mini Program SEO documentation](https://developers.weixin.qq.com/miniprogram/dev/framework/search/seo.html)
- [CloudBase WeChat Pay Mini Program integration](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with inline code blocks and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend authenticated WeChat Developer Tools, miniprogram-ci, or CloudBase operations that require user review before execution.]

## Skill Version(s):

1.28.36 (source: ClawHub release evidence; artifact frontmatter reports 2.31.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
