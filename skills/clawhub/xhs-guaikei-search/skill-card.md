## Description:

Searches XiaoHongShu public notes, note details, comments, and creator posts through Guaikei API-backed CLI commands, returning structured data for trend research, competitor analysis, KOL screening, and comment insight.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, marketers, and analysts use this skill to retrieve public XiaoHongShu content and interaction data for keyword research, note review, comment analysis, creator monitoring, trend tracking, and competitor analysis. It does not support login, posting, liking, or access to private content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, XiaoHongShu URLs, and the GUAIKEI_API_TOKEN are sent to guaikei.com to fulfill requests.

Mitigation: Install and run only when this third-party API use is acceptable for the intended data and authorization context.

Risk: Successful results are saved locally in logs/, which can retain sensitive queries or collected public datasets.

Mitigation: Review and clear local logs when queries, URLs, or returned datasets should not be retained.

Risk: The skill only retrieves public XiaoHongShu data and may return empty or error results for deleted, private, restricted, or unavailable content.

Mitigation: Treat empty or error responses as non-results, verify source links, broaden filters when appropriate, and avoid fabricating conclusions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/xhs-guaikei-search)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Guaikei API Website](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON, files]

**Output Format:** [JSON command output and local JSON log files, often summarized by the agent as Markdown or text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; successful results are saved under logs/.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
