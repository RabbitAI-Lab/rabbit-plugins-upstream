## Description:

Multi Agent Dev helps agents route coding work across OpenClaw, sub-agents, and Ralph Loop with configurable AI coding executors for iterative software development.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hehe973781230](https://clawhub.ai/user/hehe973781230)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering agents use this skill to classify coding tasks, choose between direct execution, sub-agent delegation, and Ralph Loop iteration, and produce structured implementation prompts and commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad coding requests may be routed into external iterative agents with limited confirmation.

Mitigation: Require user confirmation before spawning agents, creating directories, or running Ralph Loop for broad tasks.

Risk: The workflow depends on an unpinned global Ralph Wiggum npm package.

Mitigation: Pin and verify the Ralph Wiggum package before installation, and avoid elevated global npm installs when possible.

Risk: External coding agents may run outside the intended project scope.

Mitigation: Use the skill only inside intended project workspaces and review generated commands before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/hehe973781230/skills/multi-agent-dev)
- [Ralph Wiggum](https://github.com/Th0rgal/open-ralph-wiggum)
- [README](artifact/README.md)
- [Skill source](artifact/SKILL.md)
- [Changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code blocks, shell commands, task templates, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose external agent execution through Ralph Loop and configurable coding CLIs.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact changelog lists v1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
