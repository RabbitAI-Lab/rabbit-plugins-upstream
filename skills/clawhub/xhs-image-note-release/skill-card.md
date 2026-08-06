## Description: <br>
Automates Xiaohongshu image-note publishing through ego-browser, including image upload, title and body entry, topic selection, publishing, and optional generation of styled image cards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External creators and agent users use this skill to prepare styled Xiaohongshu image cards and automate publishing image-note posts from a logged-in Xiaohongshu creator session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can publish real content through a logged-in Xiaohongshu creator session without a separate dry-run or final confirmation gate. <br>
Mitigation: Review the target account, images, title, body, topics, and visibility settings before running the publish script. <br>
Risk: The card generator may fetch fonts from external CDNs for some themes. <br>
Mitigation: Run card generation only in environments where external font fetching is acceptable, or review generated cards for font fallback before publishing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/xhs-image-note-release) <br>
- [Publish method reference](references/publish-method.md) <br>
- [Card generator script](references/card-generator/card_generator.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with shell and JavaScript snippets; generated image cards are PNG files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ego-browser with an active logged-in Xiaohongshu creator session; card generation may use Chrome or Chromium and may fetch fonts from external CDNs.] <br>

## Skill Version(s): <br>
1.5.2 (source: release evidence, SKILL.md body, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
