## Description: <br>
Google Analytics (GA4) for AI agents - traffic stats, sources, campaigns, referrals, landing pages, events, and conversion funnels across all your websites from one CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yoanndefay](https://clawhub.ai/user/yoanndefay) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, site owners, and analytics operators use this skill to query read-only GA4 website analytics, traffic sources, campaigns, referrals, landing pages, events, user breakdowns, and funnels from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill depends on the third-party fleets CLI, MCP package, and service for access to GA4 and related analytics data. <br>
Mitigation: Install it only from trusted package sources, review package updates, and use it only when the fleets service is acceptable for the site's analytics data. <br>
Risk: OAuth or token setup may grant access to website analytics data beyond the immediate query being run. <br>
Mitigation: Review requested permissions during setup, prefer scoped tokens where available, and periodically revoke credentials that are no longer needed. <br>


## Reference(s): <br>
- [fleets CLI](https://fleets.run) <br>
- [ClawHub skill page](https://clawhub.ai/yoanndefay/skills/website-analytics) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance centers on read-only analytics queries and optional JSON or CSV export through the fleets CLI or MCP server.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
