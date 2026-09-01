## Description:

Archives Zhihu collections, articles, answers, questions, columns, and profile history into Markdown with local images and optional Obsidian exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[handsomestwei](https://clawhub.ai/user/handsomestwei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content archivists use this skill to route Zhihu URLs, collect item lists, fetch article or answer bodies and images, resume interrupted runs, and optionally export source mirrors or notes into Obsidian.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Zhihu browsing persists cookies and browser profile data in local workspace files.

Mitigation: Use a dedicated workspace, avoid shared machines, and delete or protect zhihu_cookies.json and chrome_user_data after use.

Risk: Stealth and keepalive behavior may conflict with site rules or user expectations.

Mitigation: Confirm the intended use is authorized, keep crawl limits enabled, and stop runs that trigger access warnings or rate-limit behavior.

Risk: Obsidian export workflows can move or delete local export files.

Mitigation: Back up the vault and test exports in a disposable vault before running against important notes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/handsomestwei/skills/zhihu-fetch-skill)
- [Skill entry and command reference](SKILL.md)
- [README](README.md)
- [Script dependency list](scripts/requirements.txt)
- [Playwright documentation](https://playwright.dev/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands; runtime scripts produce JSON lists, Markdown articles, local image files, progress summaries, and optional Obsidian notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist cookies and browser profile data in the workspace, and Obsidian export workflows may move source Markdown files.]

## Skill Version(s):

2.2.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
