## Description:

Stellar Trails provides an always-on six-phase workflow supervisor for coding, document, planning, data processing, and visualization tasks, with traceability gates and structured delivery reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agent operators use this skill to keep agent work organized through explicit specification, planning, implementation, verification, and delivery phases. It is suited for normal ClawHub agent workflows where traceability, scope control, and review checkpoints are desired.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read a local GitHub PAT when present and change global git identity or stored credentials.

Mitigation: Use it only in a disposable or tightly scoped workspace, and avoid placing sensitive tokens in the workspace unless they are required for the task.

Risk: The skill contacts ClawHub and GitHub during workflow and update checks.

Mitigation: Review network expectations before installation and use a network-restricted environment when external calls are not acceptable.

Risk: The skill starts a localhost helper server and may kill python listeners on port 3000.

Mitigation: Avoid installing it alongside unrelated services on port 3000, or isolate it in a workspace where reclaiming that port will not disrupt other work.

Risk: The skill writes persistent logs and worklogs that may contain task context.

Mitigation: Use a workspace without unrelated sensitive material and review generated logs before sharing or archiving the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Publisher profile](https://clawhub.ai/user/hoshiyomix)
- [Skill definition](artifact/SKILL.md)
- [Workflow phases](artifact/procedure/phases.md)
- [Error resolution procedure](artifact/procedure/error-resolution.md)
- [Sandbox constraints](artifact/knowledge/zai-sandbox.md)
- [Code standards](artifact/constraints/code-standards.md)
- [Type safety constraints](artifact/constraints/type-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, structured phase reports, and file path references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May append local worklog entries and operate a localhost helper server as part of its workflow.]

## Skill Version(s):

9.14.1 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
