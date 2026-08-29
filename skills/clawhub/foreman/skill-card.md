## Description:

Foreman helps agents dispatch coding work to background workers, intake delivered changes against path and test-boundary rules, and run an acceptance protocol before merge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoba-dev](https://clawhub.ai/user/xiaoba-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering leads use Foreman to delegate implementation tasks to worker agents, check deliveries against explicit work orders and allowed paths, and accept integrated changes through repeatable verification gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository content may be sent to the worker backend configured by the user.

Mitigation: Install only for repositories whose contents may be processed by the configured backend, and use the documented local or hosted backend options for sensitive repositories.

Risk: The optional caged worker exposes DEEPSEEK_API_KEY to the container process.

Mitigation: Use a scoped worker credential, prefer a pinned worker image and CLI version, and rely on the documented container boundary so the key is not written to disk or copied into the mounted worktree.

Risk: Foreman writes task and batch state under .foreman/ inside the repository.

Mitigation: Confirm .foreman/ is gitignored before dispatching tasks so local coordination state is not accidentally committed.

Risk: Verification commands are supplied by the work order and may have side effects.

Mitigation: Review work orders before dispatch, use side-effect-free preflight commands for worker self-checks and intake, and reserve side-effecting commands for final CI when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoba-dev/skills/foreman)
- [Foreman skill definition](artifact/SKILL.md)
- [Dispatch workflow](artifact/dispatch.md)
- [Acceptance workflow](artifact/verify.md)
- [Work order template](artifact/work-order.md)
- [CI gate template](artifact/ci-gate.yml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash commands, JSON state examples, and YAML CI configuration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes work-order templates, local state-file conventions, delivery intake checks, and optional container-backed worker commands.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
