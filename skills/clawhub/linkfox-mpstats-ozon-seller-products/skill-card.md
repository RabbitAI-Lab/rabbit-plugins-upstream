## Description: <br>
Retrieves seller-scoped Ozon Russia product metrics from MPSTATS, including per-SKU sales, revenue, price, ratings, stock, turnover, lost-profit, filtering, sorting, and currency conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace analysts, sellers, and agents use this skill to audit a numeric Ozon seller ID, inspect the seller's SKU mix, identify bestsellers and stockout losses, and compare seller-level product performance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ozon seller-analysis requests and the LinkFox API key are sent to the configured LinkFox gateway. <br>
Mitigation: Use only in environments where sending those requests to LinkFox is acceptable, and verify the configured gateway before use. <br>
Risk: Full API responses may be saved locally, including cached responses and session data files. <br>
Mitigation: Run the skill in an appropriate workspace, review generated linkfox data and cache files, and avoid sensitive workspaces unless local storage is acceptable. <br>
Risk: The feedback workflow can report broad user feedback or observed behavior to the LinkFox feedback API. <br>
Mitigation: Review or disable feedback reporting in sensitive workflows before deploying the skill. <br>
Risk: Queries consume LinkFox credits and repeated exploratory calls can increase cost. <br>
Mitigation: Inform users before extra calls, rely on the built-in cache for identical parameters, and prefer tighter filters before deep pagination. <br>


## Reference(s): <br>
- [MPSTATS Ozon Seller Products API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-seller-products) <br>
- [LinkFox Publisher Profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell command examples, compact tables, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full API responses to local JSON files, prints small responses inline, summarizes large responses, and uses a 24-hour local cache for repeated parameter sets.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
