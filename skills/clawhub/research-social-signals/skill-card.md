## Description:

Retrieve traceable, public, platform-native social data from X, Reddit, Xiaohongshu, Zhihu, LinkedIn, and WeChat Official Accounts through the SignalDig Social MCP.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agent builders use this skill to retrieve traceable public social posts, profiles, trends, source URLs, timestamps, native metrics, and pagination state for downstream analysis. The skill validates retrieval parameters and preserves collection boundaries without making marketing, sentiment, account-performance, SEO, or business decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live social-data retrieval can create provider-side request, quota, freshness, or paid-call implications.

Mitigation: Validate the requested platform, query, account, filters, and pagination depth before calling tools; reuse existing results when appropriate and avoid automatic pagination.

Risk: Returned social data may be incomplete, ranking-dependent, time-bounded, or non-representative.

Mitigation: Return the effective request parameters, source URLs, timestamps, native metrics, pagination state, and retrieval errors so downstream analysis can account for collection boundaries.

Risk: Ambiguous account identifiers, cursors, tokens, or filters can retrieve the wrong data or create misleading coverage.

Mitigation: Ask for missing public identifiers, explain invalid parameters, and use only continuation values returned by the immediately preceding matching result.

Risk: Downstream users may over-interpret source observations as sentiment, strategy, account quality, or business recommendations.

Mitigation: Keep the skill limited to retrieval and data-quality notes; do not generate scores, sentiment labels, opportunity rankings, performance judgments, or next-action recommendations.

## Reference(s):

- [Social Retrieval Functional Contract](references/mcp-contract.md)
- [Social Tool Parameter Guide](references/parameter-guide.md)
- [SignalDig](https://signaldig.com/)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown or structured text with retrieval parameters, source data, URLs, timestamps, native metrics, pagination state, and safe error summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves platform-native metrics and collection boundaries; avoids scores, recommendations, sentiment labels, and business decisions.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
