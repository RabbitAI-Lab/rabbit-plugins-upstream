## Description:

Retrieves structured public Douyin search, hot-list, creator-post, and comment data for competitor research, trend tracking, content strategy comparison, and brand content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External users such as brand teams, content operators, and creators use this skill to gather public Douyin data for topic research, competitor monitoring, comment insight, and trend tracking. Agents can route user requests to the appropriate Node.js CLI and return structured results for downstream analysis or reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the GUAIKEI_API_TOKEN and requested Douyin queries or links to guaikei.com.

Mitigation: Install and run it only when guaikei.com is trusted for the intended use, and keep the API token scoped and protected.

Risk: Public comments, profile metadata, and other retrieved results may be saved in local logs.

Mitigation: Collect only the amount of data needed for the task and review or delete the logs directory when results may contain personal or sensitive audience information.

Risk: The skill can request large result sets for search, posts, or comments.

Mitigation: Use explicit user intent and conservative limits before increasing collection volume.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/dou-yin-data-insight)
- [Guaikei API Token Portal](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured CLI JSON output.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI commands write JSON to stdout; result logs may also be saved locally under the skill logs directory.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, release metadata, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
