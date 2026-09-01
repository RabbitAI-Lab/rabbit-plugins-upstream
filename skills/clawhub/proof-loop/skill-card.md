## Description:

Run evidence-gated coding sprints with frozen acceptance criteria, separated builder and verifier roles, and durable proof artifacts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leostehlik](https://clawhub.ai/user/leostehlik)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to run AI coding work through a repo-local proof loop that freezes acceptance criteria, records evidence, and requires a fresh verifier before completion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create or update repo-local task artifacts and run local verification commands.

Mitigation: Install it only in repositories where proof artifacts are desired, confirm the task id and repository root before initialization, and review verification commands before running them.

Risk: Optional guide installation or task-specific checks may write outside the expected proof artifact folder.

Mitigation: Use least-privilege execution, prefer dry runs when available, and require explicit review before commands modify files outside .agent/tasks/<TASK_ID>/.

## Reference(s):

- [Proof Loop ClawHub Page](https://clawhub.ai/leostehlik/skills/proof-loop)
- [Adoption Kit](docs/adoption-kit.md)
- [Workflow](references/workflow.md)
- [Artifact Schemas](references/artifacts.md)
- [Agent Brief Template](references/brief-template.md)
- [Loopsmith Bridge](references/loopsmith-bridge.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance, JSON proof artifacts, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates repo-local proof artifacts under .agent/tasks/<TASK_ID>/ and checks verifier verdicts.]

## Skill Version(s):

0.3.0 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
