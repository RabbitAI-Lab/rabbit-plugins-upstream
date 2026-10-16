## Description:

Guides evidence-first Linux kernel crash debugging with vmcore analysis, the crash utility, and memory and concurrency diagnostics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crazyss](https://clawhub.ai/user/crazyss)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Linux systems engineers use this skill to investigate kernel panics, hangs, memory faults, and deadlocks using crash dumps and corroborating evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kernel dumps and trace output may expose credentials and process memory.

Mitigation: Restrict access to dumps and output; do not upload or share them without approval and sanitization.

Risk: Privileged host changes or deliberate crash tests can disrupt a live system.

Mitigation: Default to offline, read-only analysis; require approval of the exact host, action, maintenance context, and rollback plan before host changes, and leave crash triggers to an authorized human.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crazyss/skills/linux-kernel-crash-debug)
- [Project homepage](https://github.com/crazyss/linux-kernel-crash-debug)
- [Crash utility documentation](https://crash-utility.github.io/help_pages/)
- [Evidence-first workflow](references/evidence-first-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings should state evidence quality, confidence, competing explanations, and follow-up checks.]

## Skill Version(s):

1.4.5 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
