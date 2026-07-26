## Description: <br>
多旅游平台酒店比价与订房决策助手，帮你找到最便宜的酒店并告诉你该订还是再等等，含低价日历和订房建议，多旅游平台数据直连。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to compare hotel prices across multiple travel platforms, scan lower-price dates, and receive booking-timing guidance before following booking links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details are sent to the publisher's proxy service to retrieve live travel-platform data. <br>
Mitigation: Use the skill only for queries you are comfortable sharing with that service, and avoid entering sensitive personal information beyond search parameters. <br>
Risk: The release evidence warns that booking links may be monetized and equal-price results may favor a commission-linked source. <br>
Mitigation: Compare equal-price options directly on booking platforms before purchase and review whether ranking and affiliate behavior are acceptable for your use. <br>
Risk: The security evidence reports an embedded proxy credential. <br>
Mitigation: Prefer a release that removes the embedded token or requires operators to supply their own credential through deployment configuration. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/hotel-smart-book) <br>
- [Skill homepage](https://rollinggo.store) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown text with hotel search results, price comparisons, booking links, and booking-timing recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on live proxy-backed travel-platform data and should be checked against booking platforms before purchase.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; artifact frontmatter reports 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
