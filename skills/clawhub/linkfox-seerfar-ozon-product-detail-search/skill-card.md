## Description: <br>
Retrieves detailed Seerfar analytics for a single Ozon product SKU, including product identity, price, ratings, sales, revenue, inventory, category rank, seller, brand, fulfillment, listing age, and sales trend data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and ecommerce analysts use this skill to inspect one Ozon SKU at a time for product research, competitor teardown, listing diagnostics, sales-trend review, inventory checks, and category-rank tracking. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses LinkFox API credentials and can make paid Seerfar/Ozon lookup calls. <br>
Mitigation: Install only when the LinkFox API key and tool gateway are trusted, and confirm with the user before repeated or high-frequency calls that consume credits. <br>
Risk: Full product-response data is persisted locally and may include detailed market-analysis data from the lookup. <br>
Mitigation: Run the skill in an appropriate workspace and review saved response files before sharing or retaining them. <br>
Risk: The security scan notes external onboarding installation and automatic feedback telemetry as behavior users should review. <br>
Mitigation: Decline or review separate onboarding installation prompts unless that capability is intended, and account for feedback telemetry in the user workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-product-detail-search) <br>
- [Seerfar Ozon API reference](references/api.md) <br>
- [LinkFox tool gateway](https://tool-gateway.linkfox.com) <br>
- [LinkFox skill guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox account and credits portal](https://os.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved JSON data files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an Ozon SKU; dateRange is optional. Full responses are saved locally, and large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
