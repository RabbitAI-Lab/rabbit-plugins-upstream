## Description:

Removes AI-like polish from Chinese web-fiction prose by detecting formulaic phrasing and rewriting text toward more natural, scene-grounded narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External writers and editors use this skill to review Chinese web-fiction passages for AI-like diction, rhythm, summary endings, and formulaic sentence patterns, then produce a concise report and revised prose that preserves plot intent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may rewrite prose style aggressively when text is pasted for editing.

Mitigation: Ask for detection-only feedback or review the generated report before accepting rewrites.

Risk: File-based workflows can modify manuscript files.

Mitigation: Keep backups or run check-only commands before applying normalization or rewrite changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-deslop)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [anti-ai-writing.md](references/anti-ai-writing.md)
- [banned-words.md](references/banned-words.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown reports, revised prose, and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide detection-only feedback or rewrite pasted text; file workflows can update local manuscript files when explicitly used.]

## Skill Version(s):

1.1.13 (source: server release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
