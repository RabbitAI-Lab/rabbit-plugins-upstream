## Description:

詹明明·今天拍什么 helps an agent advise a solo knowledge-video creator on short-video topic selection by testing supply and demand, benchmark signals, real data support, and content mix before proposing or diagnosing topics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and content operators use this skill to evaluate and shape short-video topic ideas, compare evidence, identify topic tension, and choose next actions without fabricating data or replacing user judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read private vault materials when those paths are available.

Mitigation: Install it only in workspaces where that access is intended, and restrict filesystem access to the paths needed for topic-advice sessions.

Risk: The skill can write feedback into shared framework, pipeline, and memory files.

Mitigation: Require explicit confirmation before writeback or memory updates, and review saved changes after sessions.

Risk: Topic advice may be unsupported when benchmark, personal, or pipeline data is missing.

Mitigation: Label unsupported conclusions as inference and require real user or benchmark evidence before acting on recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-topic)
- [常识缺口法](references/常识缺口法.md)
- [议程与合集](references/议程与合集.md)
- [选题三路](references/选题三路.md)
- [题感引擎](references/题感引擎.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Conversational text or Markdown with structured bullets, numbered options, and occasional shell commands or saved-file paths.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write topic pipeline or memory files when the host environment provides the referenced vault paths; user review is recommended for any saved feedback.]

## Skill Version(s):

0.2.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
