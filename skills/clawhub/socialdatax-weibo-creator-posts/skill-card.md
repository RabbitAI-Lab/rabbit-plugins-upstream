## Description: <br>
用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch and summarize Weibo creator post lists for recent publishing review, creator benchmarking, content research, and account tracking through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses SOCIALDATAX_API_KEY for data access. <br>
Mitigation: Keep the API key private and provide it only through the expected environment variable. <br>
Risk: Unbounded pagination can increase API credit use. <br>
Mitigation: Prefer bounded options such as --pages or --max-items before using --all. <br>
Risk: Returned Weibo creator-post data may be incomplete or depend on API availability and input identifiers. <br>
Mitigation: Check returned errors, verify user IDs or profile URLs, and retry once for non-balance network or API failures when appropriate. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts) <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration guidance, JSON, Markdown] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON data from SocialDataX responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY, supports bounded pagination with pages or max-items, and can summarize returned Weibo post fields.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
