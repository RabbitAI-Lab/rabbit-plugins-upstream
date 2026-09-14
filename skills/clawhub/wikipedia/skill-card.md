## Description:

Access Wikipedia via MCP to search articles, retrieve summaries and extracts, inspect article metadata, view page activity, and gather current or historical Wikipedia content across supported languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users can use this MCP skill to give agents read-only access to Wikipedia and Wikimedia information for research, content discovery, topical context, article metadata, page popularity, current events, and location-based article lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool inputs are sent to Wikimedia and Wikipedia APIs, which can expose confidential research terms or precise private coordinates.

Mitigation: Avoid submitting confidential queries, sensitive topics, or precise private coordinates through the skill.

Risk: The Python dependency is unpinned, which can change installed behavior over time.

Mitigation: Install in a normal user environment or virtual environment and review or pin the dependency before deployment.

Risk: The skill retrieves live Wikipedia and Wikimedia content, so outputs may reflect recent edits, public vandalism, or incomplete article coverage.

Mitigation: Review returned source links, revision context, and article content before relying on outputs in user-facing or high-impact workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown and plain text responses with source links, article metadata, media URLs, and structured lists where applicable.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only MCP tool responses; no API key required.]

## Skill Version(s):

1.6.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
