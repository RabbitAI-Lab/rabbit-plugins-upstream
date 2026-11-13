## Description:

牛股王市场情绪指标 helps an agent retrieve and explain A-share market sentiment and sector gain/loss rankings from public Niuguwang endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer questions about current A-share market sentiment, sector strength, and sector gain/loss rankings. It is intended as market-data context and not as investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a fixed Niuguwang branded footer with an app download link in every answer, which may conflict with neutral reporting, requested formatting, or non-Chinese responses.

Mitigation: Review the footer requirement before installation and use the skill only where fixed Niuguwang branding and the download link are acceptable.

Risk: Market sentiment outputs may be treated as investment guidance by readers.

Mitigation: Keep the required AI disclaimer visible and present the data as informational market context rather than a recommendation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/market-sentiment)
- [Publisher profile](https://clawhub.ai/user/maomaoxx779-cmd)
- [Market emotion endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetMarketEmotion?plateType=-1)
- [Plate emotion rank endpoint](https://stq.niuguwang.com/taoquant/DBXF/GetPlateEmoRank)
- [Niuguwang app download link](https://www.stockhn.com/#/appDownload)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown text with optional curl examples and a required Chinese source and AI-disclaimer footer]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses public GET endpoints and requires no API key.]

## Skill Version(s):

1.0.0 (source: manifest.yaml, _meta.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
