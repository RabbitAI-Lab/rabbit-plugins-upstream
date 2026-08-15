## Description:

Access Wikipedia via MCP to search articles, get summaries, retrieve random facts, fetch dinosaur facts, and return today's featured article across ten supported Wikipedia languages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

Developers and agents use this MCP server to look up Wikipedia search results, article summaries, random articles, trivia-style facts, dinosaur facts, and featured articles without requiring an API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia search terms and article titles are sent to Wikipedia.

Mitigation: Use the skill only for queries that are acceptable to disclose to Wikipedia, and avoid sensitive or confidential search terms.

Risk: The release depends on an unpinned Python dependency range.

Mitigation: For stronger reproducibility, deploy from a vetted environment or lock the Python dependency versions before production use.

Risk: Returned facts and summaries come from live Wikipedia content and may change or contain errors.

Mitigation: Review retrieved content before using it in high-stakes, customer-facing, or regulated workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia-mcp)
- [Wikipedia REST API endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown text with source links and optional image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tool responses may include Wikipedia article links, snippets, summaries, and thumbnail image URLs.]

## Skill Version(s):

1.1.2 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
