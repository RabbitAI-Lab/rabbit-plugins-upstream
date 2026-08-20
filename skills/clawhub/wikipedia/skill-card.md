## Description:

Access Wikipedia via MCP to search articles, retrieve summaries, fetch random and featured articles, and get language-aware general knowledge results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[evanfoglia](https://clawhub.ai/user/evanfoglia)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to connect an assistant to public Wikipedia lookup tools for research, content hooks, summaries, random facts, dinosaur facts, and featured articles across supported languages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tool calls make outbound requests to wikipedia.org and may disclose search terms or article titles to Wikipedia.

Mitigation: Install only where public Wikipedia network access and sending lookup terms to wikipedia.org are acceptable.

Risk: The requests dependency is declared with a lower bound rather than a pinned version.

Mitigation: Pin or constrain requests before installing in sensitive or reproducibility-focused environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/evanfoglia/skills/wikipedia)
- [Wikipedia REST API endpoint](https://en.wikipedia.org/api/rest_v1)
- [MediaWiki Action API endpoint](https://en.wikipedia.org/w/api.php)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown-formatted strings returned from MCP tool calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses can include source article links, thumbnail URLs, and language-specific Wikipedia results.]

## Skill Version(s):

1.1.2 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
