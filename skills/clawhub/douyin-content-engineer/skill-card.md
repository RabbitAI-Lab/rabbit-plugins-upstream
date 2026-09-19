## Description:

抖音内容引擎 helps agents search public Douyin content, fetch creator posts and video comments, and retrieve hot-list data for content research, competitor monitoring, sentiment analysis, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content, marketing, ecommerce, and operations teams use this skill to collect structured public Douyin data for topic research, competitor account monitoring, comment analysis, and trend discovery. Agents can map user intent to the appropriate command and return structured results for downstream reporting or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords or links and the Guaikei token to www.guaikei.com.

Mitigation: Install and run the skill only when that third-party data transfer is acceptable for the workspace and use case.

Risk: Local plaintext logs can contain research keywords, account or video identifiers, comments, and public user metadata.

Mitigation: Treat the generated logs directory as sensitive and delete or protect it in shared, synced, or backed-up workspaces.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/why20261/douyin-content-engineer)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-content-engineer)
- [Guaikei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples; command output is structured JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN. CLI results include a status envelope, request metadata, and Douyin result records when available.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
