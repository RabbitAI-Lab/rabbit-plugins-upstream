## Description:

Safely run shell commands on Termux/Android by detecting platform, verifying tools, applying timeouts and retries, and avoiding Linux desktop assumptions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill when running shell commands in Termux/Android so they can detect platform constraints, check tool availability, apply timeouts and retries, and avoid desktop Linux assumptions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposed shell command may install packages, access storage, use the network, or delete files in ways the user did not intend.

Mitigation: Review the command text before execution, confirm risky targets explicitly, and use the dry-run helper only as a pre-check rather than as a sandbox.

Risk: Termux differs from desktop Linux, so desktop-specific commands or paths may fail or produce misleading results.

Mitigation: Detect the platform first, verify required tools with Termux-aware checks, and choose Android-compatible fallbacks before running commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/termux-compat-runner)
- [README](artifact/README.md)
- [Skill source](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline shell commands and structured command-result fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The included helper script is dry-run only and prints whether a reviewed command would be allowed or denied.]

## Skill Version(s):

1.0.0 (source: server release metadata and artifact/_meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
