## Description: <br>
Provides agent workflows and Python scripts for Shopee FirstMile store logistics, including unbound-order lookup, tracking-number generation, binding and unbinding, waybills, channels, transit warehouses, and courier-delivery first-mile endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Shopee sellers, commerce operators, and developers use this skill to manage cross-border FirstMile logistics for authorized stores, including finding unbound orders, generating or binding first-mile tracking numbers, retrieving waybills, and checking channel or warehouse information. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Shopee first-mile logistics state by generating, binding, or unbinding tracking numbers. <br>
Mitigation: Require explicit user approval before any generate, bind, or unbind operation, especially when working with real stores. <br>
Risk: Full API responses are always saved locally and may include store, order, tracking, or waybill details. <br>
Mitigation: Use the skill only in workspaces where local response storage is acceptable, avoid --inline unless necessary, and delete the linkfox output tree after sensitive work. <br>
Risk: The local storage location can be broader than the documentation suggests. <br>
Mitigation: Check the configured workspace and linkfox data directory before use, and review saved output paths after each run. <br>
Risk: The skill depends on LinkFox authentication and a companion Shopee store auth skill. <br>
Mitigation: Run dependency checks first, use only the needed LinkFox API key, and avoid exposing unrelated credentials in the execution environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopee-store-first-mile) <br>
- [FirstMile API reference](artifact/references/api.md) <br>
- [Shopee FirstMile API documentation](https://open.shopee.com/documents/v2/v2.first_mile.get_unbind_order_list?module=96&type=1) <br>
- [LinkFox API key and credit guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python command examples and JSON request parameters; runtime output is saved JSON plus either full JSON or a concise text summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox authentication and the companion Shopee store auth skill. Full API responses are saved under a linkfox data directory, small responses are printed inline, and large responses are summarized unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
