## Description: <br>
Research-grade Tavily web search and URL extraction for OpenClaw using native Node.js, with caching, usage stats, and rate-limit backoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jwestburg](https://clawhub.ai/user/jwestburg) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill for deep web research, Tavily search, multi-URL extraction, usage review, cache inspection, and source-backed research follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries and extraction URLs are sent to Tavily as a third-party research API. <br>
Mitigation: Use the skill only for approved external research and avoid client/private or sensitive queries unless that external transmission is approved. <br>
Risk: Default cache and usage-log behavior can leave local records of queries, URLs, and results. <br>
Mitigation: Use --no-log --no-cache for sensitive approved work, and review or clear local cache entries only with explicit approval. <br>
Risk: Cached results are not scoped to a specific Tavily account when multiple accounts share the same OS user profile. <br>
Mitigation: Use separate OS profiles or --no-cache when account isolation matters. <br>
Risk: Local/private URL refusal is a guardrail for obvious mistaken extract targets, not a complete boundary for all network misuse scenarios. <br>
Mitigation: Extract only intended public HTTP(S) URLs and review URLs before sending them to Tavily. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jwestburg/skills/tavily-search-pro-native-node) <br>
- [Publisher profile](https://clawhub.ai/user/jwestburg) <br>
- [Tavily Pro Contract](references/tavily-pro-contract.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON command output with URLs, source summaries, cache/log status, freshness choices, and estimated Tavily credit usage.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include command plans, source/result URLs, limitations, caveats, and next safe research steps.] <br>

## Skill Version(s): <br>
1.0.20 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
