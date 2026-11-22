## Description:

Retrieves public Douyin videos, creator posts, work details, comments, and trending lists as structured JSON for content research and account analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Social media operators, marketers, content planners, and analysts use this skill to research public Douyin content, compare creator accounts, review engagement and comments, and track trending topics. It returns structured data that an agent can summarize for topic planning, competitor research, or sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an API token and sends submitted Douyin search terms, links, or IDs to the GUAIKEI service; the security scan was benign but had medium confidence and partial inspection.

Mitigation: Use only queries and public Douyin links you intend to send to that service. Keep GUAIKEI_API_TOKEN in a protected environment variable and do not disclose it in chat or shared logs.

Risk: Saved JSON results can contain creator and comment data that may be sensitive when shared outside the intended analysis.

Mitigation: Review and redact saved results before sharing them, and remove local result logs when they are no longer needed.

## Reference(s):

- [Skill instructions](artifact/SKILL.md)
- [Usage and output documentation](artifact/readme.md)
- [Output contract](artifact/references/contract.md)
- [Command options](artifact/references/options.md)
- [GUAIKEI service](https://www.guaikei.com)
- [Douyin](https://www.douyin.com)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [Structured JSON results, with agent-written text summaries or analysis when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Most query results are also saved as JSON logs in the skill directory; the hot list is not saved.]

## Skill Version(s):

1.5.0 (source: frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
