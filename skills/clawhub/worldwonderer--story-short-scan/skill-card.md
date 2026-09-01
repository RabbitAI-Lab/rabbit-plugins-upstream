## Description:

Analyzes short-form web fiction ranking data from platforms such as Zhihu Yanyan, Qimao, Heiyan, and Dianzhong to identify trending themes and market signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative-market analysts use this skill to scan short-form web fiction rankings, compare platform patterns, and produce actionable topic, emotion, saturation-risk, and validation recommendations. When live scraping is unavailable, it can fall back to provided ranking data or historical reference material while labeling the limits of that evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Heiyan workflow reads a logged-in browser admin cookie and uses it as a Bearer token for management API calls.

Mitigation: Run the scraper only in a separate browser profile with a limited read-only account, and avoid using accounts with broad administrative privileges.

Risk: Scraped ranking reports may include private or account-scoped data from authenticated sessions.

Mitigation: Review generated Markdown before sharing or publishing and remove private account, author, or operational details that should not leave the collection environment.

Risk: Historical market-reference data can become stale for fast-moving short-form fiction trends.

Mitigation: Use current scan results when possible and label fallback analysis as historical hypotheses until the target platforms are rescanned.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-scan)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Short-form web fiction market reference](artifact/references/real-market-data.md)
- [Dianzhong browse target](https://www.ishugui.com/browse)
- [Heiyan management target](https://manage.zhangwenpindu.cn/books/booklist)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Shell commands, Guidance, Files]

**Output Format:** [Markdown reports with tables, rankings, recommendations, and optional scraper-generated data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include sample date, confidence, trend validity window, saturation risk, and next rescan timing.]

## Skill Version(s):

1.1.11 (source: server release metadata; packaged frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
