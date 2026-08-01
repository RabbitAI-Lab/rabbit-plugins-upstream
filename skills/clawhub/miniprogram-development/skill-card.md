## Description: <br>
WeChat Mini Program development skill for building, debugging, previewing, testing, publishing, optimizing projects, and handling CloudBase-specific mini program workflows when relevant. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to create, modify, debug, preview, test, upload, and optimize WeChat Mini Program projects. It also guides CloudBase integration when the project explicitly uses wx.cloud, Tencent CloudBase, or related mini program cloud workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may guide an agent through authenticated WeChat or Tencent Cloud sessions. <br>
Mitigation: Review authentication steps and approve only project-specific sessions needed for the current mini program workflow. <br>
Risk: Preview, upload, publishing, cloud write, or storage operations can affect live project resources. <br>
Mitigation: Require human review before cloud write or publishing actions, and complete the skill's deployment gate checks before upload or release. <br>
Risk: Incorrect appid, project path, or CloudBase environment selection can target the wrong mini program or cloud environment. <br>
Mitigation: Read project.config.json and resolve appid, miniprogramRoot, cloudbaseRoot, and env values from the project or tooling instead of using guessed defaults. <br>
Risk: Stable WeChat Developer Tools may not include Nightly Skills or the wechatide workflow. <br>
Mitigation: Confirm Nightly and wechatide availability before using those workflows, and fall back to miniprogram-ci or CloudBase MCP only when appropriate. <br>


## Reference(s): <br>
- [CloudBase Mini Program Integration](references/cloudbase-integration.md) <br>
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md) <br>
- [WeChat IDE Skills vs CloudBase MCP / Skills](references/wxide-vs-cloudbase-mcp.md) <br>
- [Common Pitfalls in WeChat Mini Program Development](references/pitfalls.md) <br>
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html) <br>
- [Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code blocks, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include project-specific checks for appid, environment IDs, project paths, preview/upload readiness, and CloudBase workflow selection.] <br>

## Skill Version(s): <br>
1.28.18 (source: ClawHub release metadata; artifact frontmatter: 2.25.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
