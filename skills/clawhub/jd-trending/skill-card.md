## Description: <br>
京东实时热销榜商品查询，展示当前畅销自营好货，好评>=98%品质精选，支持品类搜索、价格筛选、多种排序，发现大家都在买什么。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers use this skill to query real-time JD self-operated product rankings, filter by category and price, sort by score, price, or discount, and review product links before buying. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The configured proxy endpoint may receive proxy credentials and user shopping queries. <br>
Mitigation: Install only when the publisher and configured HTTPS proxy endpoint are trusted, and verify PROXY_URL before use. <br>
Risk: Shopping queries may include sensitive personal details. <br>
Mitigation: Avoid entering sensitive personal information and use explicit JD ranking prompts for intended shopping lookup tasks. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-trending) <br>
- [京东自营超级补贴](https://clawhub.ai/cn-shopping/jd-super-deals) <br>
- [京东自营历史最低价](https://clawhub.ai/cn-shopping/jd-lowest-price) <br>
- [购物比价助手](https://clawhub.ai/cn-shopping/best-price) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, links] <br>
**Output Format:** [JSON object with a human-readable summary and a JSON-encoded product list] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include product image URLs and purchase links; results can change as real-time rankings change.] <br>

## Skill Version(s): <br>
0.4.2 (source: server release evidence; artifact frontmatter and _meta.json report 0.4.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
