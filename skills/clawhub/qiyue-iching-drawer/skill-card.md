## Description:

用六爻（I Ching / 易经）起卦——三枚铜钱摇卦、时间起卦或数字起卦，展示卦名、卦辞、六爻爻辞、动爻与变卦。由栖月 QiyueAstro 提供，无需 API Key；支持免费 AI 解读（每 IP 每日 2 次）。

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to cast or browse I Ching hexagrams through QiyueAstro, display the returned original hexagram text, changing lines, and changed hexagram, and optionally request the service-provided AI interpretation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Questions sent for casting or AI interpretation go to QiyueAstro, and AI interpretation explicitly involves an external AI service.

Mitigation: Inform users before calling the interpretation endpoint and advise them not to submit highly sensitive personal information.

Risk: Responses may include QiyueAstro promotional links.

Mitigation: Preserve the link as service-provided output and make its promotional nature visible to users.

Risk: The skill is an I Ching lookup and interpretation helper, not a source of factual, medical, legal, financial, or safety-critical advice.

Mitigation: Use results for entertainment and self-exploration, and avoid treating hexagram text or interpretations as decision authority.

## Reference(s):

- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro I Ching API](https://qiyueastro.com/api/v1/openclaw/iching)
- [QiyueAstro AI Interpretation API](https://qiyueastro.com/api/v1/openclaw/interpret)
- [ClawHub Skill Page](https://clawhub.ai/bloodymarygg/skills/qiyue-iching-drawer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with API-returned hexagram text, image links, and optional service-provided AI interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include QiyueAstro promotional links and remaining daily AI interpretation count when returned by the API.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
