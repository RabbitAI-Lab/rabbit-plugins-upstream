## Description:

Reviews Chinese web-fiction drafts from multiple perspectives, using full, lean, or solo modes with fallback rubrics when reviewer agents or reference files are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors, editors, and writing-focused agents use this skill to identify structure, character, prose, continuity, and platform-fit issues in Chinese web-fiction drafts and receive actionable revision advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read manuscript, planning, and continuity files during review.

Mitigation: Run it only in projects where those files are intended for review, and avoid including unrelated private material in the review scope.

Risk: Full and lean modes may spawn configured reviewer agents, which can broaden the review path and produce additional findings.

Mitigation: Use `/story-review solo` when a single report-only pass is preferred or when reviewer-agent behavior has not been checked.

Risk: Full or lean workflows may update project continuity tracking files through the included tracking tool.

Mitigation: Review tracking changes after execution and use solo mode when no tracking-file maintenance should occur.

Risk: Automated prose and punctuation checks can flag functional stylistic choices as risks.

Mitigation: Treat script findings as review evidence and confirm each suggested edit against the story context before changing manuscript text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-review)
- [OpenClaw source metadata](https://github.com/worldwonderer/oh-story-claudecode)
- [Quality checklist](artifact/references/quality-checklist.md)
- [Quality rubric](artifact/references/quality-rubric.md)
- [Anti-AI-writing guide](artifact/references/anti-ai-writing.md)
- [Banned words and sentence patterns](artifact/references/banned-words.md)
- [Plot core methods](artifact/references/plot-core-methods.md)
- [Character relations](artifact/references/character-relations.md)
- [Dialogue mastery](artifact/references/dialogue-mastery.md)
- [Tracking transaction protocol](artifact/references/tracking-transaction.md)
- [Fanqie quality rubric](artifact/references/rubrics/fanqie.md)
- [Qidian quality rubric](artifact/references/rubrics/qidian.md)
- [Zhihu quality rubric](artifact/references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown review report with findings, mode metadata, rubric source, and actionable revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local check-script findings and, in full or lean mode, synthesized reviewer-agent findings; solo mode is report-only.]

## Skill Version(s):

1.1.17 (source: ClawHub release evidence; artifact frontmatter: 1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
