## Description:

多视角对抗式审查。full/lean 模式在已部署 reviewer agents 时并行 spawn；缺失/异常 agents 或 spawn 失败时自动降级 solo，参考文件不可读时使用内置 rubric fallback。触发方式：/story-review、/审查、「审查一下」「帮我审一下」。

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External authors and writing teams use this skill to review Chinese web-fiction drafts for structure, character consistency, prose quality, platform fit, factual continuity, and actionable revision priorities. It can coordinate multiple reviewer agents when available or fall back to solo review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review workflow can create or update local project state, including review state, author memory, and story tracking files.

Mitigation: Prefer /story-review solo for read-only-style review when state changes are not desired, and inspect .story-review/, .story/作者记忆/, and 追踪/ before committing.

Risk: Review findings and detector outputs may be incorrect, style-dependent, or too broad for a specific manuscript.

Mitigation: Treat all findings as review proposals and require human review before applying edits or accepting tracking changes.

## Reference(s):

- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [审稿质量检查清单](artifact/references/review-quality.md)
- [通用网文内容审查 Rubric](artifact/references/quality-rubric.md)
- [去AI味完整指南](artifact/references/anti-ai-writing.md)
- [剧情核心方法](artifact/references/plot-core-methods.md)
- [角色关系与感情线操作手册](artifact/references/character-relations.md)
- [对话设计操作手册](artifact/references/dialogue-mastery.md)
- [作者记忆协议](artifact/references/author-memory.md)
- [追踪状态协议](artifact/references/tracking-transaction.md)
- [番茄小说 Quality Rubric](artifact/references/rubrics/fanqie.md)
- [起点中文网 Quality Rubric](artifact/references/rubrics/qidian.md)
- [知乎盐言故事 Quality Rubric](artifact/references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown review reports with structured findings, verdict summaries, and optional shell commands for local checks or tracking transactions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports use severity-ranked findings and may include fallback-mode metadata, rubric source metadata, inherited review items, and concrete revision guidance.]

## Skill Version(s):

1.1.22 (source: server release metadata; artifact frontmatter states 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
