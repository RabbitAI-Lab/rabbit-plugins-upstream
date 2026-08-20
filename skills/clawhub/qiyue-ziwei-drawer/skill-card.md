## Description:

排紫微斗数命盘——输入出生年月日时与性别，输出五行局与十二宫主星（命宫/财帛/官禄等）。由栖月 QiyueAstro 提供，无需 API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to draw a Zi Wei Dou Shu chart from birth date, birth hour, and gender, then present the returned Five Elements class and twelve palace star data. The skill is for chart display and does not provide model-generated fortune interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends birth date, birth hour, gender, and optional question text to qiyueastro.com to generate the chart.

Mitigation: Avoid entering unnecessary personal details in the optional free-text question field and install only if this external API data sharing is acceptable.

Risk: Users may mistake chart display for authoritative advice or model-generated interpretation.

Mitigation: Present only the API-returned chart data and avoid adding independent judgement, fortune interpretation, or claims beyond the returned palace and star fields.

## Reference(s):

- [QiyueAstro homepage](https://qiyueastro.com)
- [QiyueAstro Zi Wei public API](https://qiyueastro.com/api/v1/openclaw/ziwei)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summary of API-returned chart data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Displays birth chart fields returned by QiyueAstro and ends with a QiyueAstro call to action; no local files or executable code are produced.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
