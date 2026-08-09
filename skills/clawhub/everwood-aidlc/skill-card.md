## Description:

Strict human-gated AIDLC planning for non-trivial software work, with per-gate deconfliction review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mlwood-dev](https://clawhub.ai/user/mlwood-dev)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to run a structured, human-approved planning workflow before non-trivial OpenClaw software work. It helps capture context, assess complexity, decompose work, record design decisions, and produce an execution plan before construction begins.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Planning artifacts can contain sensitive project details if users paste secrets or credentials into gate notes.

Mitigation: Avoid placing secrets, credentials, tokens, or sensitive customer data in AIDLC gate artifacts.

Risk: Activating the workflow creates local aidlc-sessions files in the workspace.

Mitigation: Tell users about the local write behavior at session start and review or remove planning artifacts according to the workspace's retention needs.

Risk: Reviewer subagents may influence planning quality but do not replace human approval.

Mitigation: Keep reviewer subagents read-only and require explicit human approval before each gate advances.

## Reference(s):

- [AIDLC Core Workflow](references/core-workflow.md)
- [ClawHub Skill Page](https://clawhub.ai/mlwood-dev/skills/everwood-aidlc)
- [OpenClaw AIDLC Homepage](https://github.com/Everwood-Technologies/openclaw-aidlc)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and local Markdown/JSON planning artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates local aidlc-sessions planning files in the active workspace when activated.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
