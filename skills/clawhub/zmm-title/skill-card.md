## Description:

Generates platform-specific Chinese social-media titles and cover text by matching the content shape to a 12-structure title taxonomy, checking red lines, and explaining why each candidate fits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and publishing assistants use this skill to draft and refine titles, short cover text, and title-selection rationale for platforms such as Douyin, Xiaohongshu, WeChat Channels, and public-account posts. It is intended for content-facing workflows where candidates must fit the source material, stay within stated platform constraints, and avoid the skill's documented red-line patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to read shared vault or framework files.

Mitigation: Use explicit invocation and narrow vault permissions so the agent only reads files needed for the active title-writing task.

Risk: The skill may persist title feedback for future use without explicit approval.

Mitigation: Require confirmation before memory or framework writeback, especially when feedback contains user preferences or private campaign details.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-title)
- [标题结构库](references/标题结构库.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown with structured title candidates, rationale, red-line checks, and short cover-text options when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a recommendation about whether the source opening should change when invoked by another writing skill.]

## Skill Version(s):

0.2.5 (source: server release evidence; artifact frontmatter states 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
