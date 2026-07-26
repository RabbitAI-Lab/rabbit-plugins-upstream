## Description: <br>
用于小红书数据助手、小红书搜索热榜、小红书数据分析、小红书笔记搜索、笔记详情、评论分析、博主数据和博主笔记。覆盖 Xiaohongshu / XHS / RedNote，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to retrieve and analyze Xiaohongshu / XHS / RedNote hot searches, notes, comments, creator profiles, and creator note lists through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: XHS queries and URLs are sent to SocialDataX using SOCIALDATAX_API_KEY. <br>
Mitigation: Use the skill only when this data sharing is acceptable, and keep the API key in the environment rather than embedding it in prompts or files. <br>
Risk: Returned Xiaohongshu note URLs may include token-like xsec_token query parameters. <br>
Mitigation: Share full note_url values only with intended recipients and avoid placing them in public chats, tickets, logs, or shared documents unless the exact link is needed. <br>


## Reference(s): <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and data-result guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and may return Xiaohongshu note URLs containing token-like query parameters.] <br>

## Skill Version(s): <br>
0.1.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
