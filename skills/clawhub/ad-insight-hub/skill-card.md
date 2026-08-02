## Description: <br>
Ad Insight Hub helps agents query AdMapix advertising intelligence by translating natural-language parameters, orchestrating endpoint calls, caching reusable results, and labeling estimate confidence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External marketing, user acquisition, and market analysis teams use this skill to search ad creatives, inspect app and developer profiles, compare store rankings, and retrieve download or revenue estimates with confidence labels. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: AdMapix query results, business intelligence, and bulk exports may remain on the local machine. <br>
Mitigation: Use non-shared local storage for sensitive exports and delete ~/.admapix-cache when cached data should no longer remain on the machine. <br>
Risk: The AdMapix API key could be exposed if handled directly in chat, logs, files, or URL parameters. <br>
Mitigation: Configure ADMAPIX_API_KEY as an environment variable, send it only as the X-API-Key request header, and do not print, store, or accept the key in chat. <br>
Risk: Download and revenue values are third-party estimates and may be unsuitable for precise financial decisions. <br>
Mitigation: Preserve the skill's A/B/C confidence labels and use lower-confidence long-tail estimates only for directional analysis. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/thcjp/skills/ad-insight-hub) <br>
- [AdMapix](https://www.admapix.com) <br>
- [AdMapix API base](https://api.admapix.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and structured JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confidence labels for third-party estimates and references to local AdMapix cache behavior.] <br>

## Skill Version(s): <br>
1.0.5 (source: server evidence release.version and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
