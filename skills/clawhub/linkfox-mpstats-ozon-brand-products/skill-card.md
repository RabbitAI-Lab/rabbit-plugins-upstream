## Description: <br>
This skill queries LinkFox MPSTATS data for Ozon Russia products under an exact brand display name, returning per-SKU sales, revenue, price, rating, inventory, turnover, and lost-profit metrics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace operators, analysts, and agents use this skill to inspect the SKU-level product structure of a single Ozon brand and compare sales, revenue, pricing, ratings, stock, and lost-profit signals. It is suited to brand competitor audits, bestseller review, and currency-normalized marketplace analysis when the exact brand display name is known. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and can make paid LinkFox API calls. <br>
Mitigation: Install and run it only when the user accepts LinkFox credential use and possible credit consumption; confirm additional paid lookups before retrying or broadening a query. <br>
Risk: The skill stores full marketplace-analysis API responses on disk. <br>
Mitigation: Review saved JSON files before sharing a workspace or committing generated outputs, and remove cached or session data when it is no longer needed. <br>
Risk: The security summary notes automatic feedback reporting and onboarding-install behavior that may be broader than expected. <br>
Mitigation: Review or disable feedback reporting and onboarding installation behavior before deployment in environments with strict data-sharing or software-installation controls. <br>


## Reference(s): <br>
- [MPSTATS Ozon Brand Products API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-brand-products) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API results or summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are persisted as JSON files; large responses are summarized in stdout unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
