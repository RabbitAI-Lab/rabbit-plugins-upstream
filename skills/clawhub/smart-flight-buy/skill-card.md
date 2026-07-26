## Description: <br>
多旅游平台机票比价与购票决策助手，帮你找到最便宜的机票并告诉你该买还是再等等，含低价日历和降价监控，多旅游平台数据直连。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to compare domestic flight prices, inspect low-price calendar options, and generate buy, wait, or watch guidance. It can also emit a monitor task for a host agent to perform scheduled price checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight search details such as route and date are sent to the publisher's proxy service for live pricing. <br>
Mitigation: Use the skill only when sending those travel search details to the publisher-operated proxy is acceptable. <br>
Risk: The security scan reports an embedded shared fallback proxy token despite the artifact claiming no hardcoded secrets. <br>
Mitigation: Review credential handling before installation and prefer a user-supplied PROXY_TOKEN where the host environment supports it. <br>
Risk: Purchase advice depends on live third-party prices and heuristic route/date rules, so it may be incomplete or change quickly. <br>
Mitigation: Confirm price, routing, restrictions, and final purchase terms on the booking platform before buying. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/smart-flight-buy) <br>
- [Publisher profile](https://clawhub.ai/user/travel-skills) <br>
- [Skill homepage](https://rollinggo.store) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Configuration, Guidance] <br>
**Output Format:** [JSON objects containing flight options, low-price calendar entries, booking-advice signals, or monitor task details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results are capped to the first 20 flights; calendar scans are capped at 30 days.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
