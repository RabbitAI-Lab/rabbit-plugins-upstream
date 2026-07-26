## Description: <br>
Enables agents to read Adobe Commerce product and category data through the OOMOL Adobe Commerce connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Adobe Commerce categories and products from an OOMOL-connected Adobe Commerce account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connected OOMOL account can expose Adobe Commerce product and category data to the agent. <br>
Mitigation: Install only when that read access is acceptable, and use the listed read-only actions: get_category, get_product, list_categories, and list_products. <br>
Risk: Connector action inputs can fail or produce unexpected results if payloads are built from stale assumptions. <br>
Mitigation: Inspect the live action schema with oo connector schema before constructing each payload. <br>


## Reference(s): <br>
- [ClawHub Adobe Commerce skill](https://clawhub.ai/oomol/skills/oo-adobe-commerce) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Adobe Commerce homepage](https://business.adobe.com/products/magento/magento-commerce.html) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands use oo connector schema and oo connector run, which may return JSON data from Adobe Commerce.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
