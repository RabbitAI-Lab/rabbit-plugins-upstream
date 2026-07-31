## Description: <br>
基于聚合数据星座 API，为用户在付费确认后查询十二星座档案及日、周、月、年运势，并以 Markdown 输出结果。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[juhemcp](https://clawhub.ai/user/juhemcp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill through an agent to request paid horoscope profile and fortune lookups for a specified zodiac sign and period. The skill is intended for entertainment-oriented constellation information, with payment consent before results are retrieved. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a paid Alipay lookup flow before returning horoscope results. <br>
Mitigation: Review the payment prompt carefully and proceed only after the user has confirmed the charge and lookup. <br>
Risk: The lookup sends the selected zodiac sign and period to Juhe's API. <br>
Mitigation: Disclose that data transfer to the user and avoid sending unrelated personal or sensitive information. <br>
Risk: Horoscope and personality content may be mistaken for decision guidance. <br>
Mitigation: Present results as entertainment-only and avoid using them for medical, financial, legal, career, or relationship decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/juhemcp/skills/juhe-constellation-a2a) <br>
- [Output format reference](artifact/OUT_FORMAT.md) <br>
- [Juhe A2A query endpoint](https://apis.juhe.cn/a2a/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Text, Guidance] <br>
**Output Format:** [Markdown with structured sections and tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Paid lookup flow; horoscope content is entertainment-only and rendered from provider API fields.] <br>

## Skill Version(s): <br>
1.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
