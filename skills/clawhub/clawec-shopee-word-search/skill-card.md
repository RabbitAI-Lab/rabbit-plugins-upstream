## Description: <br>
通过 Clawec API 查询 Shopee 热搜词列表（按站点/类目，含搜索指数、近30天销量销售额、推荐出价、产品数等筛选）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External cross-border ecommerce operators and agents use this skill to query Shopee site or category keyword rankings through the ClawEC API, then summarize search demand, recent sales, GMV, bid, and competition signals for keyword planning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the user's ClawEC API key and Shopee query parameters to the disclosed ClawEC API. <br>
Mitigation: Keep the key in the CLAWEC_API_KEY environment variable, avoid hardcoding it, and confirm users are comfortable with the ClawEC API before execution. <br>
Risk: Broad or unchecked filters can return misleading keyword opportunities or overly large result sets. <br>
Mitigation: Validate site, date, page size, category, and filter JSON before calling the API; keep pageSize at or below 100 and explain API errors clearly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-word-search) <br>
- [Shopee word search API endpoint](https://www.clawec.com/api/aigc/ec/shopee/data/word/search) <br>
- [Shopee hot word response schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown report with tables and optional shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Default output is Chinese and includes query conditions, keyword metrics, opportunity analysis, and recommended keywords.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
