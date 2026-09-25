## Description:

Multi search engine integration with 16 engines (7 CN + 9 Global). Supports advanced search operators, time filters, site search, privacy engines, and WolframAlpha knowledge queries. No API keys required.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiiang0529](https://clawhub.ai/user/xiiang0529)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build web search workflows that select Chinese or international search engines, apply advanced search operators and time filters, and summarize aggregated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries can be sent to multiple external search providers, possibly in different jurisdictions.

Mitigation: Review intended queries before use, avoid sensitive topics or regulated data, and limit provider selection to jurisdictions acceptable for the deployment.

Risk: The artifact privacy notice states there is no external data transmission, which conflicts with the skill behavior and security summary.

Mitigation: Update user-facing privacy disclosures and installation review notes to state that search terms are transmitted to external providers.

Risk: Automated searches may conflict with provider terms, rate limits, or crawling policies.

Mitigation: Keep rate limiting enabled, respect provider policies, and require users to confirm search-engine terms before commercial use.

## Reference(s):

- [Multi Search Engine ClawHub Listing](https://clawhub.ai/xiiang0529/skills/multi-search-engine)
- [Domestic Search Guide](references/advanced-search.md)
- [International Search Guide](references/international-search.md)
- [Baidu Advanced Search Syntax](https://baike.baidu.com/item/搜索语法)
- [Bing Search Tips](https://cn.bing.com/tips)
- [Sogou Search Help](https://help.sogou.com/)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown search guidance and report text with web_fetch JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No API keys are required; search queries may be sent to selected external search providers.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact version files also cite 2.1.0 and 2.1.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
