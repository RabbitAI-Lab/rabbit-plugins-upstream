## Description:

抖音热点数据追踪 helps agents query public Douyin trend, keyword search, creator post, and comment data through command-line tools and return structured JSON for content research, competitor analysis, and monitoring.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operations teams, marketers, and analysts use this skill to inspect public Douyin trends, search results, creator posts, and comments for topic research, competitor monitoring, campaign analysis, and public-sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords or links to www.guaikei.com and uses a GUAIKEI_API_TOKEN.

Mitigation: Use a dedicated token, confirm data-sharing approval before use, and avoid private or sensitive investigations.

Risk: Search, post, and comment results may be saved locally under the skill's logs directory.

Mitigation: Use a dedicated workspace and delete or protect logs when retained results could reveal business research or personal data.

Risk: Security evidence reports a mismatch between the skill's no-write claim and observed local result logging.

Mitigation: Review behavior before deployment and update operating guidance so users understand what data may be written locally.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-trend-data-track)
- [Server-resolved GitHub source](https://github.com/why20261/douyin-trend-data-track)
- [Server-resolved source commit](https://github.com/why20261/douyin-trend-data-track/tree/cf6280fed6fcfe95acda74a27ed6bd8ab1b692b4)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Guaikei API and token help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [JSON envelopes from command-line tools, with optional human-facing summaries by the calling agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN. Search, post, and comment results may be saved under the skill's logs directory.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter, package.json, and changelog report 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
