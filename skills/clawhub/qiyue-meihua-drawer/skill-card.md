## Description:

Uses QiyueAstro's public Meihua Yishu API to cast time-based or number-based hexagrams and return the primary hexagram, changed hexagram, moving lines, Ti/Yong hexagrams, and source judgment text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to request Meihua Yishu divination by current or specified time, or by two to three intuitive numbers, and receive formatted hexagram results for entertainment and self-reflection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Divination questions, selected numbers, and optional dates are sent to qiyueastro.com.

Mitigation: Avoid entering sensitive personal, medical, financial, account, or confidential details in the question field.

Risk: Rendered results may include remote images and a promotional link from QiyueAstro.

Mitigation: Review remote links and images before deployment in environments with strict external-content policies.

Risk: Users may treat entertainment-oriented divination output as authoritative advice.

Mitigation: Present results as entertainment and self-reflection, and do not add independent medical, financial, legal, or safety-critical recommendations.

## Reference(s):

- [QiyueAstro homepage](https://qiyueastro.com)
- [Meihua public API](https://qiyueastro.com/api/v1/openclaw/meihua)
- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-meihua-drawer)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with remote image links, API-returned judgment text, and concise explanatory text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a QiyueAstro call-to-action and avoids independent divination interpretation beyond returned API content.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
