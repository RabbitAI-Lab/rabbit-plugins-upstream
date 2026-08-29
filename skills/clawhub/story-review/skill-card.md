## Description:

Multi-perspective adversarial review for Chinese web-fiction drafts, with full, lean, and solo modes, fallback rubrics, and triggers such as /story-review and /审查.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and agent users use this skill to find structural, character, prose, continuity, and platform-fit problems in Chinese web-fiction drafts and receive actionable revision findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read project writing context and may persist author preferences or review state during some workflows.

Mitigation: Use explicit solo or read-only review when only comments are needed, and review workspace diffs after full or lean runs.

Risk: Full and lean modes can coordinate additional reviewer agents, expanding the amount of draft and project context processed during review.

Mitigation: Run the skill only in the intended writing workspace and provide the smallest practical review scope.

Risk: Story tracking files may be updated during supported review workflows.

Mitigation: Keep tracking changes limited to the documented transaction flow and inspect generated tracking changes before relying on them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-review)
- [Story review skill definition](artifact/SKILL.md)
- [General web-fiction quality rubric](artifact/references/quality-rubric.md)
- [Review quality checklist](artifact/references/review-quality.md)
- [Anti-AI writing guide](artifact/references/anti-ai-writing.md)
- [Banned AI-flavor words and patterns](artifact/references/banned-words.md)
- [Plot core methods](artifact/references/plot-core-methods.md)
- [Character relationships guide](artifact/references/character-relations.md)
- [Dialogue design guide](artifact/references/dialogue-mastery.md)
- [Author memory protocol](artifact/references/author-memory.md)
- [Tracking state protocol](artifact/references/tracking-transaction.md)
- [Fanqie quality rubric](artifact/references/rubrics/fanqie.md)
- [Qidian quality rubric](artifact/references/rubrics/qidian.md)
- [Zhihu YanYan quality rubric](artifact/references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown review report with structured findings, mode metadata, optional shell command output, and guidance for revisions or state updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include severity-labeled findings, reviewer verdicts, fallback notices, and receipts for explicitly requested author-memory updates.]

## Skill Version(s):

1.1.20 (source: server release metadata; artifact frontmatter lists 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
