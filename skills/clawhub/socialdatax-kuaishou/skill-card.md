## Description: <br>
用于快手数据助手、快手内容研究、作品研究、作品详情、评论分析、评论回复分析、达人数据和达人作品。覆盖 Kuaishou / Kwai short-video research，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to research Kuaishou/Kwai content, works, comments, replies, creators, and creator work lists through SocialDataX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The SocialDataX API key is exposed to the SocialDataX npm tool at runtime. <br>
Mitigation: Install and run the skill only in environments where sharing SOCIALDATAX_API_KEY with the SocialDataX CLI is acceptable. <br>
Risk: Examples use npx with @latest, so the executed package version can change over time. <br>
Mitigation: Pin or review the socialdatax-skills package version before use in stricter environments. <br>


## Reference(s): <br>
- [SocialDataX AI access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and CLI/MCP tool references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and examples call the SocialDataX npm CLI.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
