## Description: <br>
Helps agents manage Shopee Shop Category operations through LinkFox scripts for listing, creating, updating, and deleting shop categories and their item lists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and ecommerce agents use this skill to call Shopee Shop Category APIs for authorized stores, including category management and category item-list updates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and delete Shopee shop-category data. <br>
Mitigation: Review the intended store, category, and item-list changes before running mutating operations. <br>
Risk: API responses may contain sensitive store or business data and are saved locally. <br>
Mitigation: Run the skill in a private workspace, treat saved LinkFox response files as sensitive, and delete them when no longer needed. <br>
Risk: The skill depends on LinkFox/Shopee authorization and API-key access. <br>
Mitigation: Install and configure only the required authorization skill and keep LinkFox API keys out of shared shells, logs, and repositories. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-shop-category) <br>
- [Shopee Shop Category API reference](https://open.shopee.com/documents/v2/v2.shop_category.add_shop_category?module=101&type=1) <br>
- [Artifact API reference](artifact/references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, JSON] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are saved to a local LinkFox session directory; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
