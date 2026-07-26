## Description: <br>
Search and retrieve Magic: The Gathering card data using the Scryfall API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[santidev95](https://clawhub.ai/user/santidev95) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to search Magic: The Gathering card data, retrieve card details, check rulings, prices, images, and legality information, and run Scryfall query workflows from an agent. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Card names and search terms may be sent to Scryfall when the skill performs lookups. <br>
Mitigation: Avoid sending confidential or unrelated user text as a query, and disclose that searches use the Scryfall API when relevant. <br>
Risk: Ambiguous prompts mentioning magic or cards could trigger the skill in the wrong context. <br>
Mitigation: Ask a clarifying question when the user has not clearly requested Magic: The Gathering card information. <br>
Risk: Scryfall API errors or rate limits can affect lookup results. <br>
Mitigation: Respect the documented request delay and handle 404, 422, and 429 responses before presenting results. <br>


## Reference(s): <br>
- [Scryfall API](https://api.scryfall.com) <br>
- [Scryfall Search Syntax Reference](references/search_syntax.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, code, API calls, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell command examples; script output is plain text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Scryfall API responses and should respect the documented request delay and API error handling.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
