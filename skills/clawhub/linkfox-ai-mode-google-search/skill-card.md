## Description:

Retrieves Google AI Mode / AI Overview results for a single keyword and returns the synthesized answer with source links as Markdown.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to get AI-summarized live web information from Google AI Mode for deep research, technical questions, market preference analysis, and long-tail product research. It is intended for single-question searches; follow-up questions require summarizing prior context into a new keyword.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries, feedback text, phone/SMS login data, API keys, order metadata, and saved response files may be handled by LinkFox services.

Mitigation: Use only after confirming LinkFox data handling is acceptable, avoid sensitive searches, and review locally saved response files before sharing or committing them.

Risk: The skill includes paid service, billing, payment, and credential creation flows.

Mitigation: Confirm costs with the user before additional calls, use the documented onboarding flow for 401 or 402 errors, and do not create orders or credentials without user consent.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox services.

Mitigation: Set endpoint override environment variables only for destinations the operator controls and trusts.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-ai-mode-google-search)
- [Google AI 搜索 API 参考](references/api.md)
- [解决认证和积分问题](references/onboarding.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Files, Shell commands, Configuration guidance]

**Output Format:** [Markdown search summary with citation links, plus JSON responses or compact stdout summaries saved to local files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single keyword per call; results are live and may vary; API calls consume LinkFox credits and may require account, API key, and billing setup.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
