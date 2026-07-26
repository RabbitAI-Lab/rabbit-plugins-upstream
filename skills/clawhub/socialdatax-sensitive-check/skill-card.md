## Description: <br>
用于敏感词检测、违禁词检测、文案发布前检查、内容安全检查、文案合规审核、能不能发判断、平台风险提示和改写建议，支持小红书、抖音、快手和通用文本场景。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, marketers, and agents use this skill to check draft Chinese social content for sensitive or prohibited wording before publishing. It returns risk status, risk level, matched issue types, highlighted text, and safer rewrite suggestions for generic, Xiaohongshu, Douyin, and Kuaishou contexts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided draft text is sent to SocialDataX and may be retained with analysis results for disclosed operational purposes. <br>
Mitigation: Avoid submitting secrets or highly confidential drafts unless the user's SocialDataX account and policies permit that use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-sensitive-check) <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown summary for agent responses; CLI and MCP calls return JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY; avoid echoing the full submitted draft unless the user explicitly asks.] <br>

## Skill Version(s): <br>
0.1.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
