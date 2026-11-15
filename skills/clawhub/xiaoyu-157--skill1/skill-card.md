## Description:

Helps an agent learn from corrections, self-reflection, and repeated patterns by maintaining local tiered memory and applying it in future work.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaoyu-157](https://clawhub.ai/user/xiaoyu-157)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to help an agent record explicit corrections, reflect on completed work, organize reusable lessons, and apply confirmed preferences across future sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores user-derived corrections and preferences persistently in local files.

Mitigation: Install only when persistent local storage is acceptable, and avoid storing credentials, health data, or third-party personal information.

Risk: The skill may modify workspace steering files with incomplete or conflicting scope disclosure.

Mitigation: Review proposed writes to ~/self-improving/ and approve exact diffs before changing AGENTS.md, SOUL.md, or HEARTBEAT.md.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xiaoyu-157/skills/skill1)
- [Server-resolved GitHub source](https://github.com/xiaoyu-157/test-import-skill-4/tree/main/skill1)
- [Skill homepage](https://clawic.com/skills/self-improving)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with file paths and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose local memory and workspace steering file updates that should be reviewed before applying.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
