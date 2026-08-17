## Description:

A distilled meta-skill for formal capability contract tasks that adds self-verification, reflection, and local learning notes around agent outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent builders use this skill to guide formal capability contract work with precondition, postcondition, invariant, self-verification, and reflection steps. It is suited for agents that need more traceable reasoning around contract-style tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The learner helper can persist invocation or failure notes locally if it is run, including sensitive text if that text is passed as a note.

Mitigation: Keep use user-directed, avoid passing secrets or personal data to learner notes, and review local learned state before sharing artifacts.

Risk: The skill text advertises inherited formal-contract and super-agent capabilities that may not exist unless separately provided.

Mitigation: Confirm required helper skills, scripts, and workflow hooks are available before relying on those capabilities for production work.

## Reference(s):

- [Skill definition](artifact/SKILL.md)
- [Distillation report](artifact/distillation_report.md)
- [ClawHub skill page](https://clawhub.ai/qq435912743/skills/meta-formal-capability-contract)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown or plain text, with code and shell snippets when relevant.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include verification and reflection notes; the learner helper can persist simple local learning state if run.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
