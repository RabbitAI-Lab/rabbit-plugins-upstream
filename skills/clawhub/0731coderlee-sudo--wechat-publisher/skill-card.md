## Description: <br>
Publishes Markdown articles and referenced images to a WeChat Official Account draft box through wenyan-cli, with theme and code highlighting options. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0731coderlee-sudo](https://clawhub.ai/user/0731coderlee-sudo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and content teams use this skill to prepare and publish Markdown articles as WeChat Official Account drafts after configuring WeChat credentials, article frontmatter, themes, and image assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected Markdown content and referenced images are sent to WeChat when publishing a draft. <br>
Mitigation: Review the article, frontmatter, and image paths before running the publish workflow. <br>
Risk: WeChat AppID and AppSecret are required for publishing. <br>
Mitigation: Keep WECHAT_APP_SECRET out of git and shared logs, and prefer secure environment injection over plaintext credential files when possible. <br>
Risk: The publish script may install @wenyan-md/cli globally if wenyan is missing. <br>
Mitigation: Install or verify @wenyan-md/cli yourself before execution if you do not want the script to perform a global npm install. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/0731coderlee-sudo/skills/wechat-publisher) <br>
- [Publisher Profile](https://clawhub.ai/user/0731coderlee-sudo) <br>
- [wenyan-cli GitHub](https://github.com/caol64/wenyan-cli) <br>
- [wenyan Documentation](https://wenyan.yuzhi.tech) <br>
- [WeChat Official Account API Documentation](https://developers.weixin.qq.com/doc/offiaccount/) <br>
- [WeChat IP Whitelist Configuration](https://yuzhi.tech/docs/wenyan/upload) <br>
- [Theme Reference](references/themes.md) <br>
- [Troubleshooting Guide](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and WeChat draft publishing side effects] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Markdown article with required frontmatter, WeChat API credentials, a whitelisted IP address, Node.js, and wenyan-cli.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
