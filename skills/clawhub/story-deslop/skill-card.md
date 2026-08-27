## Description:

story-deslop detects and rewrites Chinese web-novel prose to reduce AI-like writing patterns while preserving plot, character intent, and narrative function.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agents use this skill to scan Chinese web-novel manuscripts for AI-like phrasing, produce concise findings, and make conservative rewrites that keep story facts intact.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may directly rewrite supplied manuscript files.

Mitigation: Use detection-only wording when only a report is desired, keep version control or backups for manuscripts, and review diffs before accepting edits.

Risk: The skill may retain local author-style preferences under .story/作者记忆 state.

Mitigation: Review or delete author-memory files when style habits should not be retained.

## Reference(s):

- [Anti-AI Writing Guide](references/anti-ai-writing.md)
- [Author Memory Protocol](references/author-memory.md)
- [Banned Words and Patterns](references/banned-words.md)
- [OpenClaw Source Metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-deslop)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and rewritten prose, with optional shell command snippets and local file updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run local check or normalization scripts; may edit manuscript files or update local author-style memory when requested.]

## Skill Version(s):

1.1.17 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
