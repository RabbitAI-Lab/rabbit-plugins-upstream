## Description: <br>
Filters and analyzes Etsy stores by sales, favorites, reviews, opening date, country, category, and Raving or star status. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query Etsy store data, screen stores by performance and profile filters, and inspect returned store metrics through LinkFox's third-party data service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Etsy search parameters and an API key to a third-party LinkFox gateway. <br>
Mitigation: Use the skill only when the user trusts LinkFox with the query parameters and key, and confirm that any gateway override is expected before execution. <br>
Risk: Queries may consume paid LinkFox credits, with cost based on the number of returned stores. <br>
Mitigation: Confirm the expected page size and obtain user approval before running paid queries or additional pages. <br>
Risk: Full API responses may be saved locally and cached in linkfox-related directories. <br>
Mitigation: Treat saved files as potentially sensitive and delete cached or session outputs when the results or search terms should not persist. <br>


## Reference(s): <br>
- [API Reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-store-query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell commands, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The helper script may save full API responses under linkfox-related local directories and print either full JSON or a concise summary depending on response size.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
