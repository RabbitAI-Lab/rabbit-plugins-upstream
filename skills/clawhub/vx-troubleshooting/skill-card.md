## Description:

Guides developers through diagnosing and resolving vx installation, version, PATH, runtime, and configuration issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[loonghao](https://clawhub.ai/user/loonghao)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to troubleshoot vx installation failures, version conflicts, PATH resolution, runtime errors, and configuration problems. It provides diagnostic commands and recovery guidance for local environments and CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live remote installation scripts can execute unreviewed code.

Mitigation: Require explicit approval; download and verify install scripts before running them.

Risk: Reset, elevated-privilege, and shim-repair commands can remove user state or overwrite local executables.

Mitigation: Back up vx state, inspect shim destinations and ownership, and obtain approval before deleting ~/.vx, using sudo, or rewriting shims.

Risk: Issue-tracker actions can disclose diagnostics or make changes beyond troubleshooting.

Mitigation: Review diagnostic content and require explicit approval before posting to issue trackers.

## Reference(s):

- [vx managed command shim guide](https://github.com/vx-org/vx/blob/main/docs/guide/managed-command-shims.md)
- [vx documentation](https://github.com/vx-org/vx#readme)

## Skill Output:

**Output Type(s):** [Troubleshooting guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the reported error and operating system.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
