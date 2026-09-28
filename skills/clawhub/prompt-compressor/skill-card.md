## Description:

Compresses long prompts and context by selecting high-information sentences while retaining constraints, numbers, and code blocks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT-0 (ClawHub listing); bundled code: MIT; documentation and theory: all rights reserved

## Use Case:

Developers and other agent users use this skill to shorten prompts or long documents for an agent's context window while retaining important instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compression may leave out context needed for accurate decisions.

Mitigation: Compare compressed output with the original and review important instructions before reuse.

Risk: The skill declares broad tool access and may process sensitive local text.

Mitigation: Use only necessary tools and avoid sensitive files unless local processing and printed output are acceptable.

## Reference(s):

- [Prompt Compressor on ClawHub](https://clawhub.ai/zhaoxinghua09-cell/skills/prompt-compressor)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local CLI prints compressed text and preservation checks; shortening may omit useful context.]

## Skill Version(s):

1.0.2 (source: ClawHub release; bundled frontmatter says 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
