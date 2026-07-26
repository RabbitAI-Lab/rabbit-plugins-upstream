## Description: <br>
Helps agents search and filter Amazon products with Keepa data across category, price, monthly sales, keywords, BSR, reviews, ratings, package dimensions, weight, and fulfillment criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, product researchers, and e-commerce operators use this skill to turn multi-criteria Amazon product research requests into Keepa product-search parameters, run the LinkFox-backed search, and present structured product results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and calls LinkFox services. <br>
Mitigation: Install and run it only when sharing the API key and product-search queries with LinkFox services is acceptable. <br>
Risk: Full product-search responses are saved locally and may contain sensitive sourcing research. <br>
Mitigation: Review the configured output location before use, avoid sensitive searches when local retention is not acceptable, and clean saved response files according to workspace policy. <br>
Risk: Feedback reporting can send observations about skill behavior or user reactions to a separate LinkFox feedback API. <br>
Mitigation: Review or disable feedback behavior before using the skill in workflows where user comments, business context, or query details should not be reported. <br>
Risk: The onboarding flow can direct installation of a remote LinkFox onboarding ZIP. <br>
Mitigation: Install the onboarding package only after confirming the source is trusted and the user has approved the download and installation. <br>


## Reference(s): <br>
- [Keepa Product Search API Reference](artifact/references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-keepa-product-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, files, guidance] <br>
**Output Format:** [Markdown guidance with JSON request parameters, shell-command examples, stdout summaries, and saved JSON response files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script saves full product-search responses locally; responses up to 8 KB are printed in full, larger responses print a summary unless --inline is used.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
