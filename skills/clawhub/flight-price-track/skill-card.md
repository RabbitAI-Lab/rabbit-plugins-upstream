## Description: <br>
机票降价监控与多平台比价助手，搜索多平台实时价格对比，支持航线搜索、指定航班精确比价、低价日历、降价监控，帮你把握最佳购票时机。暑期机票价格监控。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to search flight routes, compare real-time prices across multiple booking sources, identify cheaper travel dates, and prepare price-watch requests for later follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight search details such as city pairs, dates, and optional target prices are sent to external proxy services. <br>
Mitigation: Install only when that data flow is acceptable, and avoid using unrelated personal or corporate secrets for PROXY_TOKEN. <br>
Risk: Same-price booking results may place commission-linked sources first, and prices can change after the skill reports them. <br>
Mitigation: Review all returned platform options and confirm final price and booking terms on the destination booking page before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/flight-price-track) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON results and concise agent guidance with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include flight search results, platform price comparisons, low-price calendar summaries, and structured price-watch requests.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
