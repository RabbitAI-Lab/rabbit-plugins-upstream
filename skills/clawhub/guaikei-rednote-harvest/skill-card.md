## Description:

搜小红书笔记、看笔记详情、查笔记评论、查博主作品；当用户提供关键词或小红书链接并需要公开内容数据时使用。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

Content creators, marketers, analysts, and operators use this skill to collect public Xiaohongshu note, comment, author, and profile-post data for topic research, competitive analysis, KOL screening, and sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Xiaohongshu keywords or links are sent to guaikei.com with the configured GUAIKEI_API_TOKEN.

Mitigation: Use only inputs that are approved for this third-party API, and avoid sending sensitive client research unless that sharing is authorized.

Risk: Result logs can contain research queries, comments, profile data, or client work on the local machine.

Mitigation: Review and delete generated logs when they contain sensitive material, especially on shared machines or systems with backup or log collection.

Risk: The skill is intended for public Xiaohongshu data and can fail or misroute when given private, hidden, or mismatched links.

Mitigation: Use public note links for detail and comment commands, public profile links for post collection, and ask for clarification when the target is unclear.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-rednote-harvest)
- [Guaikei API token and support](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Structured JSON results with brief human-facing summaries and command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN. Successful runs may write result JSON files under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
