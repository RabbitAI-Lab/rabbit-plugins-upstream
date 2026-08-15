## Description:

当用户需要做小红书选题、小红书内容选题、小红书选题策划、爆款选题拆解、内容角度规划或选题素材整理时使用。面向内容运营、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operators, brand researchers, and creators use this skill to research Xiaohongshu topic ideas, review relevant public samples, and plan content angles from keyword-based searches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tokenized Xiaohongshu result URLs may be sensitive if forwarded, stored, or reused outside the analysis context.

Mitigation: Keep full result URLs only when needed for traceability, and avoid sharing them outside the immediate analysis unless the user accepts that exposure.

Risk: The skill runs an external npm CLI and uses SOCIALDATAX_API_KEY to fetch results.

Mitigation: Run it only in a trusted agent environment with the expected node, npm, and socialdatax-skills package configuration.

## Reference(s):

- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-topic-analysis-v2)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown text with optional shell command examples and structured analysis notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Xiaohongshu titles, authors or account names, content IDs, full result URLs, topic patterns, audience feedback, creator positioning, and suggested follow-up angles.]

## Skill Version(s):

0.1.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
