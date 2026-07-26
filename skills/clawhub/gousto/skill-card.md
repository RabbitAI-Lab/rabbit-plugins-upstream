## Description: <br>
Search and browse 9,000+ Gousto recipes. Get full ingredients and step-by-step cooking instructions via official API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dhruvkelawala](https://clawhub.ai/user/dhruvkelawala) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agent developers use this skill to search Gousto recipes and retrieve structured ingredients, preparation details, and cooking instructions for recipe-planning workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Gousto's public API and stores a local recipe cache. <br>
Mitigation: Install only in environments where outbound access to Gousto and local caching of public recipe metadata are acceptable. <br>
Risk: The documentation contains a mismatch about the network path for recipe fetches. <br>
Mitigation: Review the scripts as the authoritative behavior and correct the note before relying on the documentation for network review. <br>


## Reference(s): <br>
- [Gousto Recipes Skill on ClawHub](https://clawhub.ai/dhruvkelawala/skills/gousto) <br>
- [Gousto recipe listing API](https://production-api.gousto.co.uk/cmsreadbroker/v1/recipes?limit=50&offset=0) <br>
- [Gousto single recipe API](https://production-api.gousto.co.uk/cmsreadbroker/v1/recipe/{slug}) <br>
- [OpenClaw](https://github.com/openclaw/openclaw) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text and JSON emitted by shell scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results are read from a local recipe cache; full recipe details are fetched from Gousto's public API.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
