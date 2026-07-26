## Description: <br>
Queries the Jungle Scout Product Database through LinkFox to filter Amazon products across 10 marketplaces by category, price, sales, revenue, reviews, rating, BSR, LQS, seller type, and related criteria. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers and e-commerce researchers use this skill to build filtered Amazon product research queries and review Jungle Scout Product Database results for Amazon product discovery and competitive screening. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: LinkFox receives product queries, API-key-authenticated requests, session/app metadata, and possible automatic feedback content. <br>
Mitigation: Use the skill only when that external sharing is acceptable, keep sensitive business details out of queries and feedback, and review any feedback content before it is sent. <br>
Risk: Queries can consume LinkFox credits, and the skill states that dynamic pricing may make a single request costly. <br>
Mitigation: Confirm marketplace, filters, and expected credit cost with the user before running paid searches; avoid repeated exploratory calls after failures or empty results. <br>
Risk: Full API responses and cached results may be written to local linkfox data directories. <br>
Mitigation: Run the skill only in an appropriate workspace, treat saved result files as potentially sensitive commercial research, and remove cached or session files when they are no longer needed. <br>
Risk: The tool gateway can be changed through environment configuration. <br>
Mitigation: Use the default or another trusted gateway only, and inspect gateway-related environment variables before use in sensitive environments. <br>


## Reference(s): <br>
- [Jungle Scout Product Database API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-junglescout-product-database) <br>
- [LinkFox Skills](https://skill.linkfox.com/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Files, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands; API responses are JSON and may be printed or saved to local result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses LinkFox API-key authentication, may consume LinkFox credits, caches repeated requests for 24 hours, and writes full responses under a local linkfox session data directory.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
