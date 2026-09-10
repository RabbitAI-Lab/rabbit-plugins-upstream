## Description:

查询上期所、大商所、郑商所、中金所、广期所期货实时行情及历史 K 线。当用户说：螺纹钢主力什么价？豆粕期货涨了吗？SC 原油最近一周走势？或类似期货行情问题时，使用本技能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve real-time and historical futures market data for Shanghai, Dalian, Zhengzhou, China Financial Futures Exchange, and Guangzhou futures markets through JisuAPI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the JISU_API_KEY and futures query parameters to JisuAPI.

Mitigation: Use a dedicated API key for this service and install the skill only when sharing those query parameters with JisuAPI is acceptable.

Risk: Returned futures market data is third-party information.

Mitigation: Treat results as informational and verify important market data against an authoritative source before relying on it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/futures)
- [JisuAPI futures API documentation](https://www.jisuapi.com/api/futures/)
- [JisuAPI](https://www.jisuapi.com/)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a JISU_API_KEY environment variable; supports exchange-specific real-time queries and historical futures queries.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
