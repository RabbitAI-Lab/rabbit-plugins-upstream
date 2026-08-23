## Description:

Draw tarot cards from QiyueAstro -- one card, daily card, or any of 13 spreads; browse the full 78-card Rider-Waite deck and read card meanings in English or Chinese with no API key required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to draw tarot cards, browse Rider-Waite card details, choose spreads, and request optional QiyueAstro AI readings for entertainment and self-reflection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tarot questions and draw requests are sent to QiyueAstro, and explicit AI readings send the question to an external AI service.

Mitigation: Warn users before AI readings and advise them not to share highly sensitive personal details if they do not want those details processed externally.

Risk: Tarot outputs may be mistaken for factual, professional, or predictive advice.

Mitigation: Present the skill as entertainment and self-reflection, and display API-returned meanings without adding independent interpretation.

Risk: The external tarot service may rate-limit requests or become unavailable.

Mitigation: Retry rate-limit responses only once after a short wait and provide the documented unavailable-service message for other errors.

## Reference(s):

- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro OpenClaw API](https://qiyueastro.com/api/v1/openclaw)
- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-tarot-drawer)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown with card images, API-returned meanings, and optional AI reading Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses QiyueAstro API responses verbatim; supports en and zh_CN; optional AI interpretation quota is 2 per day per IP.]

## Skill Version(s):

1.0.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
