## Description: <br>
Filters Temu products by keyword, product or store ID, category, price, rating, reviews, sales, listing date, fulfillment model, region, and tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query and compare Temu products for product research, using marketplace attributes, sales signals, and fulfillment details to narrow results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API credentials, Temu query content, and session metadata can be sent to a configurable LinkFox gateway. <br>
Mitigation: Install only if LinkFox is trusted for this data, and keep LINKFOX_TOOL_GATEWAY unset unless the destination is intentionally controlled. <br>
Risk: Credential or billing failures can lead the workflow to request installation of a separate onboarding skill. <br>
Mitigation: Review the onboarding skill package before approving installation or use the documented LinkFox account and credit guidance instead. <br>
Risk: Full query results may be saved locally and can fall back outside the current project directory. <br>
Mitigation: Run the helper from an appropriate workspace and review generated linkfox data files before sharing logs or archives. <br>
Risk: Broad or repeated paginated queries can consume LinkFox credits based on returned product count. <br>
Mitigation: Confirm scope, page size, and pagination with the user before running high-volume queries. <br>


## Reference(s): <br>
- [Temu product query API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-product-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters and optional shell command output; helper script writes JSON result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key; paginated product queries may consume credits based on returned product count.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
