## Description:

抖音爆款选题 retrieves public Douyin keyword search results, creator posts, comments, and trending lists as structured JSON for content research, competitor monitoring, sentiment analysis, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketing teams, and analysts use this skill to collect public Douyin data for topic ideation, account benchmarking, comment review, and hot-list monitoring. Agents invoke Node.js command-line tools and return structured JSON that can feed reports, spreadsheets, or downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, monitored account links, comment targets, and the API token are sent to www.guaikei.com.

Mitigation: Use the skill only when third-party API disclosure is acceptable, avoid sensitive queries or links, and confirm token handling with the deploying organization.

Risk: Search, post, and comment results are automatically saved in local plaintext JSON log files.

Mitigation: Run the skill in an approved workspace, protect or delete generated logs after use, and avoid collecting sensitive datasets unless local retention is permitted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-hot-title-creation)
- [Server-resolved source repository](https://github.com/why20261/douyin-hot-title-creation)
- [Douyin data API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, API calls, Guidance]

**Output Format:** [Structured JSON envelopes with status, request metadata, and result arrays; guidance may include inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, comment, and hot-list commands read public Douyin data and do not perform account write actions.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter, package.json, and changelog declare 1.3.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
