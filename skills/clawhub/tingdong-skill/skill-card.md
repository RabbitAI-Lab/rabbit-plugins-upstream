## Description:

Converts user-provided article links from WeChat, Zhihu, or general webpages into AI-analyzed audio podcast episodes through the TingDong remote service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill when a user explicitly asks to convert an article link into an audio or podcast version. The skill submits the link to a remote podcast-generation API, monitors task status, and returns status text and the generated audio link when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Article links or text may be sent to a remote service over unencrypted HTTP.

Mitigation: Use only non-sensitive content, avoid private or confidential sources, and consider self-hosting or HTTPS before using the skill for protected material.

Risk: Automated article fetching may interact with sources that have access controls, paywalls, or anti-scraping restrictions.

Mitigation: Confirm that the user is authorized to convert the source content and prefer user-provided text or officially accessible sources when access terms are unclear.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/agentforge-cyber/skills/tingdong-skill)
- [听懂了 API 文档 (v1)](references/api_docs.md)
- [内容源处理策略](references/content_sources.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses with inline shell commands, JSON API results, task status text, and generated audio URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include task IDs, polling status, estimated wait times, errors, and MP3 links returned by the remote service.]

## Skill Version(s):

1.1.0 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
