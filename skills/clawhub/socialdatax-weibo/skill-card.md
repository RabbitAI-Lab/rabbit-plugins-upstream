## Description: <br>
用于微博数据助手、微博热搜、微博内容研究、帖子详情、评论分析、评论回复观察、转赞互动、创作者资料和创作者内容列表。覆盖 Weibo post research，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve read-only Weibo hot-search, post, comment, reply, engagement, creator profile, and creator post-list data through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses SOCIALDATAX_API_KEY with a CLI/API workflow. <br>
Mitigation: Install only when comfortable exposing the API key to SocialDataX, and keep key permissions and billing limits appropriate. <br>
Risk: The skill runs the npm package socialdatax-skills at latest. <br>
Mitigation: Review package trust before installation and pin or audit the package where deployment policy requires it. <br>


## Reference(s): <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and API-key setup guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY and node/npm to call the SocialDataX CLI or matching MCP tools.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
