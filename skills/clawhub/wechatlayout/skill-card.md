## Description: <br>
微信公众号排版引擎把 Markdown 文章转换为可直接粘贴进微信公众号编辑器且样式不丢失的 HTML，并可从公众号文章 URL 提取视觉风格生成匹配的主题组件库。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qomob](https://clawhub.ai/user/qomob) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, operators, and developers use this skill to convert Markdown into WeChat-compatible article HTML with inline styles and platform checks. They can also extract a visual style from a public WeChat article URL and turn it into a reusable theme component library. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mode B fetches a user-provided public WeChat article URL. <br>
Mitigation: Use Mode B deliberately with public URLs, and provide local HTML instead when live fetching is inappropriate or fails. <br>
Risk: Generated themes can persist in the skill references directory and may overwrite existing theme names. <br>
Mitigation: Use clear output names and review generated theme files and registry updates before reuse. <br>
Risk: Generated article HTML may violate WeChat editor constraints if validation is skipped. <br>
Mitigation: Run the included validation workflow and require zero severe issues before publishing or pasting output. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qomob/skills/wechatlayout) <br>
- [Mode A formatting workflow](artifact/references/mode-a-format.md) <br>
- [Mode B style extraction workflow](artifact/references/mode-b-extract.md) <br>
- [Theme registry](artifact/references/theme-index.md) <br>
- [Common components](artifact/references/common-components.md) <br>
- [Paste test checklist](artifact/references/paste-test-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with WeChat-compatible HTML fragments, preview-page code, theme component files, and validation commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Mode A outputs inline-styled section HTML and a preview page; Mode B can generate persistent theme markdown files and update the theme registry.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
