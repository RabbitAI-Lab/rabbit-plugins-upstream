## Description: <br>
Searches and filters Amazon products using Sorftime data across 14 marketplaces, including competitor, category, brand, seller, price, sales, and historical snapshot queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External Amazon sellers, ecommerce analysts, and agent users use this skill to discover and compare products across marketplaces, brands, sellers, categories, price ranges, sales ranges, and historical snapshots. It supports product-search workflows and returns data-oriented results rather than business advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can call LinkFox/Sorftime APIs and consume credits, with broad searches potentially incurring higher cost. <br>
Mitigation: Verify the API gateway and request explicit user approval before paid queries, retries, broad searches, onboarding downloads, or additional pagination. <br>
Risk: Full product-search responses are persisted locally and may include commercially sensitive research data. <br>
Mitigation: Avoid sending confidential research unless needed, and review saved JSON files before sharing or committing workspace outputs. <br>
Risk: The skill may submit feedback text externally to LinkFox. <br>
Mitigation: Use feedback submission only when appropriate and avoid including confidential user content in feedback. <br>


## Reference(s): <br>
- [Sorftime API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-sorftime-amazon-product-query) <br>
- [LinkFox skill guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox account and credits](https://os.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell commands, saved JSON data files, and summarized product-search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved locally; small responses can be printed inline, while large responses are summarized with key fields and sample records.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
