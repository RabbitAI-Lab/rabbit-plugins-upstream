## Description: <br>
This skill helps agents search and discover GetYourGuide tours, activities, day trips, and attraction tickets through a read-only MCP integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent find GetYourGuide tours, attraction tickets, day trips, reviews, options, and location-based activities. It supports discovery and comparison; booking remains on getyourguide.com. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The GetYourGuide Partner API key could be exposed if stored in an untrusted MCP configuration. <br>
Mitigation: Store GYG_API_KEY only in trusted local or project MCP configuration and avoid committing secrets. <br>
Risk: Broad travel-activity prompts may route relevant query context to this integration. <br>
Mitigation: Invoke the skill only when GetYourGuide-backed tour, ticket, or activity search is intended. <br>


## Reference(s): <br>
- [ClawHub release page](https://clawhub.ai/chrischall/skills/getyourguide-mcp) <br>
- [getyourguide-mcp npm package](https://www.npmjs.com/package/getyourguide-mcp) <br>
- [GetYourGuide Partner API](https://partner.getyourguide.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown prose with JSON configuration examples and structured MCP tool results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only search and discovery; requires GYG_API_KEY, with optional GYG_CURRENCY and GYG_LANGUAGE settings.] <br>

## Skill Version(s): <br>
1.1.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
