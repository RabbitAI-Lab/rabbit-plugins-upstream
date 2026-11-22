## Description:

Retrieves public Douyin videos, creator profiles, post details, comments, and trending topics as structured JSON for content and market analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content, social media, and market researchers use the skill to discover public Douyin videos and creators, review post engagement and comments, and track trending topics for planning and internal analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and supplied Douyin links or IDs are sent to GUAIKEI's third-party API.

Mitigation: Avoid sending sensitive terms or identifiers; submit only the public information needed for the requested lookup.

Risk: ClawScan reports account discovery beyond the declared capabilities, and some components were only partially inspected.

Mitigation: Review account-search results before use, keep analysis to public information, and review the skill before using it in sensitive workflows.

## Reference(s):

- [GUAIKEI service and API access](https://www.guaikei.com)
- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-daily-hot-keywords)
- [Douyin platform](https://www.douyin.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON with concise summaries or analysis when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One JSON envelope per command; most query results are also saved under the skill's logs/ directory.]

## Skill Version(s):

1.5.0 (source: SKILL.md frontmatter, package.json, changelog released 2026-11-10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
