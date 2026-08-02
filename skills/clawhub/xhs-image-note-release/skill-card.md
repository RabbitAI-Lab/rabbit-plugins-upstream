## Description: <br>
Automates Xiaohongshu image-note publishing through ego-browser, including image upload, title and body entry, topic tags, publishing, and configurable card image generation with 28 visual styles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and content operators use this skill to generate Xiaohongshu-style image cards and publish image notes through a logged-in Xiaohongshu creator account. It is intended for agent-assisted publishing workflows where the user provides or approves the images, title, and body. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish to a live Xiaohongshu account using an existing logged-in browser session. <br>
Mitigation: Require explicit final confirmation of the title, body, image set, target account, and visibility before any publish action. <br>
Risk: The documentation includes sandbox-reduction guidance for environments where ego-browser is blocked. <br>
Mitigation: Avoid disabling sandboxing unless necessary for the chosen environment, understand the added exposure, and re-enable sandboxing after the publishing task. <br>
Risk: Some card themes may contact external font CDNs during card rendering. <br>
Mitigation: Run rendering in a network policy appropriate for the workspace, or review and replace external font loading before use in restricted environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/xhs-image-note-release) <br>
- [publish-method.md](references/publish-method.md) <br>
- [card_generator.py](references/card-generator/card_generator.py) <br>
- [Xiaohongshu creator publish page](https://creator.xiaohongshu.com/publish/publish) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell, JavaScript, and Python command examples; generated card images are written as PNG files when the card generator is used.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires IMAGE_DIR, IMAGES, TITLE, and BODY for the publishing script; publishing uses a logged-in browser session.] <br>

## Skill Version(s): <br>
1.5.0 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
