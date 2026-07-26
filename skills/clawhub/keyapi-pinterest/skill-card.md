## Description: <br>
Keyapi Pinterest helps agents discover and analyze Pinterest users, pins, boards, followers, and following through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer Pinterest discovery, profile, content, and network questions by routing requests through KeyAPI, checking current docs, and returning concise reports or structured results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow can store a KeyAPI token in a local shell profile. <br>
Mitigation: Prefer a safer local environment or secret-store workflow when available, avoid passing the token with --token, and review or remove the managed KEYAPI_TOKEN block when the skill is no longer used. <br>
Risk: The skill performs live KeyAPI requests for Pinterest workflows. <br>
Mitigation: Install only when KeyAPI-backed Pinterest workflows are intended, confirm broad multi-endpoint reports before execution, and keep credentials local. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xyzzero/skills/keyapi-pinterest) <br>
- [KeyAPI Documentation Index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Pinterest Documentation](https://docs.keyapi.ai/en/pinterest/) <br>
- [KeyAPI Authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global Rules](references/global-rules.md) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Pinterest Rules](references/pinterest-rules.md) <br>
- [Pinterest Profile Module Rules](references/pinterest-profile-rules.md) <br>
- [Pinterest Content Module Rules](references/pinterest-content-rules.md) <br>
- [Pinterest Network Module Rules](references/pinterest-network-rules.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional tables, JSON excerpts, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save complete API responses to JSON files when the user requests export or full-result files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
