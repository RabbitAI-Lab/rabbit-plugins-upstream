## Description: <br>
Discover and analyze Instagram users and content through the KeyAPI REST API using live official docs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[xyzzero](https://clawhub.ai/user/xyzzero) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and operators use this skill to turn Instagram research goals into KeyAPI REST workflows for profile, content, follower, hashtag, music, location, and search analysis. It helps resolve current endpoint documentation, configure authentication, execute live requests, and present results as observed API facts with clear interpretation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Instagram usernames, URLs, IDs, comments, likes, follower and following data, locations, and similar query targets may be sent to KeyAPI for live requests. <br>
Mitigation: Install and use the skill only when that data sharing is acceptable, and confirm broad report scope or pagination depth before collecting large result sets. <br>
Risk: The skill stores a KeyAPI bearer token in a local shell profile during setup. <br>
Mitigation: Run setup only in a private terminal, avoid passing tokens on the command line, and remove or rotate the managed KEYAPI_TOKEN block if uninstalling or rotating credentials. <br>
Risk: Endpoint assumptions can become stale if requests are made from remembered routes instead of current documentation. <br>
Mitigation: Resolve the official KeyAPI documentation page before live calls and extract the current method, path, parameters, pagination, and response shape. <br>
Risk: Repeated requests and broad fan-out workflows can consume credits, hit rate limits, or collect more data than intended. <br>
Mitigation: Use the documented stop conditions, ask before broad crawling or multi-endpoint reports, and save large responses only when needed for the user-requested output. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/xyzzero/skills/keyapi-instagram) <br>
- [KeyAPI Documentation Index](https://docs.keyapi.ai/llms.txt) <br>
- [KeyAPI Instagram Documentation](https://docs.keyapi.ai/en/instagram/) <br>
- [KeyAPI Authentication](https://docs.keyapi.ai/overview/authentication#bearer-authentication) <br>
- [Global Rules](references/global-rules.md) <br>
- [Scenario Cards](references/scenarios.md) <br>
- [Routing Policy](references/routing-policy.md) <br>
- [Instagram Rules](references/instagram-rules.md) <br>
- [Instagram User Module Rules](references/instagram-user-rules.md) <br>
- [Instagram Content Module Rules](references/instagram-content-rules.md) <br>
- [Instagram Discovery Module Rules](references/instagram-discovery-rules.md) <br>
- [Setup And Auth](references/setup-and-auth.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown responses with inline shell commands and optional JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute live KeyAPI requests and optionally write full JSON responses when the user asks for exports.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
