## Description: <br>
Coordinates multi-perspective adversarial review of fiction text, using full, lean, or solo review modes with fallback behavior when reviewer agents or reference files are unavailable. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[worldwonderer](https://clawhub.ai/user/worldwonderer) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Writers and agent users use this skill to review fiction drafts for structure, character, prose, continuity, platform fit, and actionable revision findings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can persist review discoveries into project tracking files without a separate confirmation step. <br>
Mitigation: Review proposed tracking-file changes before relying on them, and require an explicit confirmation or diff when using this skill in a shared project. <br>
Risk: The skill may read local story project materials and use reviewer subagents when available. <br>
Mitigation: Install and run it only in projects where that local access and subagent use are acceptable, and prefer explicit /story-review commands over broad natural-language triggers. <br>


## Reference(s): <br>
- [Story Review skill page](https://clawhub.ai/worldwonderer/skills/story-review) <br>
- [OpenClaw metadata source](https://github.com/worldwonderer/oh-story-claudecode) <br>
- [Quality Checklist](references/quality-checklist.md) <br>
- [Quality Rubric](references/quality-rubric.md) <br>
- [Anti-AI Writing Guide](references/anti-ai-writing.md) <br>
- [Banned Words and Patterns](references/banned-words.md) <br>
- [Plot Core Methods](references/plot-core-methods.md) <br>
- [Character Relations](references/character-relations.md) <br>
- [Dialogue Mastery](references/dialogue-mastery.md) <br>
- [Fanqie Quality Rubric](references/rubrics/fanqie.md) <br>
- [Qidian Quality Rubric](references/rubrics/qidian.md) <br>
- [Zhihu Quality Rubric](references/rubrics/zhihu.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown review report with structured findings and actionable revision guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports requested mode, effective mode, fallback status, rubric, rubric source, severity, category, location, evidence, issue, and fix fields.] <br>

## Skill Version(s): <br>
1.1.13 (source: server release evidence; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
