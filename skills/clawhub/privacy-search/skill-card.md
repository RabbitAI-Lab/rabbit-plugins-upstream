## Description:

Privacy Search helps agents run privacy-oriented, multi-engine web searches with strict and normal privacy modes, local SearXNG support, ranking and deduplication, result exports, synthesized answers, and engine health alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent operators use this skill to perform configurable web search workflows, inspect privacy posture, export results, and generate source-linked summaries while managing local SearXNG and engine health.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local search history and cache may retain sensitive queries on disk.

Mitigation: Decide whether local history is acceptable before installing; for sensitive searches, disable or clear cache/history and use strict mode.

Risk: Network integrations can disclose query or result details to configured search engines, LLM providers, webhook endpoints, or update checks.

Mitigation: Prefer local SearXNG for sensitive searches, disable update checks when needed, and only configure API keys or webhooks when that disclosure is acceptable.

Risk: The referenced configuration template is missing from the artifact.

Mitigation: Verify the expected settings or create config.yaml manually before running the skill.

Risk: Synthesized answers and fetched page content may be incomplete or inaccurate.

Mitigation: Review the cited sources and use fallback snippets or direct search results when page fetching or answer synthesis is unreliable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fyniujin/skills/privacy-search)
- [Quick Start](references/QUICK_START.md)
- [Search Engine Adapter Documentation](references/engines.md)
- [Domestic Engine and Fallback Guide](references/engines_zh.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, html, pdf, shell commands, configuration, guidance]

**Output Format:** [CLI text, JSON output, Markdown/HTML/PDF exports, configuration guidance, and source-linked synthesized answers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include cached search results, local history, privacy reports, self-test status, and citation-style answer synthesis.]

## Skill Version(s):

1.6.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
