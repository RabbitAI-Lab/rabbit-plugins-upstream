## Description: <br>
Query the free countries.dev REST API for country, city, postal-code, IP-geolocation, and distance data without an API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to answer geography, country-code, currency, city-coordinate, postal-code, IP-geolocation, and distance questions through countries.dev lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries may send IP addresses, precise coordinates, or postal codes to the third-party countries.dev service. <br>
Mitigation: Avoid submitting private or third-party location data unless the user intends to disclose it to countries.dev. <br>


## Reference(s): <br>
- [Countries API on ClawHub](https://clawhub.ai/nanookai/skills/countries-api) <br>
- [countries.dev endpoint reference](references/endpoints.md) <br>
- [countries.dev API](https://countries.dev) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with endpoint guidance, curl examples, and JSON response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May recommend countries.dev requests and field filters; does not require API keys.] <br>

## Skill Version(s): <br>
1.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
