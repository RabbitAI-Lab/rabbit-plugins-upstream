## Description: <br>
This skill helps agents manage Shopee Add-On Deal promotions through LinkFox by calling the Shopee Open API add-on deal endpoints for listing, creating, updating, ending, and deleting promotions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and e-commerce operators use this skill to inspect and manage Add-On Deal promotions for authorized Shopee shops. It is useful when an agent needs to call Shopee add-on deal APIs through LinkFox scripts and review the resulting JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Mutating scripts can change, delete, or end live Shopee Add-On Deal promotions. <br>
Mitigation: Before running mutating scripts, confirm the shopId, promotion ID, affected items, and intended action with the user. <br>
Risk: Saved API responses can contain sensitive business data. <br>
Mitigation: Protect or delete saved LinkFox JSON files after use, and avoid inline full-output mode unless full response details are necessary. <br>


## Reference(s): <br>
- [Skill API Reference](references/api.md) <br>
- [Shopee Add-On Deal API Index](https://open.shopee.com/documents/v2/v2.add_on_deal.add_add_on_deal?module=111&type=1) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-add-on-deal) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON responses saved to local files, with stdout JSON or summaries and shell command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API results are saved under LinkFox session directories; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
