## Description:

Content Matrix Factory helps generate and adapt social commerce content across Xiaohongshu, Douyin, WeChat Official Accounts, Weibo, and Zhihu, including drafts, platform-specific rewrites, calendars, trend-based angles, and operating guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, marketers, and social commerce operators use this skill to plan and generate batches of platform-adapted posts, product-promotion copy, short-video scripts, publishing schedules, and matrix-account strategy guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The self-learning helper can persist user preferences, operation history, notes, and error patterns in local learning files.

Mitigation: Avoid storing sensitive data in notes or preferences, review learned_patterns.json periodically, and remove or disable the learning file when persistence is not desired.

Risk: The learning helper can write learning files for other skill directories when invoked with those paths.

Mitigation: Run learner.py only with an intended skill directory and review the target path before recording or updating preferences.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/content-matrix-factory)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with content drafts, strategy tables, scheduling guidance, and optional shell commands for the learning helper.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May maintain local usage patterns and preferences in learned_patterns.json when the bundled learner script is used.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
