## Description:

Troubleshooting guide for vx issues. Use when encountering installation failures, version conflicts, PATH issues, or other vx problems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to diagnose and resolve vx installation, version, PATH, configuration, and runtime problems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A complete reset can delete local vx state and configuration.

Mitigation: Try vx doctor --fix and cache repair first; back up and inspect ~/.vx before deleting it.

Risk: Installer commands can run unverified remote scripts.

Mitigation: Download and verify installer scripts before running them; do not pipe remote content directly to a shell.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/loonghao/skills/vx-troubleshooting)
- [vx documentation](https://github.com/loonghao/vx#readme)
- [vx issue tracker](https://github.com/loonghao/vx/issues)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Symptom-based troubleshooting and diagnostic steps]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
