## Description:

获取小红书博主公开作品列表，可配合笔记详情看单篇表现。当用户想了解某个小红书博主发什么、发多勤、哪些火时使用本技能；即使用户没说"博主分析"，只要给了主页链接并想看其作品也适用。不用于粉丝画像或后台数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content teams, and market analysts use this skill to retrieve public Xiaohongshu search results, note details, comments, and creator post lists for topic research, competitor monitoring, KOL screening, and trend analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu keywords or URLs to GuaiKei using GUAIKEI_API_TOKEN.

Mitigation: Use only approved public-data workflows, keep GUAIKEI_API_TOKEN secret, and avoid pasting the token into chats, command output, or logs.

Risk: Fetched public comments and post data can be saved to local JSON logs.

Mitigation: Review and delete local logs when the retained Xiaohongshu content is no longer needed.

Risk: The skill is limited to public Xiaohongshu data and can return empty or error results for deleted, private, inaccessible, or mismatched links.

Mitigation: Validate whether the input is a keyword, note URL, or creator profile URL before execution, and report empty or failed results without inventing data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/xhs-competitor-watch-guaikei)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [GuaiKei API service](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return structured JSON with status, request metadata, skill metadata, and results, and successful runs may save JSON logs locally.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter and package metadata report 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
