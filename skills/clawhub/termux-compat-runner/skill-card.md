## Description:

Use when executing shell commands on Termux/Android: validate platform, choose safe commands, apply timeout/retry, and avoid Linux desktop assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to prepare and review Termux/Android shell-command workflows, including platform detection, tool checks, timeout/retry choices, and fallback planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat a dry-run ALLOWED result as authorization to execute a shell command without review.

Mitigation: Review every command manually before execution, especially package installs, apt/dpkg operations, curl, python, git pull, and storage-access commands.

Risk: Termux and Android shell environments can differ from Linux desktop environments, causing commands or paths to fail.

Mitigation: Detect platform, architecture, runtime, and tool availability before choosing a command strategy.

Risk: Destructive or storage-affecting commands can damage files if executed without explicit target validation.

Mitigation: Confirm risky targets before execution, avoid unreviewed scripts, use timeout/retry limits, and verify command output before reporting success.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/termux-compat-runner)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands and structured command-result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes platform, exit-code, result, output, and next-action reporting guidance; bundled helper script performs dry-run validation only.]

## Skill Version(s):

1.0.1 (source: server release metadata and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
