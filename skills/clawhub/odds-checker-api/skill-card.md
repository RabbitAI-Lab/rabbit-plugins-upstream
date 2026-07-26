## Description: <br>
Query Odds-API.io for sports events, bookmakers, and betting odds through the Odds-API.io v3 API using a user-provided API key. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[diegopetrucci](https://clawhub.ai/user/diegopetrucci) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to look up sports, bookmakers, events, and betting odds through the Odds-API.io v3 API. It supports event search, event ID lookup, odds retrieval, and compact command-line summaries when a user provides an API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Authenticated requests and dry-run output may expose the user's Odds-API.io API key in printed request URLs or logs. <br>
Mitigation: Avoid dry-run or debug output until apiKey values are redacted, pass keys only at runtime, and prefer a restricted or easily rotated API key. <br>
Risk: The helper contacts Odds-API.io and sends a user-provided API key to that external service for authenticated endpoints. <br>
Mitigation: Install and run the skill only in environments where outbound calls to Odds-API.io are approved, and never store the API key in the skill files or repository. <br>


## Reference(s): <br>
- [Odds-API.io quick reference](references/odds-api-reference.md) <br>
- [Odds-API.io API base URL](https://api.odds-api.io/v3) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API calls, Text, JSON] <br>
**Output Format:** [Markdown guidance with shell commands; CLI responses are plain text summaries or JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided Odds-API.io API key for authenticated endpoints.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
