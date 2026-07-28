## Description: <br>
Guides agents through building, debugging, previewing, testing, publishing, and optimizing WeChat Mini Program projects, including CloudBase integration when the project explicitly uses it. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to create, modify, debug, preview, upload, and maintain WeChat Mini Program projects. It also guides CloudBase-specific coding and operations when the project uses `wx.cloud`, Tencent CloudBase, or related mini program cloud features. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through real preview, upload, publish, and CloudBase cloud-operation workflows. <br>
Mitigation: Grant only task-specific project, WeChat DevTools, and CloudBase access, and review each upload, publish, or cloud write action before approval. <br>
Risk: Incorrect project, appid, or environment assumptions can cause failed previews, uploads, or cloud operations. <br>
Mitigation: Confirm `project.config.json`, `miniprogramRoot`, `appid`, asset paths, and CloudBase environment before running DevTools or CI workflows. <br>
Risk: Tooling differences between Stable and Nightly WeChat Developer Tools can lead to unavailable commands or incomplete debugging. <br>
Mitigation: Check whether Nightly `wechatide` is available, discover command flags with `--help` or documented tool registries, and fall back to `miniprogram-ci` or CloudBase MCP only when appropriate. <br>


## Reference(s): <br>
- [CloudBase Mini Program Integration](references/cloudbase-integration.md) <br>
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md) <br>
- [WeChat IDE Skills vs CloudBase MCP / Skills](references/wxide-vs-cloudbase-mcp.md) <br>
- [Common Pitfalls in WeChat Mini Program Development](references/pitfalls.md) <br>
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html) <br>
- [WeChat DevTools Release Notes](https://developers.weixin.qq.com/miniprogram/dev/devtools/log.html#stable) <br>
- [Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, shell-command examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose project files, Mini Program configuration, DevTools commands, CloudBase setup steps, preview/upload workflows, and operational checks.] <br>

## Skill Version(s): <br>
1.28.16 (source: server release evidence; artifact frontmatter reports 2.25.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
