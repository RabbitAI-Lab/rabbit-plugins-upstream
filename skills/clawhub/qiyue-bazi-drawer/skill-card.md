## Description:

排八字命盘——输入出生年月日时与性别，输出四柱干支、日主、五行统计、命宫与大运。由栖月 QiyueAstro 提供，无需 API Key。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to generate a BaZi chart from birth date, birth time, and gender, then display the returned four pillars, daymaster, five-element counts, palaces, and fortune periods. The skill presents the API response without model-authored fortune interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided birth date, birth time, gender, and optional question text to qiyueastro.com.

Mitigation: Ask users to avoid sensitive details in the optional question and proceed only when they are comfortable sharing the required birth details with QiyueAstro.

Risk: Astrology chart output may be mistaken for advice.

Mitigation: Present the output as entertainment or self-exploration and avoid adding model-authored interpretation or decision guidance.

## Reference(s):

- [QiyueAstro homepage](https://qiyueastro.com)
- [QiyueAstro BaZi public API](https://qiyueastro.com/api/v1/openclaw/bazi)
- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-bazi-drawer)
- [ClawHub publisher profile](https://clawhub.ai/user/bloodymarygg)

## Skill Output:

**Output Type(s):** [API Calls, Markdown, Guidance]

**Output Format:** [Markdown summary of JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a QiyueAstro call-to-action and should avoid independent BaZi interpretation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
