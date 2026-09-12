## Description:

PASM Learning Tutor Agent is an offline learning tutor that tracks per-topic mastery, selects weak topics for practice, gives encouraging feedback, and exports machine-readable progress snapshots.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

External users, educators, and developers use this agent to build adaptive tutoring flows that track knowledge-topic mastery, choose next practice topics, and export learner progress for profile or reporting systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable Python package installation can introduce normal dependency risk.

Mitigation: Install in a virtual environment or container, avoid administrator pip, and pin reviewed package versions.

Risk: Saved learner state can persist mastery data and mistake history.

Mitigation: Treat saved snapshots and mistake history as learner data, and use save or interactive mode only where persistence is intended.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-tutor)
- [PASM agents homepage listed in artifact](https://github.com/arronJack/pasm-agents)
- [PASM skills tutorial linked by artifact](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [PASM agents source install fallback listed in artifact](https://gitee.com/arronzheng/pasm-agents)

## Skill Output:

**Output Type(s):** [text, JSON, guidance]

**Output Format:** [Text tutoring responses and JSON-compatible progress snapshots, with Markdown and shell-command examples in documentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-runnable; persisted learning state and mistake history may be saved when using save or interactive mode.]

## Skill Version(s):

0.4.1 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
