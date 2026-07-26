## Description: <br>
Looks up Amazon SP-API Catalog Items through LinkFox for category, keyword, identifier, and ASIN catalog queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External ecommerce operators and developers use this skill to retrieve Amazon product catalog categories and item metadata through LinkFox-authenticated SP-API Catalog Items calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Full authenticated Amazon catalog API responses may include sensitive seller, SKU, query, or returned product metadata and are automatically stored locally. <br>
Mitigation: Run the skill only in workspaces where local LinkFox data files are acceptable, avoid sharing generated files, and periodically delete saved linkfox data files that are no longer needed. <br>
Risk: Using --inline can place complete API responses into the agent transcript or logs. <br>
Mitigation: Use the default summarized output for sensitive catalog lookups and inspect saved JSON selectively with tools such as jq when specific fields are needed. <br>
Risk: Catalog lookups depend on LinkFox gateway authentication and an installed Amazon store auth skill. <br>
Mitigation: Verify the LinkFox gateway, API key, and required auth skill before providing credentials or running catalog requests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-store-catalog) <br>
- [references/api.md](references/api.md) <br>
- [Amazon SP-API listCatalogCategories](https://developer-docs.amazon.com/sp-api/reference/listcatalogcategories) <br>
- [Amazon SP-API searchCatalogItems](https://developer-docs.amazon.com/sp-api/reference/searchcatalogitems) <br>
- [Amazon SP-API getCatalogItem](https://developer-docs.amazon.com/sp-api/reference/getcatalogitem) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON files, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; scripts emit JSON to stdout and save full JSON responses locally.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Large responses are summarized unless --inline is used; full responses are saved under a local linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
