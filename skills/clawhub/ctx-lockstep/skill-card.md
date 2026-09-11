## Description:

Manage long-term project context and session-resume checkpoints for Git and non-Git projects, including project adoption, drift detection, checkpointing, and archiving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[holdyounger](https://clawhub.ai/user/holdyounger)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use Ctx-Lockstep to bring long-running Git or non-Git projects under file-based context management, resume work from .ctx-lockstep/PROJECT.md, detect unsaved project drift, and save checkpoints before pauses or handoffs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup can modify Git repositories by adding a persistent post-commit hook that records commit metadata.

Mitigation: Use the skill only on projects where local commit-subject logging is acceptable, and review or remove the marked ctx-lockstep block from .git/hooks/post-commit if ongoing commit-time logging is not desired.

Risk: The security verdict is suspicious because the skill performs local setup that persists after initialization.

Mitigation: Review the generated .ctx-lockstep files and hook changes before relying on the skill in sensitive repositories.

## Reference(s):

- [Ctx-Lockstep ClawHub release](https://clawhub.ai/holdyounger/skills/ctx-lockstep)
- [Ctx-Lockstep project link declared by artifact](https://github.com/holdyounger/ctx-lockstep)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and generated project context files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3; setup may create .ctx-lockstep files and append a marked post-commit hook block in Git projects.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
