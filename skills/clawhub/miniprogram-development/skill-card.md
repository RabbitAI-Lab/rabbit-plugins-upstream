## Description: <br>
Guides agents through WeChat Mini Program project structure, CloudBase integration, debugging, preview, upload, publishing, and common implementation pitfalls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[binggg](https://clawhub.ai/user/binggg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to build, modify, debug, preview, publish, and optimize WeChat Mini Program projects, including CloudBase mini program integrations when the project uses CloudBase. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated WeChat Developer Tools, preview, upload, and CloudBase operations can affect real mini program or cloud resources. <br>
Mitigation: Use the skill only in trusted mini program workspaces, confirm project, appid, and environment values before write operations, and review DevTools or cloud write confirmations. <br>
Risk: Project files may accidentally retain long-lived secrets, upload keys, or cloud credentials. <br>
Mitigation: Prefer interactive login or device-code authentication where available, and keep credentials out of committed project files. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/binggg/skills/miniprogram-development) <br>
- [CloudBase Main Entry](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md) <br>
- [Current Skill Raw Source](https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/miniprogram-development/SKILL.md) <br>
- [CloudBase Mini Program Integration](references/cloudbase-integration.md) <br>
- [WeChat DevTools Debug and Preview](references/devtools-debug-preview.md) <br>
- [WeChat IDE Skills vs CloudBase MCP](references/wxide-vs-cloudbase-mcp.md) <br>
- [Common Pitfalls](references/pitfalls.md) <br>
- [WeChat Developer Tools Nightly](https://developers.weixin.qq.com/miniprogram/dev/devtools/nightly_backup.html) <br>
- [Mini Program CI](https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code, JSON snippets, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May route agents to additional CloudBase or WeChat Mini Program references based on the user's task.] <br>

## Skill Version(s): <br>
1.28.17 (source: ClawHub release metadata; artifact frontmatter states 2.25.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
