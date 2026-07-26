## Description: <br>
Guides agents through WeChat Mini Program development, including project structure, debugging, preview, testing, publishing, optimization, and CloudBase integration when applicable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build, modify, debug, preview, upload, and optimize WeChat Mini Program projects, including CloudBase-backed mini programs when the project uses wx.cloud or related CloudBase services. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Preview, upload, publish, database, storage, or cloud-function actions can target the wrong Mini Program appid or CloudBase environment. <br>
Mitigation: Confirm the intended appid, project path, and CloudBase environment before running DevTools, miniprogram-ci, or cloud-resource commands. <br>
Risk: DevTools or CloudBase workflows may prompt for WeChat scan login or device-code authentication. <br>
Mitigation: Review authentication prompts and authorize only the intended account and environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/miniprogram-development) <br>
- [CloudBase Mini Program Integration](references/cloudbase-integration.md) <br>
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md) <br>
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md) <br>
- [Common Pitfalls](references/pitfalls.md) <br>
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html) <br>
- [CloudBase WeChat Pay Mini Program Documentation](https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with code blocks and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose DevTools, miniprogram-ci, wechatide, or CloudBase MCP commands that require user approval and project-specific appid and environment values.] <br>

## Skill Version(s): <br>
1.28.15 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
