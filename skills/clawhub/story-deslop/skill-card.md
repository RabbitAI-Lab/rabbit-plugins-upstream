## Description:

story-deslop detects and reduces formulaic AI-flavored Chinese web-novel prose while preserving plot intent, character facts, and narrative continuity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and editors use this skill to scan Chinese web-novel text for AI-flavor patterns, produce concise issue reports, and rewrite or polish manuscript passages without changing the story premise. In file mode it can apply local manuscript edits and run bundled style, degeneration, and punctuation checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify supplied manuscript files in local writing workspaces.

Mitigation: Run it only where local manuscript edits are intended, review diffs before accepting changes, and use detection-only mode when edits are not desired.

Risk: The skill can store long-term writing preferences locally when the user explicitly expresses them.

Mitigation: Review or delete .story/作者记忆 if persistent style memory is not wanted.

Risk: Style-cleanup heuristics may over-edit functional wording or weaken narrative continuity.

Mitigation: Follow the skill's deletion limits, preserve plot and character facts, and mark uncertain changes for human review instead of forcing rewrites.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [Publisher profile](https://clawhub.ai/user/worldwonderer)
- [references/banned-words.md](references/banned-words.md)
- [references/anti-ai-writing.md](references/anti-ai-writing.md)
- [references/author-memory.md](references/author-memory.md)
- [metadata.openclaw.source](https://github.com/zenstory-ai/oh-story-claudecode)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, rewritten prose, local file edits, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit issue tables, before-and-after excerpts, bounded rewrite summaries, local check results, and author-memory receipts.]

## Skill Version(s):

1.1.18 (source: ClawHub release evidence; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
