## Description: <br>
Queries and analyzes Amazon Brand Analytics search-term data across 15 marketplaces with nearly three years of weekly history. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and ecommerce analysts use this skill to query ABA search-term rankings, click share, conversion share, marketplace trends, seasonal terms, and competitor keyword traffic. It helps translate a user's search-term analysis request into a precise LinkFox ABA query and present the returned data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ABA query descriptions and the LinkFox API key are sent to LinkFox services. <br>
Mitigation: Confirm the marketplace and query before use, and avoid including secrets or sensitive business context in query text or feedback. <br>
Risk: Queries can spend LinkFox credits and may consume significant credits for broad requests. <br>
Mitigation: Explain the expected paid-query behavior before continuing and keep filters precise to avoid unnecessary calls. <br>
Risk: Full paid-query responses and cache files are saved locally under linkfox session folders. <br>
Mitigation: Review or clean the generated linkfox folders after use, especially on shared workstations or sensitive projects. <br>
Risk: The feedback flow can send user comments or context to an external LinkFox feedback endpoint. <br>
Mitigation: Do not include credentials, private business details, or unnecessary user context when reporting feedback. <br>


## Reference(s): <br>
- [ABA API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-aba-intelligent-query) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell command examples, tabular result summaries, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script caches identical queries for 24 hours and saves full API responses under a local linkfox session directory before printing either full JSON or a compact summary.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
