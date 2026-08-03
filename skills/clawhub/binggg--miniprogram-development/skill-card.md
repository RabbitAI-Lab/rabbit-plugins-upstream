## Description: <br>
Supports agents working on WeChat Mini Program projects, including project structure, pages and components, CloudBase integration when applicable, debugging, preview, upload, and release workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to build, modify, debug, preview, test, publish, and optimize WeChat Mini Program projects. It also guides CloudBase mini program integration when project evidence or the user request makes CloudBase relevant. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide preview, upload, publish, cloud writes, and authenticated CloudBase operations. <br>
Mitigation: Review those actions before approval and keep credentials in interactive tooling rather than committed configuration. <br>
Risk: WeChat Developer Tools Nightly and wechatide workflows may differ from stable tool behavior. <br>
Mitigation: Confirm Nightly availability and inspect tool help or the tool registry before using command flags. <br>
Risk: Mini Program changes can fail when project configuration, appid, or CloudBase environment settings are incorrect. <br>
Mitigation: Check project.config.json, appid, miniprogramRoot, and CloudBase environment before preview, upload, publish, or cloud operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/binggg/skills/miniprogram-development) <br>
- [CloudBase Mini Program Integration](artifact/references/cloudbase-integration.md) <br>
- [WeChat DevTools Debug and Preview](artifact/references/devtools-debug-preview.md) <br>
- [WeChat IDE Skills vs CloudBase MCP](artifact/references/wxide-vs-cloudbase-mcp.md) <br>
- [Common Pitfalls in WeChat Mini Program Development](artifact/references/pitfalls.md) <br>
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with code blocks, JSON and configuration examples, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide authenticated preview, upload, publish, and CloudBase operations that require user review.] <br>

## Skill Version(s): <br>
1.28.20 (source: server release metadata; artifact frontmatter version 2.25.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
