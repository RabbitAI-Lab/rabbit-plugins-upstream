## Description:

抖音内容研究 helps agents retrieve public Douyin search results, hot lists, creator posts, and comments as structured data for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content operators, brand researchers, creators, and agents use this skill to collect public Douyin data for topic research, competitor monitoring, trend tracking, comment analysis, and downstream reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, URLs, account or video identifiers, and the Guaikei API token are sent to guaikei.com.

Mitigation: Install only when that data sharing is acceptable, keep the token secret, and rotate it if exposed.

Risk: Retrieved data is automatically saved locally in the skill's logs directory.

Mitigation: Avoid shared workspaces unless logs are managed or deleted according to the user's data-handling policy.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-content-research-v1)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-content-research-v1)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Guaikei API site](https://www.guaikei.com)
- [Changelog](references/changelog.md)
- [Options reference](references/options.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON from CLI stdout with concise text guidance for command selection and interpretation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; operational logs may be written under the skill's logs directory.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
