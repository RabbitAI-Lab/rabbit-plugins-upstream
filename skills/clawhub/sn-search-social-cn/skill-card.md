## Description:

Searches Chinese social platforms, with script entry points for Bilibili videos, Zhihu Q&A, and Douyin videos, plus browser fallback guidance for Xiaohongshu and Weibo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Chinese social platforms and return structured social search results for research, monitoring, or content discovery workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated platform cookies can expose account access if handled unsafely.

Mitigation: Use dedicated low-privilege or throwaway platform sessions, prefer environment variables over command-line cookie arguments, and avoid logging credentials.

Risk: Zhihu search can leave authenticated full-content results in persistent temporary files.

Mitigation: Delete generated Zhihu temporary files after use and avoid running the skill where those files may be retained or shared.

Risk: The skill uses internal platform APIs and unpinned dependencies that may change or be unsuitable for sensitive environments.

Mitigation: Review before installing, pin or remove dependencies before sensitive use, and fall back to visible public web results when scripts fail.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-search-social-cn)
- [Bilibili search endpoint](https://api.bilibili.com/x/web-interface/search/all/v2)
- [Zhihu search page](https://www.zhihu.com/search)
- [Douyin search page](https://www.douyin.com/search/)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON search results with optional Markdown guidance for browser fallback cases]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Script JSON includes success, query, provider, items, and error fields; Zhihu results may include truncated content with a temporary file path for full content.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
