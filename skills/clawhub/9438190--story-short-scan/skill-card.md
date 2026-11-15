## Description:

Analyzes short-form Chinese web fiction rankings across platforms such as Zhihu Yanyan, Qimao, Heiyan, and Dianzhong to identify market themes, emotional hooks, trend candidates, and validation actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[9438190](https://clawhub.ai/user/9438190)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and publishing analysts use this skill to scan short-fiction market samples, compare platform patterns, and turn ranking evidence into topic directions, risk thresholds, and follow-up validation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Heiyan scraper can reuse a logged-in admin browser session and call management APIs with an extracted Admin-Token cookie.

Mitigation: Run it only with explicit authorization, prefer a dedicated low-privilege Chrome profile, and avoid personal or high-privilege admin sessions.

Risk: Generated ranking reports may contain sensitive internal catalog data from authenticated sources.

Mitigation: Treat generated reports as sensitive, store them in approved locations, and review contents before sharing outside the authorized team.

Risk: Historical market reference data can become stale in fast-moving short-fiction markets.

Mitigation: Require current scan dates, trend confidence, and rescan timing before using recommendations as active market guidance.

## Reference(s):

- [Story Short Scan ClawHub page](https://clawhub.ai/9438190/skills/story-short-scan)
- [OpenClaw metadata source](https://github.com/worldwonderer/oh-story-claudecode)
- [Short-form fiction market reference](references/real-market-data.md)
- [Dianzhong male short-fiction browse page](https://www.ishugui.com/browse)
- [Dianzhong female short-fiction browse page](https://www.ishugui.com/browse/on3)
- [Heiyan management booklist page](https://manage.zhangwenpindu.cn/books/booklist)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports with optional shell commands and generated Markdown data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include sample date, trend confidence, expiry or rescan timing, topic candidates, saturation risks, and validation actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
