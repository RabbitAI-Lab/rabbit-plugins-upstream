## Description: <br>
Search Walmart products and look up product details by product ID, with support for delivery speed, ZIP code, and in-store availability filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, shopping assistants, and developers use this skill to search Walmart listings, retrieve product details, and compare price, delivery, and in-store availability using Scavio's API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill sends Walmart search parameters to Scavio as a third-party API provider. <br>
Mitigation: Install and use it only when that provider relationship is acceptable; send only shopping parameters needed for the task. <br>
Risk: Localized availability checks may require a ZIP code or store ID, which can reveal location context. <br>
Mitigation: Avoid sensitive personal information and provide only the ZIP code or store ID needed for availability filtering. <br>
Risk: The skill relies on SCAVIO_API_KEY in the runtime environment. <br>
Mitigation: Store the API key in environment configuration and do not paste it into chat transcripts or committed files. <br>


## Reference(s): <br>
- [Scavio documentation](https://scavio.dev/docs) <br>
- [ClawHub skill page](https://clawhub.ai/scavio-ai/skills/scavio-walmart) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; responses may include prices, ratings, fulfillment details, availability, and product URLs.] <br>

## Skill Version(s): <br>
2.0.4 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
