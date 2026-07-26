## Description: <br>
This skill queries LinkFox MPSTATS for Ozon Russia products under a full Russian category path and returns SKU-level sales, revenue, pricing, rating, inventory, turnover, and lost-sales metrics for category analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketplace analysts and ecommerce operators use this skill to inspect Ozon category product performance, identify category bestsellers, scan blue-ocean niches, and compare brand or seller presence within a specific Russian category path. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and sends category-query parameters to the LinkFox gateway. <br>
Mitigation: Use an appropriately scoped API key, avoid submitting sensitive category research when that is not acceptable, and review the configured LinkFox gateway before running the script. <br>
Risk: Full Ozon analytics responses are stored locally and cached by default, which may retain commercially sensitive query results. <br>
Mitigation: Run the skill from an approved writable workspace, clear saved LinkFox output when no longer needed, and use --no-cache for sensitive queries. <br>
Risk: The artifact includes automatic feedback behavior that can submit observations about skill behavior to LinkFox. <br>
Mitigation: Review or disable feedback submission behavior before installation if automatic external feedback is not acceptable for the deployment environment. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-mpstats-ozon-category-products) <br>
- [MPSTATS Ozon Category Products API Reference](references/api.md) <br>
- [LinkFox Skill Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox Skill Catalog](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON response files with stdout summaries or full inline JSON for small responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a full Russian Ozon category path and LinkFox API credentials; page size is capped at 100 and default local cache TTL is 24 hours.] <br>

## Skill Version(s): <br>
1.0.4 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
