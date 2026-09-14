## Description:

Helps AI agents convert daily corrections, errors, positive signals, and weekly retrospectives into structured local memory, verified rules, and reviewed skill drafts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to help an LLM agent maintain durable local memory, record mistakes and corrections, run scheduled reflection, verify recurring rules before promotion, and propose new skill drafts for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives an agent broad durable authority to record conversations and rewrite future behavior files.

Mitigation: Require explicit human review before accepting changes to MEMORY.md, SOUL.md, TOOLS.md, AGENTS.md, or newly generated skills.

Risk: Conversation or error logs may contain secrets or sensitive details before they are written to durable memory.

Mitigation: Add secret redaction before logging errors, corrections, feature requests, or daily diary entries.

Risk: Persistent memory rewrites may overwrite useful context or introduce incorrect long-term guidance.

Mitigation: Keep backups or diffs for persistent memory files and review proposed promotions before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/muippt/skills/mu-self-evolve)
- [Project landing page](https://muippt.github.io/mu-self-evolve/)
- [Claude Code compatibility](references/claude-code-compat.md)
- [File structure and taxonomy](references/file-structure.md)
- [Record templates](references/record-templates.md)
- [Weekly reflection workflow](references/weekly-reflection.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, local file templates, summaries, and draft skill scaffolds]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for human review before durable memory, behavior-file, schedule, or new-skill changes are accepted.]

## Skill Version(s):

3.1.0 (source: frontmatter and changelog, released 2026-09-09)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
