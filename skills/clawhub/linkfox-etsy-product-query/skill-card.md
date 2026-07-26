## Description: <br>
Helps agents search and filter Etsy products by keyword or listing URL, price, sales, favorites, reviews, listing date, category, product type, and product tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, product researchers, and e-commerce operators use this skill to turn multi-criteria Etsy product research requests into LinkFox-backed product-query parameters, run the search, and review structured product results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and sends Etsy research queries through a credentialed LinkFox remote gateway. <br>
Mitigation: Use it only when sharing the API key, query terms, filters, and session metadata with LinkFox services is acceptable. <br>
Risk: The gateway host can be changed through environment configuration. <br>
Mitigation: Before running the skill, confirm LINKFOX_TOOL_GATEWAY is unset or points only to the official LinkFox gateway. <br>
Risk: Full product-query responses may be saved or cached locally and can contain sensitive sourcing research. <br>
Mitigation: Review the local linkfox output and cache directories after sensitive searches, and delete saved JSON files when retention is not needed. <br>
Risk: Large result pages can consume many LinkFox credits because costs scale with returned product count. <br>
Mitigation: Warn the user about per-result credit consumption and confirm before broad searches, large page sizes, or repeated pagination. <br>
Risk: Authentication or credit troubleshooting can direct installation of a remote LinkFox onboarding package. <br>
Mitigation: Download or install onboarding material only after confirming the source and obtaining explicit user approval. <br>


## Reference(s): <br>
- [Etsy Product Query API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-product-query) <br>
- [LinkFox API Key and Credit Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox Tool Gateway](https://tool-gateway.linkfox.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON request parameters, shell-command examples, stdout summaries, and optional saved JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts Etsy keywords or listing URLs plus filters for price, sales, favorites, reviews, listing date, category, status, product type, and tags; requires a LinkFox API key and can save or cache full response JSON under a linkfox directory.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
