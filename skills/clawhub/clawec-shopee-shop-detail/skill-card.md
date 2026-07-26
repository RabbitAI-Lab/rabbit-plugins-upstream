## Description: <br>
Queries Shopee shop details in batches through the Clawec API, returning sales, GMV, sales rate, followers, category, ratings, and other shop metrics for up to 10 shop IDs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce analysts, and agents use this skill to fetch known Shopee shop IDs by site, compare store performance, and produce concise operating observations from shop-detail metrics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow sends queried Shopee shop IDs and a ClawEC API key to the ClawEC API. <br>
Mitigation: Confirm ClawEC is acceptable for the workflow, keep the API key in the CLAWEC_API_KEY environment variable, and avoid hardcoding it in files or prompts. <br>


## Reference(s): <br>
- [Shopee shop detail response schema](references/response-schema.md) <br>
- [ClawEC API base URL](https://www.clawec.com/api) <br>
- [Shopee shop detail endpoint](https://www.clawec.com/api/aigc/ec/shopee/data/shop/detail) <br>
- [ClawHub skill page](https://clawhub.ai/anyunzhong/skills/clawec-shopee-shop-detail) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Chinese Markdown report with optional curl or shell command snippets and structured shop metrics] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY; accepts a Shopee site code, up to 10 comma-separated shop IDs per request, and an optional yyyy-MM-dd accounting date.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
