## Description: <br>
Manages Shopee Top Picks collections for authorized stores by calling LinkFox scripts for the Shopee Open API list, create, update, and delete endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and ecommerce operators use this skill to list, create, update, and delete Shopee Top Picks collections for authorized stores through LinkFox scripts and API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, or delete live Shopee Top Picks for a store. <br>
Mitigation: Install it only when LinkFox and Shopee store authority is appropriate, and verify the shop and top_picks_id before mutating actions. <br>
Risk: Full API responses may be saved locally under LinkFox session data. <br>
Mitigation: Review stored JSON files for sensitive store data and handle them according to local data-retention policy. <br>
Risk: The security guidance notes conflicting credit-consumption documentation. <br>
Mitigation: Clarify credit consumption with the publisher before repeated or exploratory calls. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-top-picks) <br>
- [API parameter and field reference](references/api.md) <br>
- [Shopee get_top_picks_list documentation](https://open.shopee.com/documents/v2/v2.top_picks.get_top_picks_list?module=100&type=1) <br>
- [Shopee add_top_picks documentation](https://open.shopee.com/documents/v2/v2.top_picks.add_top_picks?module=100&type=1) <br>
- [Shopee update_top_picks documentation](https://open.shopee.com/documents/v2/v2.top_picks.update_top_picks?module=100&type=1) <br>
- [Shopee delete_top_picks documentation](https://open.shopee.com/documents/v2/v2.top_picks.delete_top_picks?module=100&type=1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, json] <br>
**Output Format:** [Markdown guidance, shell command examples, and JSON API responses saved as local files or printed to stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials and authorized Shopee store tokens; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
