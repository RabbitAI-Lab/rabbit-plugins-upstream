## Description: <br>
Compares direct flight prices across Fliggy, Tuniu, Tongcheng, Meituan, and RollingGo, matching the same flight by flight number and returning booking links with the results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Travelers and travel-planning agents use this skill to compare real-time direct domestic flight prices for a route and date, identify the lowest available platform price, and review flight timing, airline, airport, and booking-link details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Flight route and date queries are sent through the publisher's Tencent Cloud proxy and onward to travel platforms. <br>
Mitigation: Use the skill only when that data flow is acceptable; avoid sensitive travel queries in environments that prohibit third-party proxying. <br>
Risk: The artifact includes a proxy token in source code. <br>
Mitigation: Review credential exposure before deployment and rotate, scope, or replace the token for managed or enterprise use. <br>
Risk: Flight prices and booking links are time-sensitive and may omit taxes, fees, or platform-specific fare conditions. <br>
Mitigation: Confirm final price and terms on the booking platform before purchase. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/travel-skills/skills/china-flight-price-compare) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown flight comparison results with platform prices, source labels, booking links, warnings, and plain text status messages when no results are available.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results are limited to direct flights and may include warnings about missing platforms, price differences, or platform-specific price caveats.] <br>

## Skill Version(s): <br>
4.2.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
