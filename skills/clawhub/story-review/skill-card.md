## Description:

Coordinates adversarial, multi-perspective review of Chinese web-fiction drafts, with full, lean, and solo modes plus rubric fallbacks when reviewer agents or reference files are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and editors use this skill to find structural, character, prose, continuity, platform-fit, and AI-style issues in web-fiction drafts and receive actionable revision guidance. It supports direct solo review and coordinated multi-agent review when the required reviewer agents are deployed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist author memory and mutate project tracking files during review without a clear separate opt-in.

Mitigation: Install it only when a stateful story-review workflow is wanted; use solo mode or request no persistence for comment-only review, and inspect changes under .story/, .story-review/, and 追踪/ after full or lean runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-review)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Review quality checklist](references/review-quality.md)
- [Generic web-fiction quality rubric](references/quality-rubric.md)
- [Anti-AI-writing guide](references/anti-ai-writing.md)
- [Plot core methods](references/plot-core-methods.md)
- [Character relationships guide](references/character-relations.md)
- [Dialogue design guide](references/dialogue-mastery.md)
- [AI-style banned words and sentence patterns](references/banned-words.md)
- [Author memory protocol](references/author-memory.md)
- [Tracking state protocol](references/tracking-transaction.md)
- [Fanqie rubric](references/rubrics/fanqie.md)
- [Qidian rubric](references/rubrics/qidian.md)
- [Zhihu Yanxuan rubric](references/rubrics/zhihu.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance, Files]

**Output Format:** [Markdown review report with structured findings, mode metadata, rubric source, and actionable revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May run local precheck scripts and may maintain review, author-memory, or tracking state files when the selected workflow requires persistence.]

## Skill Version(s):

1.1.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
