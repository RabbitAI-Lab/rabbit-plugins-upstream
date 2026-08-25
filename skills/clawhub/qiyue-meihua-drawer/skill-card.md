## Description:

Qiyue Meihua Drawer helps an agent cast Meihua Yishu hexagrams by time or user-provided numbers, then display the returned primary hexagram, changed hexagram, moving lines, Ti/Yong information, and source text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bloodymarygg](https://clawhub.ai/user/bloodymarygg)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to ask Meihua Yishu divination questions and receive the original hexagram, moving-line, changed-hexagram, and Ti/Yong details returned by QiyueAstro. Agents may request the free AI interpretation endpoint only when the user explicitly asks and after a privacy notice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: User questions and casting inputs may be sent to qiyueastro.com, and AI interpretation requests may involve external AI processing.

Mitigation: Tell users before calling the interpretation endpoint and advise them not to enter sensitive personal, health, financial, legal, or confidential details.

Risk: Divination output or AI interpretation could be mistaken for authoritative advice.

Mitigation: Frame the skill as entertainment and self-exploration, show casting endpoint results verbatim, and avoid independent model interpretation unless the user explicitly requests the AI interpretation endpoint.

Risk: The remote service can be unavailable or rate limited.

Mitigation: Follow the documented error handling: retry 429 responses only once after waiting, do not repeatedly retry other errors, and direct users to QiyueAstro when the service is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/bloodymarygg/skills/qiyue-meihua-drawer)
- [Publisher profile](https://clawhub.ai/user/bloodymarygg)
- [QiyueAstro homepage](https://qiyueastro.com)
- [QiyueAstro Meihua API](https://qiyueastro.com/api/v1/openclaw/meihua)
- [QiyueAstro AI interpretation API](https://qiyueastro.com/api/v1/openclaw/interpret)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and plain text responses containing API-returned hexagram data and optional AI interpretation Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include remote image URLs and QiyueAstro links returned by the service; does not produce local files.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
