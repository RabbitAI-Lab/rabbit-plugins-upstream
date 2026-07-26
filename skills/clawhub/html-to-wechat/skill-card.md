## Description: <br>
Publishes existing HTML from a file, URL, or pasted source to a WeChat Official Account draft box after compatibility checks, inline-style conversion, cover image compression, and credential-guided upload. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lutongsuo](https://clawhub.ai/user/lutongsuo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, content operators, and external users use this skill to publish prepared HTML into a WeChat Official Account draft workflow without manually converting styles or packaging cover images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow uses WeChat AppID/AppSecret credentials and uploads HTML and cover images to a WeChat Official Account draft box. <br>
Mitigation: Keep credentials out of source files and command history, prefer environment variables or interactive prompts, use a dedicated or least-privilege WeChat account where practical, and review the draft in WeChat before publishing. <br>
Risk: The artifact can install Python dependencies at runtime and relies on a companion skill for conversion and publishing. <br>
Mitigation: Prefer manually installing pinned dependencies, verify the companion skill before use, and review generated commands before execution. <br>


## Reference(s): <br>
- [HTML to WeChat ClawHub listing](https://clawhub.ai/lutongsuo/skills/html-to-wechat) <br>
- [WeChat Official Account Platform](https://mp.weixin.qq.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code snippets, file paths, and publishing status summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local HTML and cover-image files and submit a draft to WeChat when credentials and the companion skill are available.] <br>

## Skill Version(s): <br>
1.0.0 (source: artifact SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
