## Description: <br>
配置赢麻了 API 凭证、浏览官方技能与 Role 目录，或安装/更新其它官方技能与 Role 时使用。请先安装本技能，再由它管理其余条目。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jerryzhou](https://clawhub.ai/user/jerryzhou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to configure Winmale API credentials, discover official Winmale skills and roles, and install or update the local skill catalog. It is intended as a SkillHub manager rather than a direct financial analysis skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide credential setup and broad install or update flows that modify local agent behavior. <br>
Mitigation: Install only when you intend it to manage Winmale credentials and local skill directories; confirm official Winmale catalog sources before install, update_all, or credential rotation. <br>
Risk: Winmale API keys or tokenized deeplinks could be exposed in chat logs or repositories. <br>
Mitigation: Keep API keys out of chat and source control, avoid full key echoing, and avoid sharing tokenized links outside the intended conversation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jerryzhou/skills/wm-skillhub) <br>
- [Winmale public skill catalog](https://open.winmale.com/api/skills) <br>
- [Winmale SkillHub credentials](https://open.winmale.com/skillhub/creds) <br>
- [Winmale getting started](https://open.winmale.com/get-started) <br>
- [Error recovery guide](references/errors-recovery.md) <br>
- [Output reliability guide](references/output-hygiene.md) <br>
- [Units and values guide](references/units-and-values.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell, HTTP, JSON, and XS examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide credential setup, catalog discovery, local skill or role installation, update flows, and feedback/deeplink handling.] <br>

## Skill Version(s): <br>
1.0.29 (source: SKILL.md frontmatter, manifest.json, server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
