## Description: <br>
通过 Clawec API 查询 Shopee 店铺榜单（热销榜/飙升榜，天周月，本土/跨境）。在用户需要虾皮店铺榜、热销店铺、飙升店铺、类目竞店调研、站点店铺选品时使用。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce operators and analysts use this skill to query Shopee shop bestseller and fast-rising rankings by site, category, period, and shop type. It supports competitor research by returning ranked shop metrics such as sales, GMV, followers, ratings, and shop links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user's ClawEC API key and query parameters to clawec.com. <br>
Mitigation: Confirm the user accepts this data flow, read the key from the CLAWEC_API_KEY environment variable, and avoid hardcoding secrets. <br>
Risk: Returned Shopee ranking data is third-party business intelligence and may be incomplete, delayed, or unsuitable as a sole decision source. <br>
Mitigation: Present the results as ranking intelligence, include query conditions and dates, and encourage verification before business decisions. <br>


## Reference(s): <br>
- [Shopee shop ranking response schema](references/response-schema.md) <br>
- [ClawEC API base URL](https://www.clawec.com/api) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-shop-ranking) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown report with optional shell commands and API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is a Chinese shop-ranking report with query conditions, ranking table, competitor observations, and suggested shops to benchmark.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
