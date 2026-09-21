## Description:

按关键词、点赞、类目和市场筛选快手带货达人，结合达人互动数据、作品表现数据和带货效果给出合作优先级，找到真正和品类、受众及目标匹配的快手达人候选。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External operators, marketers, creators, and analysts use this skill to retrieve Kuaishou public video, creator, and comment data for creator matching, content research, competitor monitoring, and trend analysis. Agents can route keyword searches, creator profile lookups, and video comment collection to the appropriate command and return structured results for downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou keywords, profile or video URLs, request parameters, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and run it only when that data sharing is acceptable for the intended workflow.

Risk: Collected public comments or creator data may be saved in generated local logs.

Mitigation: Review and delete generated logs when the collected data should not remain on disk or enter backups or source control.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/kuaishou-creator-match)
- [Publisher Profile](https://clawhub.ai/user/why20261)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands require Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved to local logs.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
