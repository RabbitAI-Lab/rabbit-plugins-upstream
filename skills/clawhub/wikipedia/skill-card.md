## Description:

Access Wikipedia through MCP to search articles, retrieve summaries, random facts, featured articles, historical events, categories, links, and related knowledge lookups across supported language editions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to retrieve Wikipedia-backed reference material, article summaries, discovery links, categories, and daily content hooks from an MCP-compatible agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Wikipedia queries and article titles are sent to Wikipedia.

Mitigation: Avoid sending sensitive or confidential search terms, article titles, or research topics through this skill.

Risk: The requests dependency is declared with a lower bound rather than an exact pinned version.

Mitigation: Install the skill in an isolated environment or pin requests during deployment for stronger reproducibility.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text returned through MCP tool responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include Wikipedia article links, thumbnail Markdown, plain-text extracts, and tabular daily metrics when supported by the release.]

## Skill Version(s):

1.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
