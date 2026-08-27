## Description:

多视角对抗式审查。full/lean 模式在已部署 reviewer agents 时并行 spawn；缺失/异常 agents 或 spawn 失败时自动降级 solo，参考文件不可读时使用内置 rubric fallback。触发方式：/story-review、/审查、「审查一下」「帮我审一下」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and writing teams use this skill to review Chinese web-fiction drafts for structure, character behavior, prose quality, continuity, platform fit, and actionable revisions. It can coordinate deployed reviewer agents when available, fall back to solo review, run local read-only checkers, and maintain review or tracking state when the documented workflow calls for it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads manuscript, outline, settings, and tracking files as part of story review.

Mitigation: Install it only in story projects where that file access is expected and appropriate.

Risk: The workflow may run local checker scripts, spawn deployed reviewer agents, and maintain review, tracking, or author-preference state.

Mitigation: Use explicit /story-review commands when possible and review generated state changes before relying on them.

Risk: Bundled market-writing references may not match every project's intended audience or platform.

Mitigation: Set audience, platform, and rubric assumptions explicitly when the defaults do not match the project.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-review)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Quality checklist](references/quality-checklist.md)
- [Quality rubric](references/quality-rubric.md)
- [Anti-AI writing guide](references/anti-ai-writing.md)
- [Banned words and sentence patterns](references/banned-words.md)
- [Plot core methods](references/plot-core-methods.md)
- [Character relations guide](references/character-relations.md)
- [Dialogue mastery guide](references/dialogue-mastery.md)
- [Author memory protocol](references/author-memory.md)
- [Tracking transaction protocol](references/tracking-transaction.md)
- [Fanqie rubric](references/rubrics/fanqie.md)
- [Qidian rubric](references/rubrics/qidian.md)
- [Zhihu rubric](references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown review reports with structured findings, verdict summaries, mode metadata, and actionable revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include review-state or tracking-state updates when the workflow and project context require them.]

## Skill Version(s):

1.1.19 (source: server release metadata; artifact frontmatter reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
