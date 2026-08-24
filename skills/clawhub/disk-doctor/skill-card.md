## Description:

Diagnose and safely reclaim disk space on an OpenClaw host

This skill is ready for commercial/non-commercial use.

## Publisher:

[breakzoras](https://clawhub.ai/user/breakzoras)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators maintaining OpenClaw hosts use this skill to diagnose root filesystem usage, review running processes, and identify safe cache cleanup steps before deleting anything.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cache cleanup or pruning commands can remove data the host may still rely on, especially Docker images or containers.

Mitigation: Review command output before deletion, confirm Docker is present and unused before pruning, and follow the skill's instruction to leave workspaces, OpenClaw credentials, and unexplained paths alone.

Risk: Running cleanup while package installation, builds, or other high-load work is active can interrupt or fail that work.

Mitigation: Check uptime and active processes first, and wait when npm, apt, pip, builds, or high load are visible.

Risk: Disk usage guidance can be misleading if deletion starts from guesses rather than measured filesystem data.

Mitigation: Measure with df, du, and large-file discovery commands before recommending cleanup, then report findings to the user before optional removals.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
