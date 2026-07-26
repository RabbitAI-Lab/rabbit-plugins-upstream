## Description: <br>
Compares hotel prices across 飞猪, 途牛, 同程, 美团, and RollingGo, returning hotel options, scores, distance details, breakfast and cancellation notes, and the lowest observed price. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and agent users use this skill to browse hotels in Chinese cities and compare a selected hotel's prices across multiple travel platforms before following a booking link. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel searches and travel dates are sent through the publisher's Tencent Cloud proxy and OTA providers. <br>
Mitigation: Use the skill only when that data flow is acceptable, and avoid entering sensitive itinerary details unless the publisher's proxy handling is trusted. <br>
Risk: Booking links may be monetized or tracked, and price data can change after the comparison result is shown. <br>
Mitigation: Treat booking links as potentially tracked and verify the final price, room type, cancellation policy, and platform terms on the booking page before purchase. <br>
Risk: The release was flagged as suspicious because it ships a backend proxy token and does not fully disclose monetized booking behavior. <br>
Mitigation: Review the security summary before deployment and consider rotating or removing exposed backend tokens before relying on the skill in managed environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-hotel-price-compare) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown-formatted text with hotel lists, prices, warnings, and booking links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include real-time prices, platform availability notes, and links to third-party booking pages.] <br>

## Skill Version(s): <br>
4.1.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
