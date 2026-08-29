## Description:

Requirements-Driven Development helps agents converge fuzzy requirements into specifications before coding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[anyjohn](https://clawhub.ai/user/anyjohn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to refine raw requirements into traceable stories, specifications, acceptance criteria, implementation work, and verification evidence before code is written.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated planning and specification artifacts may add local files that are inappropriate for small changes or should not be committed.

Mitigation: Review generated .rdd artifacts before committing or sharing, and use the Lite or Solo-dev path for small, low-risk changes.

Risk: The artifact is primarily written in Chinese, which may lead to misunderstood requirements for non-Chinese users.

Mitigation: Ask the agent to work in the user's preferred language before relying on generated requirements, specifications, or decisions.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/anyJohn/OpenReq/tree/main/skills/rdd)
- [RDD Design](artifact/references/rdd-design.md)
- [RDD File Templates](artifact/references/templates.md)
- [ClawHub skill page](https://clawhub.ai/anyjohn/skills/rdd)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with structured work-item and specification examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local planning and specification artifacts such as .rdd/items for larger tasks; small solo changes may use commit messages instead.]

## Skill Version(s):

0.1.0 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
