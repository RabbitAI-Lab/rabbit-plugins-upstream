## Description: <br>
抖音自动回复助手帮助抖音创作者、电商卖家和知识付费从业者配置关键词规则，用于自动回复评论、发送引荐码并引导私信转化。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[grcdevil-art](https://clawhub.ai/user/grcdevil-art) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External creators, sellers, brand operators, and knowledge-commerce users can use this skill to manage Douyin comment replies, keyword-triggered responses, and private-message lead routing from local configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks users to provide a full Douyin session cookie, which can grant broad account access if exposed or misused. <br>
Mitigation: Use a non-primary account where possible, avoid storing cookies in shell history, keep config files private, rotate cookies regularly, and prefer an official scoped API or OAuth flow if available. <br>
Risk: Automated replies and private messages can violate platform policy, trigger account controls, or create unwanted user contact. <br>
Mitigation: Set conservative reply delays and daily limits, review keyword responses before use, monitor douyin_bot.log and config.json, and stop automation if Douyin flags unusual activity. <br>
Risk: The artifact describes unfinished API integration while marketing text presents some capabilities as complete. <br>
Mitigation: Review the implementation before deployment, test with a low-risk account, and confirm that required Douyin API calls work in the intended environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/grcdevil-art/douyin-auto-reply) <br>
- [Publisher profile](https://clawhub.ai/user/grcdevil-art) <br>
- [Douyin API reference](references/api_docs.md) <br>
- [Troubleshooting guide](references/troubleshooting.md) <br>
- [Quickstart guide](assets/QUICKSTART.md) <br>
- [Douyin open platform documentation](https://open.douyin.com/platform/doc) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Code, Guidance] <br>
**Output Format:** [Markdown instructions with JSON configuration and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local configuration guidance, command examples, and Python automation behavior for Douyin comment and message workflows.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
