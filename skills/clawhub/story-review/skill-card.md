## Description:

story-review coordinates multi-perspective adversarial reviews of Chinese web-fiction drafts, using deployed reviewer agents when available and falling back to solo review with embedded rubrics when needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and development teams use this skill to review web-fiction chapters for structure, character behavior, prose quality, platform fit, continuity, and concrete revision opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads local story, outline, setting, and continuity files during review.

Mitigation: Run it only in the intended project workspace and avoid using it on drafts or notes the user does not want included in review context.

Risk: Full and lean review modes can maintain continuity files under `追踪/`.

Mitigation: Use `solo` for report-only review, and inspect changes under `追踪/` after full or lean runs.

Risk: Bundled Node and Python checks can influence the final findings and recommendations.

Mitigation: Treat reported findings as review guidance and confirm proposed revisions before applying them to story text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-review)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [quality-checklist.md](references/quality-checklist.md)
- [quality-rubric.md](references/quality-rubric.md)
- [anti-ai-writing.md](references/anti-ai-writing.md)
- [plot-core-methods.md](references/plot-core-methods.md)
- [character-relations.md](references/character-relations.md)
- [dialogue-mastery.md](references/dialogue-mastery.md)
- [tracking-transaction.md](references/tracking-transaction.md)
- [fanqie.md](references/rubrics/fanqie.md)
- [qidian.md](references/rubrics/qidian.md)
- [zhihu.md](references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance, configuration]

**Output Format:** [Markdown review reports with structured findings and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include requested/effective mode, fallback status, rubric source, findings, and recommendations; full and lean modes may also maintain tracking files.]

## Skill Version(s):

1.1.16 (source: server release evidence; artifact frontmatter says 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
