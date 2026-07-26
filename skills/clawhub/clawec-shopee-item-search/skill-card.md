## Description: <br>
Uses the ClawEC API to search Shopee item lists by marketplace site, category, sales, GMV, price, seller type, and other filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce analysts, and agents use this skill to query recent Shopee item performance for selected sites and categories. It helps produce Chinese product tables, opportunity observations, and sourcing recommendations from ClawEC data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Shopee query parameters and a ClawEC API key to ClawEC. <br>
Mitigation: Use it only with an approved ClawEC account and keep the API key in the CLAWEC_API_KEY environment variable rather than hard-coding it. <br>
Risk: Results depend on the selected site, category, filters, and the ClawEC API response. <br>
Mitigation: Review request parameters and response errors before relying on product recommendations or sourcing conclusions. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/anyunzhong/skills/clawec-shopee-item-search) <br>
- [Response schema](references/response-schema.md) <br>
- [ClawEC Shopee item search endpoint](https://www.clawec.com/api/aigc/ec/shopee/data/item/search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Chinese Markdown report with optional curl or shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses CLAWEC_API_KEY for authenticated ClawEC requests and limits query page size to 10 items.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
