## Description:

This skill helps an agent find GetYourGuide tours, activities, day trips, attraction tickets, tour details, options, reviews, categories, and locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent search and inspect GetYourGuide tours, activities, attraction tickets, availability options, reviews, categories, and locations before booking on GetYourGuide.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generic travel-planning prompts may route to GetYourGuide when the user did not specifically ask for GetYourGuide results.

Mitigation: Confirm whether GetYourGuide-specific results are desired before using the skill for broad travel-planning requests.

Risk: Runtime behavior may change if the npm package is resolved without a fixed version.

Mitigation: Pin the npm package version when predictable runtime code is required.

Risk: The integration requires a GetYourGuide Partner API key.

Mitigation: Provide the API key only in the MCP server environment and verify partner-tier access when 401 or 403 errors occur.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/getyourguide-mcp)
- [npm package](https://www.npmjs.com/package/getyourguide-mcp)
- [GetYourGuide Partner Program](https://partner.getyourguide.com)

## Skill Output:

**Output Type(s):** [guidance, configuration, shell commands, text]

**Output Format:** [Markdown with JSON configuration examples and tool-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only tour and activity discovery; requires a GetYourGuide Partner API key.]

## Skill Version(s):

1.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
