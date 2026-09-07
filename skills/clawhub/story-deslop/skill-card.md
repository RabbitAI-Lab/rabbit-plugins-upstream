## Description:

网文去AI味。检测并清除文本中的AI写作痕迹，让文字回归自然、非模板化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and writing agents use this skill to scan Chinese web-novel prose for AI-flavored patterns, produce concise issue reports, and rewrite text while preserving plot, character intent, and narrative function.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Rewrite mode can change manuscript files.

Mitigation: Use check-only mode when only a report is needed, and review proposed edits before accepting rewritten manuscript content.

Risk: The skill can store explicit long-term style preferences locally in .story/作者记忆.

Mitigation: Use the documented forget or replace flows when stored preferences should be changed or removed.

## Reference(s):

- [story-deslop ClawHub Page](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [OpenClaw Source Metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [anti-ai-writing.md](references/anti-ai-writing.md)
- [author-memory.md](references/author-memory.md)
- [banned-words.md](references/banned-words.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and revised prose, with optional shell commands and local file edits when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit check-only reports, rewrite prose, normalize punctuation, or update local author-style memory according to the user's request.]

## Skill Version(s):

1.1.19 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
