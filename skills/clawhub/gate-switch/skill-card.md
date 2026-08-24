## Description:

gate-switch helps agents turn delivery claims into mechanical JSON checks and run a Python gate engine that returns pass, block, clarify, or violation verdicts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xu-jin-cs](https://clawhub.ai/user/xu-jin-cs)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to define verifiable checks for claimed work such as files written, patterns removed, JSON fields set, or scripts passing. It is useful when an agent workflow needs a mechanical gate before accepting completion claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Specs can use script_exit checks that execute arbitrary shell commands.

Mitigation: Review every spec before use and remove or tightly allowlist command execution for specs from untrusted prompts or third-party sources.

Risk: Gate logs may record sensitive paths, bindings, or violation details.

Mitigation: Use project-local logging, disable logging where appropriate, and avoid passing secrets or sensitive paths as bindings.

## Reference(s):

- [gate-switch ClawHub skill page](https://clawhub.ai/xu-jin-cs/skills/gate-switch)
- [CLAIM_GATE_TEMPLATE.md](artifact/templates/CLAIM_GATE_TEMPLATE.md)
- [L3_FRAMEWORK_TEMPLATE.md](artifact/templates/L3_FRAMEWORK_TEMPLATE.md)
- [zero_residual bundled spec](artifact/scripts/specs/zero_residual.json)
- [no_abs_path bundled spec](artifact/scripts/specs/no_abs_path.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON specifications and shell commands; the gate engine emits JSON verdicts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pure Python standard-library tool; executions can append JSONL audit records when logging is enabled.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
