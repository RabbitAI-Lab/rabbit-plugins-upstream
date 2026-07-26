## Description: <br>
App Store Optimization data for AI agents via the Sonar API: keyword research with difficulty and popularity scores, app lookup and search, ASO audits, review mining, and revenue estimates for iOS and Android apps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[petersutarik](https://clawhub.ai/user/petersutarik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to research app-store keywords, inspect app listings, audit ASO quality, analyze reviews, compare competitors, and estimate app revenue through Sonar API calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ASO research terms, app IDs, country and store selections, and request metadata are sent to Sonar using the configured API key. <br>
Mitigation: Avoid submitting confidential unreleased app names or proprietary keyword lists unless organizational policy permits that vendor use. <br>
Risk: Sonar API calls may consume account credits, especially keyword discovery requests and repeated unbatched calls. <br>
Mitigation: Prefer lower-cost metrics endpoints when keywords are already known, batch supported requests, and monitor response credit headers. <br>


## Reference(s): <br>
- [Sonar homepage](https://trysonar.app) <br>
- [Sonar developers](https://trysonar.app/developers) <br>
- [Sonar MCP docs](https://trysonar.app/docs/mcp) <br>
- [Sonar API docs](https://trysonar.app/docs/api) <br>
- [ClawHub skill page](https://clawhub.ai/petersutarik/skills/sonar-aso) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON response descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SONAR_API_KEY for Sonar API requests; responses are JSON envelopes and may include credit cost headers.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
