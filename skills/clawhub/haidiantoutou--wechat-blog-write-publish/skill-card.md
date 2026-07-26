## Description: <br>
Creates WeChat Official Account articles from user-provided reference materials, saves them as Markdown, and helps publish them to a WeChat draft box. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[haidiantoutou](https://clawhub.ai/user/haidiantoutou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators and developers use this skill to turn webpages, documents, PDFs, and other reference material into formatted WeChat Official Account draft articles. It also guides setup and use of wenyan-cli for publishing drafts with WeChat account credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: WeChat AppSecret or other account credentials could be exposed if copied into shared files, prompts, logs, or repositories. <br>
Mitigation: Treat the AppSecret like a password, configure it only in trusted local environments, and remove credentials from shared artifacts before publication. <br>
Risk: Generated articles or assets could include unapproved, private, proprietary, or inaccurate material. <br>
Mitigation: Review the generated Markdown, images, references, and draft content before publishing or moving the draft into public release. <br>
Risk: Publishing commands can act on the wrong WeChat Official Account or fail because required platform settings are incomplete. <br>
Mitigation: Confirm the active wenyan-cli configuration, target account, cover asset path, and WeChat IP allowlist before running publish commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/haidiantoutou/skills/wechat-blog-write-publish) <br>
- [WeChat Official Account developer documentation](https://developers.weixin.qq.com/doc/offiaccount/Getting_Started/Overview.html) <br>
- [WeChat Official Account backend](https://mp.weixin.qq.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown article files with front matter, Mermaid diagrams when useful, and inline shell commands for wenyan-cli publishing.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local .wxgzh publishing artifacts such as rendered HTML, cover images, and publish-result.json.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
