## Description: <br>
Crypto market intelligence powered by Messari's REST API for real-time asset metrics, sentiment, news, research, protocol data, token unlocks, fundraising, governance events, and AI-assisted crypto analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jds950](https://clawhub.ai/user/jds950) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, analysts, and developers use this skill to route crypto-market questions to Messari services for market data, sentiment, research, news, protocol metrics, stablecoin data, token unlocks, and event intelligence. Outputs should be treated as informational market research rather than trading advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends crypto research queries to Messari using the user's API key. <br>
Mitigation: Install only when third-party Messari API use is intended, configure the API key through MESSARI_API_KEY, and avoid including secrets or sensitive trading details in prompts. <br>
Risk: Messari API and AI endpoints can consume API quota or AI credits. <br>
Mitigation: Monitor API and AI credit usage before and after deployment. <br>
Risk: Market analysis may be incomplete, stale, or unsuitable for a specific trading decision. <br>
Mitigation: Treat outputs as informational research and validate important financial decisions against independent sources and applicable policies. <br>


## Reference(s): <br>
- [Messari REST API Services Reference](references/api_services.md) <br>
- [Messari API](https://messari.io/api) <br>
- [Messari REST API Base URL](https://api.messari.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API examples and curl command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a user-provided MESSARI_API_KEY; Messari AI endpoints also require Messari AI credits.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
