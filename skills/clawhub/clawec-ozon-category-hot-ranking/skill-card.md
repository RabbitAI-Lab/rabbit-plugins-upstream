## Description: <br>
Queries Ozon category hot-ranking data through the ClawEC API, including GMV, sales, price sorting, sell-through rate, commissions, and cross-border product share. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anyunzhong](https://clawhub.ai/user/anyunzhong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, agents, and cross-border ecommerce operators use this skill to query Ozon top-category ranking data and produce Chinese market-research summaries for category selection and opportunity comparison. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the ClawEC API key and query parameters to clawec.com. <br>
Mitigation: Read the key from CLAWEC_API_KEY, avoid hardcoding secrets, and revoke or rotate the key if it is exposed. <br>
Risk: API failures or parameter mistakes can produce missing or misleading category-ranking data. <br>
Mitigation: Check the top-level status, data.success, errorCode, and errorMessage before using the result for ecommerce decisions. <br>


## Reference(s): <br>
- [Response schema](references/response-schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Markdown, Guidance] <br>
**Output Format:** [Markdown report with optional shell commands and JSON API response summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires CLAWEC_API_KEY and sends category query parameters to clawec.com; pageSize is capped at 15.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
