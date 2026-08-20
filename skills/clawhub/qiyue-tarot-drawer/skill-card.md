## Description:

Draw tarot cards from QiyueAstro, including one card, daily card, or any of 13 spreads, and browse the full 78-card Rider-Waite deck with meanings in English or Chinese without an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users invoke this skill to draw tarot cards, browse Rider-Waite cards and spreads, and display QiyueAstro API-returned meanings in English or Chinese for entertainment and self-reflection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tarot requests and optional question text are sent to QiyueAstro's public API.

Mitigation: Do not include sensitive personal, medical, financial, account, or other confidential information in readings.

Risk: Card images are loaded from QiyueAstro URLs.

Mitigation: Use the skill only when external image loads to QiyueAstro are acceptable.

Risk: Tarot output is intended for entertainment and self-reflection.

Mitigation: Do not treat readings as medical, financial, legal, or other professional advice.

## Reference(s):

- [QiyueAstro](https://qiyueastro.com)
- [QiyueAstro OpenClaw API base](https://qiyueastro.com/api/v1/openclaw)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with API-returned text and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include card image URLs and API-returned tarot meanings; no local files are written.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
