## Description:

Diagnose and repair Hermes promise-only action stalls, repeated failures, and polluted sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ambitioncn](https://clawhub.ai/user/ambitioncn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to diagnose Hermes action loops and apply a bounded guard for promise-only stalls, repeated tool failures, and polluted sessions. It guides status checks, compatibility testing, dry-run installation, verification, and rollback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer makes persistent changes to a Hermes installation and can change future agent behavior.

Mitigation: Run status, test-compat, and install --dry-run first; install only on the intended Hermes instance and keep the generated backup protected.

Risk: The rollback manifest path is unsafe and can execute shell code.

Mitigation: Avoid rollback with any backup path that was not just created and verified, and fix manifest parsing before use in sensitive or shared environments.

Risk: Unsupported or ambiguous Hermes layouts can be patched incorrectly.

Mitigation: Treat compatibility failures as stop conditions and do not patch unknown Hermes versions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ambitioncn/skills/hermes-action-loop-guard)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces operational guidance for status checks, compatibility tests, dry-run installation, verification, and rollback.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
