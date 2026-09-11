## Description:

Detects and rewrites AI-flavored Chinese web-novel prose so the text reads more natural, less template-like, and closer to the author's intended style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Web-novel authors and editors use this skill to detect AI-flavored patterns in Chinese fiction, rewrite prose while preserving plot intent, and optionally apply file-based checks and punctuation cleanup to manuscript files.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify provided manuscript files.

Mitigation: Use detect-only wording when edits are not desired, and review changed text before accepting it.

Risk: Optional author memory can persist workspace-level style preferences.

Mitigation: Use explicit remember or forget requests to control what is stored, and avoid recording one-time instructions as long-term style preferences.

Risk: Style checks can flag functional prose patterns that should remain in the story.

Mitigation: Treat detector output as review guidance, preserve plot-critical content, and mark uncertain cases for follow-up instead of deleting them.

## Reference(s):

- [story-deslop skill page](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Anti-AI Writing Guide](references/anti-ai-writing.md)
- [Author Memory Protocol](references/author-memory.md)
- [Banned Words and Pattern Table](references/banned-words.md)
- [Deslop Gate Rules](references/deslop-gates.md)
- [Style Resolution Rules](references/style-resolution.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, rewritten manuscript text or file edits, inline shell commands, and local configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May edit provided manuscript files, run local report-only checks, normalize punctuation, and maintain optional workspace-level author-style memory when explicitly requested.]

## Skill Version(s):

1.1.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
