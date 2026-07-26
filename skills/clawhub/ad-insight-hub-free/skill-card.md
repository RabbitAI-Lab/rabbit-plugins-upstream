## Description: <br>
Ad Insight Hub Free helps agents translate advertising-intelligence search parameters and query AdMapix for basic creative search, creative counts, and app or developer profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growth, marketing, and app intelligence teams use this skill to convert natural-language ad research requests into AdMapix API queries for creative monitoring, creative counts, and app/developer lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advertising search terms, app identifiers, and related query parameters are sent to AdMapix. <br>
Mitigation: Use the skill only when AdMapix is an intended processor for the query data, and avoid sending sensitive competitive research unless approved. <br>
Risk: The required AdMapix API key could be exposed if pasted into chat or printed in logs. <br>
Mitigation: Store the key only in the ADMAPIX_API_KEY environment variable, never paste it into chat, and avoid commands that echo the key value. <br>
Risk: Generated curl commands perform remote HTTP requests from the user's environment. <br>
Mitigation: Review commands before execution and keep requests limited to the intended AdMapix API endpoints. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ad-insight-hub-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [AdMapix](https://www.admapix.com) <br>
- [AdMapix API base](https://api.admapix.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON] <br>
**Output Format:** [Markdown guidance with curl commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ADMAPIX_API_KEY; returns raw AdMapix JSON without caching.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
