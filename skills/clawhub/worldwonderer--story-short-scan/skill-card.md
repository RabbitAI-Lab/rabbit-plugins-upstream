## Description:

Short web-fiction market scan skill that analyzes popular short-story data from Zhihu Yanyan, Qimao, Heiyan, Dianzhong, and related inputs to identify current topic and emotion trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, editors, and market researchers use this skill to scan short web-fiction rankings, compare platform patterns, and turn current samples or provided lists into topic, emotion, and validation guidance. It can also run browser-assisted scrapers for Dianzhong and Heiyan when the required browser session is available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Heiyan workflow uses a logged-in admin browser session and extracts an admin cookie as a bearer token to read management API data.

Mitigation: Use a dedicated low-privilege account and separate browser profile, review the scripts before running them, and avoid accounts that can modify business data or expose sensitive inventory.

Risk: Market signals and built-in platform reference data can become stale quickly or be wrong when pages and API fields change.

Mitigation: Require current scan dates, trend confidence, and next rescan timing in reports; treat historical reference data as hypotheses until validated against fresh samples.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-short-scan)
- [Publisher profile](https://clawhub.ai/user/worldwonderer)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Short web-fiction cross-platform writing reference](references/real-market-data.md)
- [Dianzhong browse page](https://www.ishugui.com/browse)
- [Heiyan booklist page](https://manage.zhangwenpindu.cn/books/booklist)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, analysis, files]

**Output Format:** [Markdown reports with tables, ranked recommendations, validation notes, and optional scraper-generated markdown files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should include sample date, trend confidence, data source, and next rescan timing; scraper output includes quality signals when parsing may be incomplete.]

## Skill Version(s):

1.1.10 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
