## Description:

Adds structured JSON logging, error classification, jittered retries, circuit breaking, performance profiling, state capture, and auto-healing to Python and Bash skills or scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add observability, recovery controls, diagnostics, and reproduce-diagnose-fix-verify workflows to ClawHub skills, agents, and local scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The framework exposes powerful local command, install, process, network, and file-write behaviors.

Mitigation: Use least privilege, review the exact workflow before execution, and enable DEBUG_FRAMEWORK_ALLOW_DESTRUCTIVE only in reviewed environments for reviewed actions.

Risk: Shell helpers accept command strings and can run unintended commands if given untrusted input.

Mitigation: Pass only trusted command strings to shell helpers such as dbg_retry and dbg_with_timeout.

Risk: Logs and state captures may contain data processed by the enhanced skill, including sensitive values.

Mitigation: Protect or redirect log and capture locations, and review generated files before sharing them.

Risk: Auto-heal dependency installation can install packages based on parsed error messages when destructive mode is enabled.

Mitigation: Avoid auto-heal dependency installation for untrusted errors and confirm package names before enabling the install path.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/debug-enhancement-framework)
- [Skill definition and operational rules](artifact/SKILL.md)
- [README, security notes, and artifact hash](artifact/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python and Bash examples; helper CLIs emit JSON on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include local logs, state captures, diagnostics, performance reports, and dry-run cleanup reports.]

## Skill Version(s):

2.1.4 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
