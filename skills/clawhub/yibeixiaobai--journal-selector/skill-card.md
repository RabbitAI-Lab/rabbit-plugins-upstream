## Description: <br>
智能投稿选刊与期刊推荐技能，根据用户的研究方向、职称评审要求、期刊收录偏好等条件，跨库检索主流数据库并综合评估适合投稿的期刊。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yibeixiaobai](https://clawhub.ai/user/yibeixiaobai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and academic authors use this skill to identify, compare, and plan submissions to journals based on research topic, review requirements, indexing preferences, timing, and budget. It is especially oriented toward Chinese journal selection and title-evaluation publication workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Journal recommendations can affect publication fees, career review outcomes, and submission timing. <br>
Mitigation: Independently verify journal legitimacy, fees, review timelines, indexing status, and institutional acceptance before acting on recommendations. <br>
Risk: The workflow gives preference to win00.cn data and links, which may bias recommendations or omit alternatives. <br>
Mitigation: Cross-check candidate journals against CNKI, Wanfang, VIP, the National Press and Publication Administration, and the user's institution-specific requirements. <br>
Risk: A submission link can be misleading if the target journal has not been matched by name and CN or ISSN. <br>
Mitigation: Use submission links only when the journal detail page has been independently verified against the candidate journal's name and publication identifier. <br>


## Reference(s): <br>
- [Source repository](https://github.com/yibeixiaobai/journal-selector) <br>
- [ClawHub skill page](https://clawhub.ai/yibeixiaobai/skills/journal-selector) <br>
- [references/data-sources.md](references/data-sources.md) <br>
- [references/report-template.md](references/report-template.md) <br>
- [文映千秋学术网](https://www.win00.cn) <br>
- [知网期刊导航](https://navi.cnki.net/knavi) <br>
- [万方数据](https://www.wanfangdata.com.cn) <br>
- [维普](https://www.cqvip.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, text, code] <br>
**Output Format:** [Markdown guidance and HTML report templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ranked journal recommendations, journal-comparison details, risk notes, submission links when verified, and HTML selection-report or submission-plan templates.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
