## Description: <br>
Helps agents query and filter Shopify product opportunities by keyword or URL, price, weekly sales, listing date, Facebook ads, competition, supplier availability, and shipping country. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to research Shopify products and stores, compare sales and advertising signals, and narrow ecommerce product selections through LinkFox API queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may install a separate onboarding skill from an external ZIP while resolving authentication or credit issues. <br>
Mitigation: Require explicit user authorization and separate verification before downloading or installing external onboarding content. <br>
Risk: Full API responses may be saved in local linkfox directories, including workspace, home, or temporary fallback locations. <br>
Mitigation: Warn users before execution, avoid sensitive product-research queries when unnecessary, and remove saved response files when they are no longer needed. <br>
Risk: LinkFox credits are consumed dynamically based on returned product count, so broad queries or pagination can cost more than expected. <br>
Mitigation: Confirm credit consumption with the user before running and prefer narrow filters or smaller page sizes for exploratory searches. <br>


## Reference(s): <br>
- [Shopify Product Query API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopify-product-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Files] <br>
**Output Format:** [Markdown guidance with JSON request parameters, API response summaries, and optional saved JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Small responses may be printed inline; larger responses are summarized while full responses are saved in local linkfox session directories.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
