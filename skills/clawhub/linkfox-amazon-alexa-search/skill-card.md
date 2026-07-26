## Description: <br>
亚马逊-Alexa购物助手 lets an agent ask Amazon's storefront Alexa shopping assistant one natural-language shopping prompt at a time and return Alexa's answer, curated product recommendations, ASINs, links, and follow-up questions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill for conversational shopping discovery on Amazon, including product recommendations, ASIN links, and follow-up questions from Alexa. It is best suited to single-turn or agent-summarized follow-up shopping prompts, optionally anchored to a specific Amazon page URL. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, optional Amazon page URLs, API credentials, and session metadata are sent to LinkFox services. <br>
Mitigation: Use only in trusted environments, avoid sensitive shopping intent when possible, and set LINKFOX_TOOL_GATEWAY only to a destination the user controls or trusts. <br>
Risk: The skill can consume LinkFox credits for successful Alexa shopping calls. <br>
Mitigation: Warn users before additional calls, rely on the built-in 24-hour cache for identical parameters, and avoid automatic retries, keyword changes, page turns, or postal-code probing after failures or empty results. <br>
Risk: Full API responses are persisted locally and may contain shopping intent, product choices, page context, screenshots, or session metadata. <br>
Mitigation: Periodically delete local linkfox response and cache files when they may contain sensitive information, and avoid forcing inline full-output mode unless needed. <br>
Risk: Automatic feedback submission may disclose user sentiment or task context to the feedback service. <br>
Mitigation: Review or disable feedback submission behavior when user context is sensitive or when organizational policy requires explicit approval. <br>
Risk: Alexa responses are live and non-deterministic, and each call starts a new session without cross-call memory. <br>
Mitigation: Treat recommendations as time-sensitive guidance, summarize prior results explicitly for follow-ups, and verify important product details before purchase decisions. <br>


## Reference(s): <br>
- [亚马逊 Alexa 购物助手 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-amazon-alexa-search) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown shopping report or structured JSON response, with full responses saved as JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Each API call supports one prompt; results may include Alexa answer text, grouped product recommendations, ASINs, prices, ratings, follow-up questions, screenshots, task metadata, cost tokens, and latency.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
