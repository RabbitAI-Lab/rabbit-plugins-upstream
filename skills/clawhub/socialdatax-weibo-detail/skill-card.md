## Description: <br>
用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve structured details for a single Weibo post, including content, author, media, publish time, interaction counts, and post URL when available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on a SocialDataX npm package and service that receives the user's SOCIALDATAX_API_KEY. <br>
Mitigation: Install and run it only when the user trusts SocialDataX and intends to use that API key for read-only Weibo post lookups. <br>
Risk: Optional media downloads can write files locally. <br>
Mitigation: Save media only to an output path or directory explicitly chosen by the user. <br>


## Reference(s): <br>
- [SocialDataX AI Access Page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub Skill Page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-detail) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY for SocialDataX data calls; detail access is described as read-only.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
