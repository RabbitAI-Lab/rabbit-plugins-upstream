## Description:

Guides developers in running and troubleshooting headless coding agents through the acpx CLI, including persistent sessions and queued follow-ups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tenequm](https://clawhub.ai/user/tenequm)

### License/Terms of Use:

Apache 2.0

## Use Case:

Developers and engineers use this skill to launch coding agents with acpx, manage persistent sessions, and diagnose failed or incomplete turns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Launched coding agents may modify files in the selected working directory.

Mitigation: Use a narrow, disposable, or reviewed worktree and approve the selected provider before using sensitive repositories.

Risk: Persistent sessions can remain open, and a completed turn may not mean the requested work succeeded.

Mitigation: Check the full result and any expected output files, then close or prune sessions when work is done.

## Reference(s):

- [acpx project](https://github.com/openclaw/acpx)
- [Skill homepage listed in metadata](https://github.com/tenequm/skills/tree/main/skills/acpx-faq)
- [ClawHub skill release](https://clawhub.ai/tenequm/skills/acpx-faq)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Session-management and troubleshooting guidance.]

## Skill Version(s):

0.8.0 (source: frontmatter and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
