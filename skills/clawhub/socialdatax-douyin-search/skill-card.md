## Description:

Helps agents retrieve Douyin hot-search rankings and keyword-based work search results for content research, competitor analysis, and trend scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts, marketers, researchers, and agent developers use this skill to gather Douyin hot-search and keyword-search evidence for public content research, trend scanning, and competitive analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key for Douyin data lookups.

Mitigation: Confirm the user is comfortable providing `SOCIALDATAX_API_KEY` to the SocialDataX npm, CLI, or MCP integration before installation or execution.

Risk: Search and hot-list outputs can support interpretation but may not be complete or stable over time.

Mitigation: Keep observed ranking signals separate from interpretation and include traceable IDs, URLs, authors, counts, publish times, and content types when available.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-search)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with inline shell commands and JSON-derived observations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Douyin content IDs, URLs, titles or descriptions, authors, engagement counts, publish times, content type, and pagination guidance when available.]

## Skill Version(s):

0.1.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
