## Description: <br>
多视角对抗式审查。full/lean 模式在已部署 reviewer agents 时并行 spawn；缺失/异常 agents 或 spawn 失败时自动降级 solo，参考文件不可读时使用内置 rubric fallback。触发方式：/story-review、/审查、「审查一下」「帮我审一下」。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and story-development agents use this skill to review fiction drafts for structure, character behavior, prose quality, platform fit, continuity, and actionable revision priorities. It can coordinate local reviewer agents in full or lean mode, or fall back to solo review when those agents are unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The review workflow may update a project foreshadowing tracker for newly discovered open hooks, even though most review behavior is report-only. <br>
Mitigation: Use version control or request a read-only review when tracker changes are not desired, and review any proposed tracker edits before accepting them. <br>
Risk: Full and lean modes may spawn already-deployed local reviewer agents, which can change behavior depending on the local project setup. <br>
Mitigation: Use solo mode for a single-agent review path, or verify deployed reviewer agents and check the report's Requested Mode, Effective Mode, and Fallback fields. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-review) <br>
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Quality Checklist](artifact/references/quality-checklist.md) <br>
- [Quality Rubric](artifact/references/quality-rubric.md) <br>
- [Anti-AI Writing Guide](artifact/references/anti-ai-writing.md) <br>
- [Banned Words and Sentence Patterns](artifact/references/banned-words.md) <br>
- [Plot Core Methods](artifact/references/plot-core-methods.md) <br>
- [Character Relations](artifact/references/character-relations.md) <br>
- [Dialogue Mastery](artifact/references/dialogue-mastery.md) <br>
- [Fanqie Quality Rubric](artifact/references/rubrics/fanqie.md) <br>
- [Qidian Quality Rubric](artifact/references/rubrics/qidian.md) <br>
- [Zhihu Yanxuan Quality Rubric](artifact/references/rubrics/zhihu.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown story review report with structured S1-S4 findings, mode metadata, evidence, and revision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include deterministic precheck findings from local scripts and may identify tracker updates for open foreshadowing items.] <br>

## Skill Version(s): <br>
1.1.14 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
