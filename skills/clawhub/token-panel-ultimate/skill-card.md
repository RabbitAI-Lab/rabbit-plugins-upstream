## Description:

TinkerClaw Token Panel tracks AI token usage, budgets, rate limits, and provider spending across Anthropic, OpenAI, Gemini, and Manus through a local dashboard and REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI-tool operators use this skill to monitor local AI provider usage, budget status, quota headroom, and spend across multiple providers. It is intended for agent-accessible local reporting and dashboard integration, not for exposing usage data on a public network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles real provider credentials and spending data.

Mitigation: Run it only from a trusted shell with a clean PATH, prefer OS keychain storage, avoid logging or sharing keys, and rotate provider keys if exposed.

Risk: The local REST API has unauthenticated GET endpoints that report spending and quota data.

Mitigation: Keep the API bound to localhost, do not expose port 8765, and set TOKEN_PANEL_API_TOKEN before using mutating endpoints.

Risk: Transcript parsing can read local session transcripts that contain prompts and replies.

Mitigation: Leave TOKEN_PANEL_READ_TRANSCRIPTS unset unless transcript parsing is explicitly needed and the privacy impact is understood.

Risk: Live provider probing can send real billable requests.

Mitigation: Use --probe only when live rate-limit validation is necessary and the billing or quota impact is acceptable.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/globalcaos/skills/token-panel-ultimate)
- [Anthropic Usage and Cost API documentation](https://platform.claude.com/docs/en/build-with-claude/usage-cost-api)
- [Gemini API pricing documentation](https://ai.google.dev/gemini-api/docs/pricing)
- [Gemini API rate limits documentation](https://ai.google.dev/gemini-api/docs/rate-limits)
- [Manus plans documentation](https://manus.im/docs/introduction/plans)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands plus JSON responses from the local API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local usage, quota, cost, budget, and alert information; stores counts and opaque identifiers rather than prompts or message content.]

## Skill Version(s):

2.6.1 (source: SKILL.md frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
