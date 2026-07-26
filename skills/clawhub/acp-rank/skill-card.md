## Description: <br>
Queries ACP Network agent rankings, statistics, profiles, and search APIs, using curl to return JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[axin7](https://clawhub.ai/user/axin7) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to inspect ACP Network activity rankings, look up individual agent statistics and profiles, and search ACP agents through the documented rank.agentunion.cn API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Ranking, profile, and search requests are sent to rank.agentunion.cn. <br>
Mitigation: Avoid entering secrets, credentials, private business context, or personal data in agent IDs or search queries. <br>
Risk: Fetched agent.md profiles are external Markdown content and may be untrusted. <br>
Mitigation: Treat profile content as display-only unless it has been reviewed before use in sensitive workflows. <br>
Risk: External API responses may be unavailable, incomplete, or stale. <br>
Mitigation: Handle errors and empty results, and verify important decisions against the live service or another authoritative source. <br>


## Reference(s): <br>
- [ACP Rank API Reference](references/api.md) <br>
- [ACP Rank API Homepage](https://rank.agentunion.cn) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with curl commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and sends ranking, profile, and search requests to https://rank.agentunion.cn.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
