## Description:

搜索引擎 helps agents gather and summarize search results across 16 Chinese and global search engines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent users use this skill to gather, compare, and summarize public web search results across multiple engines for security research, audits, and decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file and command authority that is not well scoped for a web-search workflow.

Mitigation: Grant only the minimum tools needed for search, and avoid shell execution or write access unless those behaviors are explicitly required.

Risk: Search queries and API credentials may expose sensitive information to external services if used without scoping.

Mitigation: Redact sensitive query content, use scoped API keys, and avoid storing personal or confidential search history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/multi-search-engine)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [SkillHub listing](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell/API snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search workflows take a query and optional engine list; outputs may include aggregated results, summaries, troubleshooting guidance, and configuration steps.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.1.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
