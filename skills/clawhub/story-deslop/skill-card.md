## Description:

Detects and reduces AI-style patterns in Chinese web fiction so prose reads more natural and less template-driven.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and developers use this skill to inspect Chinese web-fiction drafts for AI-style writing patterns, receive concise reports, and rewrite affected prose while preserving story function. It can also run local helper scripts for deterministic pattern checks and punctuation normalization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: File-mode cleanup can rewrite prose or normalize punctuation in place.

Mitigation: Run the skill on copies or version-controlled manuscripts and review diffs before accepting changes.

Risk: Style and pattern findings can require context-sensitive judgment rather than mechanical replacement.

Mitigation: Treat findings as review prompts and preserve plot, character details, and narrative function when editing.

## Reference(s):

- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [Anti-AI Writing Guide](references/anti-ai-writing.md)
- [Banned Words and Pattern Table](references/banned-words.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports, edited prose, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May modify user-provided manuscript files when file-mode cleanup or punctuation normalization is used.]

## Skill Version(s):

1.1.15 (source: server release metadata; artifact frontmatter says 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
