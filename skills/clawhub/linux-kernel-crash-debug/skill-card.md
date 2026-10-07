## Description:

Guides evidence-first analysis of Linux kernel crashes and vmcores using the crash utility and memory and concurrency debugging tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crazyss](https://clawhub.ai/user/crazyss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Linux engineers use this skill to triage kernel panics and diagnose likely causes of crashes, deadlocks, and memory faults from vmcores and related evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Vmcores and diagnostic output can contain sensitive process memory and credentials.

Mitigation: Keep dumps and outputs access-controlled; use offline files under an unprivileged account and obtain approval before sharing or uploading them.

Risk: Live tracing, system configuration changes, or crash tests can disrupt a host.

Mitigation: Require explicit authorization for the specific host and action before privileged installs, live tracing, debugfs or procfs writes, service or boot changes, or kdump tests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crazyss/skills/linux-kernel-crash-debug)
- [Project homepage (release metadata)](https://github.com/crazyss/linux-kernel-crash-debug)
- [Crash Utility documentation](https://crash-utility.github.io/)
- [Evidence-first workflow](artifact/references/evidence-first-workflow.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Evidence-backed conclusions with confidence levels and disproof checks.]

## Skill Version(s):

1.4.4 (source: skill frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
