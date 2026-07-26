## Description: <br>
TrendRadar scans 小红书, 微博, Reddit, Google Trends, and Product Hunt to spot trending products before they peak, assigning a trend direction and a buy, wait, or skip signal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jiajiaoy](https://clawhub.ai/user/jiajiaoy) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and shopping agents use TrendRadar to identify rising consumer-product trends across social, search, and product-launch platforms, then decide whether to investigate, buy, wait, or skip an item. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trend-related phrases can trigger the skill when the user intended a different shopping or travel workflow. <br>
Mitigation: Invoke it with explicit product-trend wording and defer price analysis, coupon searches, and travel questions to the relevant sibling skills. <br>
Risk: Live searches and browsing can send query terms or browsing activity to third-party trend and social platforms. <br>
Mitigation: Avoid sensitive or personal search terms and review the platform targets before running scans. <br>
Risk: Trend rankings and commercial signals may be incomplete or time-sensitive because they depend on live platform availability and current public signals. <br>
Mitigation: Treat the output as discovery guidance and verify source evidence before making purchase or business decisions. <br>


## Reference(s): <br>
- [TrendRadar on ClawHub](https://clawhub.ai/jiajiaoy/skills/trendradar) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [BuyWise](https://github.com/jiajiaoy/BuyWise) <br>
- [CouponClaw](https://github.com/jiajiaoy/CouponClaw) <br>
- [NewsToday](https://github.com/jiajiaoy/NewsToday) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown trend briefings with product rankings, trend directions, commercial signals, and follow-up shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can be generated in English or Chinese and can target China, United States, global, or all-region scans.] <br>

## Skill Version(s): <br>
1.1.5 (source: package.json, _meta.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
