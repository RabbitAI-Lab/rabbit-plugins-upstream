## Description:

Reviews Chinese-language fiction from multiple perspectives, identifying plot, character, prose, and continuity issues with actionable revision suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Fiction authors and editors use this skill to review story chapters for narrative structure, character consistency, prose quality, and platform-specific expectations, then prioritize revisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The review reads story-project files that may contain unpublished material.

Mitigation: Run only in projects whose story files you intend to expose to the reviewing agent and any deployed reviewer agents.

Risk: Review workflows can write tracking, batch-review, or author-preference state under the project.

Mitigation: Review the memory and tracking behavior before use, and inspect scoped state changes after a review.

Risk: Automated findings and revision suggestions may misjudge authorial intent or continuity.

Mitigation: Check findings against the manuscript and story canon before making revisions.

## Reference(s):

- [Story Review on ClawHub](https://clawhub.ai/worldwonderer/skills/story-review)
- [Project link in skill metadata (not verified import provenance)](https://github.com/zenstory-ai/oh-story-claudecode)
- [Review quality rubric](references/quality-rubric.md)
- [Style resolution](references/style-resolution.md)
- [Review tracking](references/review-tracking.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Files]

**Output Format:** [Markdown review report with ranked findings and revision suggestions; optional project-scoped state files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports full, lean, and solo review; falls back to solo when reviewer agents are unavailable. Does not modify story manuscripts.]

## Skill Version(s):

1.1.26 (source: ClawHub release metadata; bundled frontmatter says 1.1.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
