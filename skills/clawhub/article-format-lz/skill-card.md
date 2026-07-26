## Description: <br>
Generates platform-compatible HTML layouts for WeChat public account and Toutiao articles, selecting article components, style palettes, and semantic markup from the user's content or publishing target. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[liuzheng60](https://clawhub.ai/user/liuzheng60) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, editors, and agents preparing Chinese self-media articles use this skill to turn article drafts or topics into publishable WeChat or Toutiao HTML layouts with appropriate visual hierarchy, platform-specific markup, and copy-ready preview pages. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML may not render exactly as expected after being pasted into WeChat or Toutiao editors. <br>
Mitigation: Review the generated HTML in the target editor before publishing, as recommended by the security guidance. <br>
Risk: Generated article files may collide with existing files in the working directory. <br>
Mitigation: Check the output filename and path before accepting or publishing generated files. <br>
Risk: Publish-ready formatting can make draft content appear final even when the article text still needs editorial review. <br>
Mitigation: Review the article content and generated layout before publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/liuzheng60/skills/article-format-lz) <br>
- [Publisher profile](https://clawhub.ai/user/liuzheng60) <br>
- [Design system reference](artifact/references/design-system.md) <br>
- [WeChat article HTML template](artifact/assets/template.html) <br>
- [Toutiao article HTML template](artifact/assets/toutiao-template.html) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Guidance] <br>
**Output Format:** [HTML files with platform-specific article markup and concise usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates local wechat-{topic}.html or toutiao-{topic}.html files; preview scripts support copying formatted article content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
