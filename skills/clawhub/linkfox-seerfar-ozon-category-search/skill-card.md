## Description: <br>
Seerfar Ozon Category Search retrieves product lists and category-level sales, revenue, price, rating, seasonality, brand, seller, and fulfillment metrics for a specified Ozon category ID. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External e-commerce operators, analysts, and developers use this skill to size an Ozon category, inspect best-selling or high-revenue products, compare price bands, and review fulfillment and seasonal signals. It is intended for category selection analysis when a category ID is already known or has been resolved by another Ozon source. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a LinkFox API key and consumes LinkFox credits for Ozon category queries. <br>
Mitigation: Confirm the user is comfortable with API-key use and credit cost before running repeated queries; rely on the documented cache and avoid automatic retry or pagination loops. <br>
Risk: The skill can automatically send feedback externally when it detects result quality or user sentiment signals. <br>
Mitigation: Review or disable feedback reporting before using sensitive task context. <br>
Risk: The script stores complete API results locally, including category and product result data. <br>
Mitigation: Treat saved output and cache directories as sensitive working data and clean the linkfox output/cache directories after use when retention is not needed. <br>


## Reference(s): <br>
- [Seerfar Ozon Category Search API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-seerfar-ozon-category-search) <br>
- [LinkFox skills site](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance, files] <br>
**Output Format:** [Markdown summaries, shell command examples, and JSON API responses saved to local files or printed to stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script writes complete API responses under a local linkfox session data directory, may print a compact summary for large responses, and uses a 24-hour cache for repeated parameter sets.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
