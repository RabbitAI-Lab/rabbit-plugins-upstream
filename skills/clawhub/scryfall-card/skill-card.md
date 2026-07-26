## Description: <br>
Search and retrieve Magic: The Gathering card data using the Scryfall API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[santidev95](https://clawhub.ai/user/santidev95) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to search for Magic: The Gathering cards, retrieve named or random cards, and inspect card images, prices, rulings, legality, and other Scryfall card data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Card names and search queries may be sent to Scryfall. <br>
Mitigation: Avoid submitting private or sensitive text as card search input; use only queries intended for Scryfall lookup. <br>
Risk: Broad trigger wording may cause invocation for non-MTG uses of "magic" or "card". <br>
Mitigation: Invoke the skill only when the user intent is clearly about Magic: The Gathering or Scryfall card data. <br>
Risk: High request volume may hit Scryfall rate limits. <br>
Mitigation: Keep the documented 50-100 ms delay between requests and handle 429 responses with retry/backoff behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/santidev95/skills/scryfall-card) <br>
- [Publisher profile](https://clawhub.ai/user/santidev95) <br>
- [Scryfall API](https://api.scryfall.com) <br>
- [Scryfall Search Syntax Reference](references/search_syntax.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown and plain text with optional shell commands and formatted Scryfall results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the Scryfall API and return card names, rules text, image URLs, prices, legality, set details, autocomplete suggestions, and error messages.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
