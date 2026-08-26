## Description:

Retrieves traceable public social account and content data from X, Reddit, Xiaohongshu, Zhihu, LinkedIn, and WeChat Official Accounts through the SignalDig Social MCP for downstream analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jerrykik](https://clawhub.ai/user/jerrykik)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to retrieve public platform-native social posts, account profiles, content metadata, source URLs, timestamps, pagination state, and native metrics without turning the retrieval into strategy, scoring, or business recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill cannot retrieve data unless the SignalDig MCP server is connected with a valid API key.

Mitigation: Verify the social-growth-signals MCP tools are available before retrieval and stop rather than fabricating results when they are unavailable.

Risk: A SignalDig API key could be exposed if copied into shared files or prompts.

Mitigation: Store the API key only in the MCP client configuration and keep it out of repositories, shared skill files, and public transcripts.

Risk: Retrieved social data may be mistaken for exhaustive, representative, or decision-ready analysis.

Mitigation: Return source data with query, filter, and pagination boundaries, and avoid scoring, sentiment labels, strategy, or business recommendations inside this skill.

Risk: Native platform metrics may be conflated across platforms or treated as missing-zero values.

Mitigation: Keep platform-native metrics distinct and report absent metrics as unknown unless the live result explicitly returns zero.

## Reference(s):

- [Setup Guide](references/setup-guide.md)
- [Social Retrieval Functional Contract](references/mcp-contract.md)
- [Social Tool Parameter Guide](references/parameter-guide.md)
- [SignalDig](https://signaldig.com/)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown or structured text containing retrieved source data, request boundaries, pagination state, and native public metrics]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the social-growth-signals MCP server and a SignalDig API key; returned data must come from live tool results, not general knowledge or simulated results.]

## Skill Version(s):

1.3.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
