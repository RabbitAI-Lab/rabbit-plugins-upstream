## Description:

Performs analogical reasoning and transfer by finding structure-preserving 1:1 mappings between source and target domains and migrating known source relations into traceable target inferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to compare structurally similar domains, reuse relationship patterns, and generate target-domain inferences from source-domain object and relation data. It is suited to cross-domain knowledge transfer, design-pattern reuse, teaching analogies, and fault-location analogies where the generated mapping and score need to be inspectable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled learner can persist usage history, errors, notes, and preferences in the skill directory.

Mitigation: Avoid recording sensitive prompts, personal information, or confidential operational details in learner notes or preferences; review stored learning data before sharing or publishing the skill directory.

Risk: The skill encourages future edits to skill files based on accumulated learning signals.

Mitigation: Require human review and normal code review before accepting any proposed skill-file changes, especially changes derived from usage history or error reflections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/analogical-reasoning)
- [ClawHub publisher profile](https://clawhub.ai/user/qq435912743)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown guidance with JSON results from local Python scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces object mappings, transferred relations, dangling relations, and transfer scores; the bundled learner may persist local usage notes and preferences.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
