## Description:

Access Wikipedia via MCP for article search, summaries, random facts, featured content, historical events, categories, links, view counts, current news, most-read articles, media, and multi-language lookups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users, employees, and developers use this MCP server to retrieve Wikipedia and Wikimedia information for research, content discovery, article exploration, media lookup, current events, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia and Wikimedia lookup terms, article interests, and coordinates are sent to external services.

Mitigation: Use the skill only in environments where outbound requests to Wikipedia and Wikimedia are approved, and avoid submitting sensitive research terms or precise private locations.

Risk: Unpinned Python dependencies can change behavior over time.

Mitigation: Deploy with a locked environment or pinned dependency set before production use.

## Reference(s):

- [ClawHub Wikipedia MCP Skill Page](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown and plain text responses from MCP tool calls, often including source article links and media URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on live Wikipedia and Wikimedia API responses; no API key is required.]

## Skill Version(s):

1.5.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
