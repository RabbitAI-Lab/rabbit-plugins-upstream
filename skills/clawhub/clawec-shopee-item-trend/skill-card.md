## Description: <br>
Queries the ClawEC API for Shopee item trend time series, including sales, GMV, price, rating, and engagement data by month, quarter, or year. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and ecommerce operators use this skill to fetch Shopee item trend data from ClawEC and produce Chinese product trend reports for competitor and item performance review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [Response schema](artifact/references/response-schema.md) <br>
- [ClawHub listing](https://clawhub.ai/anyunzhong/skills/clawec-shopee-item-trend) <br>
- [ClawEC API key page](https://www.clawec.com/api-key?source=q-clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown report with optional shell command and API request snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY in the environment; item query parameters and the bearer API key are sent to ClawEC, so users should submit only intended trend queries and avoid hardcoding credentials.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
