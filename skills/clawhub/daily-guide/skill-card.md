## Description:

今日宜出门 - 黄历+农历+天气综合出门建议。用户问「今天适合出门吗/宜出门/黄历/今日宜忌/适合买东西吗」时使用。结合个人八字（生肖冲煞）给定制化建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhangmengyang](https://clawhub.ai/user/zhangmengyang)

### License/Terms of Use:

MIT-0

## Use Case:

External users ask whether today is suitable for going out, shopping, errands, travel, or other daily activities. The skill combines Chinese almanac data, lunar calendar signals, weather, and an optional local birth profile to provide concise guidance and cautions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores birth date, time, and city in a local profile file for personalized astrology-style guidance.

Mitigation: Run initialization only if comfortable storing that profile locally, check ~/.daily-guide/bazi.json after setup, and delete it when it is no longer needed.

Risk: The skill makes external weather and almanac requests that may reveal request timing or configured location context.

Mitigation: Review the configured city and network behavior before use, and avoid running the skill in environments where those requests are not acceptable.

Risk: Guidance is based partly on traditional almanac and astrology-style signals that can conflict across sources.

Mitigation: Treat results as reference guidance, review any displayed source disagreements, and avoid using the output as a sole basis for important decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhangmengyang/skills/daily-guide)
- [Publisher profile](https://clawhub.ai/user/zhangmengyang)
- [lunar-javascript package](https://registry.npmmirror.com/lunar-javascript/-/lunar-javascript-1.7.7.tgz)
- [Tianqi almanac data endpoint](https://staticwnl.tianqistatic.com/Home/js/api/yjs/${year}.js)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Human-readable text or structured JSON from the included Node.js scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use a local birth-profile file for personalization and weather/almanac network requests for current context.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
