## Description: <br>
九赋产品溯源评级查询消费信任指数（CTI），帮助 agents assess product and brand trustworthiness, certifications, regulatory records, penalties, and related risk signals for consumer products. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiang19680401](https://clawhub.ai/user/jiang19680401) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to check whether a consumer product or brand appears trustworthy, including qualification, certification, regulatory, complaint, and penalty signals. The result is an informational CTI grade with key findings and risk alerts, not consumer advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Product names, brands, and categories submitted for lookup are sent to the disclosed jiufu-trace.cn verification API. <br>
Mitigation: Avoid submitting confidential product research, sensitive procurement plans, or private purchasing details unless that disclosure is acceptable. <br>
Risk: CTI results depend on public data and a third-party API, so records may be incomplete or stale. <br>
Mitigation: Present results as informational, include key risk flags, and avoid treating the output as definitive consumer, legal, or compliance advice. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/jiang19680401/skills/jiufu-cti) <br>
- [Jiufu CTI verification API](https://jiufu-trace.cn/api/cti/verify) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and structured CTI result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include CTI grade, score, verification dimensions, key findings, and risk flags from the Jiufu API.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
