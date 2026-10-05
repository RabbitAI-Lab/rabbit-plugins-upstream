## Description:

Tracks multi-step work, records progress, and guides cleanup and resumption of unfinished tasks across supported agent environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users track multi-step tasks, preserve progress across sessions, and review remaining work before continuing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enforcement hooks can block edits or writes until work is registered.

Mitigation: Review or disable the hook resources before enabling them in an agent environment.

Risk: The skill may inspect agent transcripts and configuration and persist or delete task state.

Mitigation: Limit access to sensitive agent files, review task-state changes, and confirm deletion of pending work.

Risk: Automatic external status checks may contact GitHub, SSH hosts, or deployment endpoints.

Mitigation: Review remote-check guidance and restrict credentials and network access to trusted endpoints.

## Reference(s):

- [WIP on ClawHub](https://clawhub.ai/drumrobot/skills/wip)
- [Claude Code task tracking guide](artifact/claude.md)
- [Antigravity task tracking guide](artifact/antigravity.md)
- [Task cleanup and resumption guide](artifact/resume.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Configuration instructions]

**Output Format:** [Task checklists and conversational progress updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May update persistent task or checklist state.]

## Skill Version(s):

0.7.4 (source: ClawHub release metadata and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
