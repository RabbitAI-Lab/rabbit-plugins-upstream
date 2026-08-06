## Description:

Story Review coordinates adversarial fiction review across full, lean, and solo modes, using deployed reviewer agents when available and falling back to solo review with embedded rubrics when agents or reference files are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and fiction authors use this skill to review Chinese web-fiction drafts for story structure, character consistency, prose naturalness, platform fit, factual continuity, and actionable revision priorities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads story project files to assemble review evidence.

Mitigation: Install and invoke it only in workspaces where project-file review is intended.

Risk: The skill can run local Node and Python checks against selected story files.

Mitigation: Review local script behavior and outputs before using findings as edit guidance.

Risk: Full and lean modes may update files under the project's tracking directory.

Mitigation: Use solo mode for report-only review, and review the tracking workflow before using full or lean mode on manually managed tracking state.

## Reference(s):

- [OpenClaw source](https://github.com/worldwonderer/oh-story-claudecode)
- [Quality Checklist](references/quality-checklist.md)
- [Generic Web-Fiction Review Rubric](references/quality-rubric.md)
- [Anti-AI Writing Guide](references/anti-ai-writing.md)
- [Banned Words and Sentence Patterns](references/banned-words.md)
- [Plot Core Methods](references/plot-core-methods.md)
- [Character Relations Guide](references/character-relations.md)
- [Dialogue Mastery Guide](references/dialogue-mastery.md)
- [Tracking Transaction Protocol](references/tracking-transaction.md)
- [Fanqie Quality Rubric](references/rubrics/fanqie.md)
- [Qidian Quality Rubric](references/rubrics/qidian.md)
- [Zhihu Yanyan Quality Rubric](references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown review report with structured findings, optional local check command output, and optional JSON tracking transaction guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include requested mode, effective mode, fallback reason, rubric, rubric source, S1-S4 severity findings, evidence, issues, fixes, and prioritized recommendations.]

## Skill Version(s):

1.1.15 (source: server release metadata; artifact frontmatter reports 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
