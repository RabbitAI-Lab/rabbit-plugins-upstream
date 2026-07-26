## Description: <br>
Deprecated WeChat article image helper that generates cover, comparison, and chart visuals from prebuilt HTML templates and directs users to yuanzi-wechat-suite for maintained workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golikegod](https://clawhub.ai/user/golikegod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and content creators use this skill to produce WeChat article covers, comparison graphics, and simple chart visuals from local HTML templates. The release is deprecated and points users to yuanzi-wechat-suite for the maintained four-step WeChat workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The screenshot helper can pass crafted file paths through an unsafe shell command. <br>
Mitigation: Avoid scripts/auto_screenshot.py unless reviewed and patched to call browser tooling with argument lists and local-file input restrictions. <br>
Risk: The release is deprecated and no longer maintained. <br>
Mitigation: Prefer yuanzi-wechat-suite 2.1.0 for maintained WeChat writing, image generation, and publishing workflows. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/golikegod/skills/wechat-image-generator) <br>
- [Publisher profile](https://clawhub.ai/user/golikegod) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Files, Guidance] <br>
**Output Format:** [Markdown with inline bash commands and generated HTML or image file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3; screenshot capture depends on a browser or browser automation tool.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
