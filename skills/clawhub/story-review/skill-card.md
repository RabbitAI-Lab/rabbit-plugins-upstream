## Description:

Coordinates multi-perspective adversarial review of Chinese web-fiction drafts, using deployed reviewer agents when available and falling back to solo rubric-based review when agents or reference files are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, editors, and agent operators use this skill to review story chapters for plot structure, character behavior, prose quality, setting consistency, platform fit, and actionable revision findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read local manuscript, outline, rubric, and tracking files during review.

Mitigation: Use it only in story project workspaces where those files are appropriate for the agent to inspect.

Risk: Full and lean modes may update .story-review/state.md and tracking records.

Mitigation: Use solo mode for report-only review, or inspect generated state and tracking changes before relying on them.

## Reference(s):

- [Story Review ClawHub page](https://clawhub.ai/worldwonderer/skills/story-review)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [General Web-Fiction Review Rubric](references/quality-rubric.md)
- [Quality Checklist](references/quality-checklist.md)
- [Anti-AI-Writing Guide](references/anti-ai-writing.md)
- [Banned Words](references/banned-words.md)
- [Plot Core Methods](references/plot-core-methods.md)
- [Character Relations](references/character-relations.md)
- [Dialogue Mastery](references/dialogue-mastery.md)
- [Tracking State Protocol](references/tracking-transaction.md)
- [Fanqie Platform Rubric](references/rubrics/fanqie.md)
- [Qidian Platform Rubric](references/rubrics/qidian.md)
- [Zhihu Platform Rubric](references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown review reports with structured findings, optional shell command snippets, and local state or tracking files when the selected mode permits updates.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include requested and effective review modes, fallback status, rubric source, severity counts, evidence-backed findings, revision guidance, and inherited open items for batched reviews.]

## Skill Version(s):

1.1.18 (source: server release metadata; artifact frontmatter reports 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
