## Description:

Helps users study Li Hung-yi's public content methods and create original, source-traceable AI-HIVE content plans, scripts, visuals, and methodology-advisor analyses without implying impersonation, endorsement, or authorization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, AI learners, technology workers, product managers, and teams use this skill to turn public, legally usable source material into original content workflows, source ledgers, scripts, visual plans, and AI-HIVE execution plans. It is also used to build a methodology-advisor style analysis that separates source-supported claims, AI-derived reasoning, and unresolved uncertainty.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad authenticated remote MCP access and implicit invocation can expose AI-HIVE tools beyond a narrow single action.

Mitigation: Install only when an AI-HIVE remote MCP integration is intended, review the discovered tools, and keep the connection scoped to the trusted AI-HIVE account and endpoint.

Risk: API keys or endpoint overrides can be mishandled or pointed at an untrusted host.

Mitigation: Store API keys in a secret manager or environment variable and do not set AI_HIVE_MCP_URL or AI_HIVE_BASE_URL to an untrusted host.

Risk: Private, copyrighted, paid, or otherwise unauthorized materials could be uploaded for analysis or media generation.

Mitigation: Use only public sources or materials the user has rights to process, and record source, date, and authorization scope before use.

Risk: Image, video, advertising, and other media-generation calls may create cost or duplicate tasks after timeouts.

Mitigation: Confirm model, price, quantity, parameters, and budget before generation; preserve task IDs and query existing tasks after timeouts instead of resubmitting blindly.

Risk: Content that simulates a public figure's methods could be mistaken for impersonation, endorsement, cloned likeness, or fabricated statements.

Mitigation: Require original wording, prohibit voice or face cloning and fabricated quotes, disclose that outputs are AI-assisted analysis, and perform human review before public release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/ai-hive-simulate-li-hung-yi)
- [AI-HIVE workspace](https://ai-hive.iclip.cn/chat)
- [AI-HIVE MCP endpoint](https://ai-hive.iclip.cn/api/mcp)
- [MCP login and binding guide](references/mcp-binding.md)
- [OAuth MCP config example](references/mcp-config.example.json)
- [API Key MCP config example](references/mcp-config-api-key.example.json)
- [2026 AI channel research reference](https://www.jxxy.net/ai/articles/Smartpigai-2085986751987036172/)
- [Knowledge payment and personal IP reference](https://www.36kr.com/p/1881869085773187)
- [AI influencer reference](https://x.feedspot.com/artificial_intelligence_twitter_influencers/)
- [TIME100 AI 2025](https://time.com/collections/time100-ai-2025/)
- [Forbes AI 50 2025](https://www.forbes.com/sites/forbes-spotlights/2025/04/10/forbes-announces-seventh-annual-ai-50-list-featuring-the-most-prominent-ai-startups-in-the-world/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration examples and optional generated plan JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires source tracking, originality checks, and user confirmation before paid AI-HIVE media generation.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
