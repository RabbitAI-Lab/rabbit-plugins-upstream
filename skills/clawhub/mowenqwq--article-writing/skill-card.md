## Description:

A Chinese article-writing experience vault for posts, op-eds, copywriting, long-form analysis, script drafts, rewriting, polishing, and pre-publication checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mowenqwq](https://clawhub.ai/user/mowenqwq)

### License/Terms of Use:

MIT

## Use Case:

Writers, editors, marketers, and agent operators use this skill to draft, revise, fact-check, and polish Chinese articles for general audiences. It emphasizes reader-first wording, source-backed claims, main-line focus, contrastive argument, and a pre-publication checklist.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to revise its own skill instructions after future writing tasks, which could persist unreviewed or draft-influenced guidance.

Mitigation: Keep the installed skill read-only during normal use, or require explicit approval and a visible diff before any change to SKILL.md.

Risk: Untrusted drafts could try to influence persistent writing guidance.

Mitigation: Treat draft content as task input only and review any proposed persistent guidance changes before accepting them.

## Reference(s):

- [Skill Definition](artifact/SKILL.md)
- [README](artifact/README.md)
- [ClawHub Skill Page](https://clawhub.ai/mowenqwq/skills/article-writing)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown or plain text writing guidance, outlines, edits, checklists, and source-list prompts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable code; guidance may include recommendations for revising the skill document under its living-document protocol.]

## Skill Version(s):

1.1.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
