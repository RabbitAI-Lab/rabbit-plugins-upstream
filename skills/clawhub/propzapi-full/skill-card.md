## Description: <br>
Live sports odds and player props via propzapi.com, with tools for moneyline, spreads, totals, upcoming player props, fixtures, live scores, and covered sportsbooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paperandbeyond23-gif](https://clawhub.ai/user/paperandbeyond23-gif) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when they need an agent to fetch current sportsbook odds, player props, fixtures, live scores, or covered sportsbook lists from PropzAPI. It is for returning sourced sports-odds data, not betting advice or picks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a PropzAPI API key and sends sports-odds queries to PropzAPI. <br>
Mitigation: Use a scoped PropzAPI key where possible, store it in PROPZAPI_KEY, and avoid sending sensitive user information in league, sport, market, or status queries. <br>
Risk: Tool calls may spend metered PropzAPI credits. <br>
Mitigation: Call the tools only for explicit live odds, props, fixtures, scores, or sportsbook coverage requests, and confirm ambiguous league or market requests before use. <br>
Risk: Sports odds are informational and may be delayed or unsuitable for wagering decisions. <br>
Mitigation: Return the sourced numbers without presenting betting advice, picks, or guarantees, and remind users to comply with applicable laws and sportsbook terms when relevant. <br>


## Reference(s): <br>
- [PropzAPI homepage](https://propzapi.com) <br>
- [PropzAPI documentation](https://propzapi.com/docs) <br>
- [PropzAPI OpenAPI specification](https://api.propzapi.com/openapi.json) <br>
- [PropzAPI pricing](https://propzapi.com/pricing) <br>
- [ClawHub skill page](https://clawhub.ai/paperandbeyond23-gif/skills/propzapi-full) <br>
- [Publisher profile](https://clawhub.ai/user/paperandbeyond23-gif) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Guidance] <br>
**Output Format:** [JSON objects returned to the agent, with structured error objects on failure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PROPZAPI_KEY and may spend metered PropzAPI credits when tools are called.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
