## Description:

Helps agents generate and evaluate multi-platform Chinese titles and cover text by selecting content-fit structures, checking title red lines, and explaining the rationale for each candidate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to draft, compare, and refine platform-specific titles and short cover text for Douyin, Xiaohongshu, WeChat Channels, and public-account content. The skill is aimed at solo knowledge creators who need title candidates with structure labels, fit rationale, and red-line checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may persist user feedback into local writing-memory or framework files without a clear confirmation step.

Mitigation: Require explicit user approval before any persistent write, and restrict updates to the intended skill-memory path.

Risk: The skill's sample output format includes an 原始爆款 field that could encourage reuse of third-party title examples.

Mitigation: Remove that field or replace it with a source-neutral structure note before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-title)
- [Publisher profile](https://clawhub.ai/user/iamzifei)
- [标题结构库](references/标题结构库.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown text with title candidates, structure labels, rationale, red-line checks, and ranked recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform-specific short cover-text variants and feedback-memory update guidance.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
