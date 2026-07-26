## Description: <br>
Helps agents query and filter Shopify independent store records through LinkFox by keyword or domain, country, store age, product count, ad count, traffic, orders, and social followers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to discover Shopify sellers, competitor stores, and store performance signals for market research or ecommerce analysis. It is useful when an agent needs structured Shopify store results and documented filter, sort, and pagination parameters. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can consume paid LinkFox credits because billing is based on returned Shopify store count and each page is a new request. <br>
Mitigation: Confirm the intended query scope, page size, and pagination plan with the user before running searches that may return many stores. <br>
Risk: The skill sends Shopify query parameters and the LinkFox API key to the LinkFox gateway. <br>
Mitigation: Use only approved LinkFox credentials and avoid sending sensitive or unnecessary query terms. <br>
Risk: The script saves full API responses locally, which may include store contact details or other business data. <br>
Mitigation: Store results only in an appropriate workspace and remove local response files when they are no longer needed. <br>
Risk: The skill directs agents to fetch and install a secondary onboarding skill from an external URL during some authentication or credit failures. <br>
Mitigation: Install the secondary skill only after verifying the source and obtaining user approval for the download. <br>


## Reference(s): <br>
- [Shopify Store Query API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-shopify-store-query) <br>
- [LinkFox API Key Guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>
- [LinkFox Account and Credits Portal](https://os.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples, JSON API responses, and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a LinkFox API key; paginated results may consume paid credits; full responses are saved locally and large responses may be summarized in stdout.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
