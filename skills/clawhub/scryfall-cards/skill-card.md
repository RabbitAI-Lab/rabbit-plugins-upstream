## Description: <br>
Searches and retrieves Magic: The Gathering card data using the Scryfall API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[santidev95](https://clawhub.ai/user/santidev95) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external agents use this skill to answer Magic: The Gathering card questions, search cards by attributes, retrieve rulings and legalities, inspect card prices and images, and get random or named cards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Magic: The Gathering card names and search queries are sent to Scryfall. <br>
Mitigation: Use the skill only when Scryfall lookups are intended, and avoid including private or sensitive information in search queries. <br>
Risk: Excessive requests may trigger Scryfall rate limiting. <br>
Mitigation: Honor the artifact guidance to pause 50-100 ms between requests and stay within the documented maximum of 10 requests per second. <br>


## Reference(s): <br>
- [Scryfall API](https://api.scryfall.com) <br>
- [Scryfall Search Syntax Reference](artifact/references/search_syntax.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/santidev95/skills/scryfall-cards) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, text] <br>
**Output Format:** [Plain text and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Scryfall API responses and formatted card summaries; no credentials are indicated.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
