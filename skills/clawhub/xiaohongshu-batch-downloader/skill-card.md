## Description:

Retrieves public Xiaohongshu/RedNote notes, creator posts, note details, and comments through Node.js command scripts for content research, market analysis, competitor monitoring, KOL screening, and sentiment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, creators, marketers, and analysts use this skill to query public Xiaohongshu keywords, note links, or creator profile links and receive structured data for content planning, competitive research, trend monitoring, creator evaluation, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Xiaohongshu links, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use a dedicated API token, avoid submitting sensitive or non-public inputs, and disclose the third-party API data flow before use.

Risk: Returned public Xiaohongshu data may be saved in local temp logs.

Mitigation: Store logs only where appropriate, restrict access to the working directory, and delete logs that contain data no longer needed.

Risk: Comment, profile, and interaction data can carry privacy and platform-compliance obligations even when sourced from public pages.

Mitigation: Use the skill only for public content and handle results according to Xiaohongshu platform rules and applicable privacy expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/xiaohongshu-batch-downloader)
- [Project homepage](https://github.com/um-why/xiaohongshu-openclaw-skill)
- [Guaikei API and token setup](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Troubleshooting guide](references/troubleshooting.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; commands return public Xiaohongshu data and may save local result logs.]

## Skill Version(s):

1.1.4 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
