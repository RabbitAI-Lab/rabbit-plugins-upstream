## Description: <br>
Batch-fetches full MPSTATS product-card data for up to 100 Ozon Russia SKUs, including pricing, ratings, reviews, inventory, sales, revenue, listing dates, images, and fulfillment details. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace operators and analysts use this skill to retrieve and compare detailed Ozon SKU metrics from MPSTATS for product checks, competitor audits, fulfillment comparisons, and period-over-period sales review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses LinkFox/MPSTATS API credentials and sends requests to LinkFox-controlled services. <br>
Mitigation: Use a scoped API key where possible, keep the key in environment variables only for the intended session, and confirm LINKFOX_TOOL_GATEWAY is unset or points to the expected LinkFox gateway before running. <br>
Risk: Full product-detail responses may be saved locally and cached, including business data from SKU lookups. <br>
Mitigation: Run the skill from an appropriate workspace, review the generated linkfox data directory, and remove cached or saved response files when they are no longer needed. <br>
Risk: The skill can consume paid LinkFox/MPSTATS credits and may produce additional cost for repeated or large-batch lookups. <br>
Mitigation: Confirm batch size and date windows before execution, rely on the built-in cache for repeated identical calls, and ask before splitting large SKU lists into multiple requests. <br>
Risk: The artifact describes automatic feedback reporting and onboarding-skill installation behavior. <br>
Mitigation: Approve feedback reporting and any onboarding-skill installation explicitly before allowing those behaviors in a sensitive environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-product-detail) <br>
- [MPSTATS Ozon API reference](references/api.md) <br>
- [LinkFox skills guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON parameters, shell commands, compact tables, summaries, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script writes full API responses to local JSON files, prints small responses inline, summarizes large responses, and supports a 24-hour local cache.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
