## Description:

Learning tutor agents built on the PASM cognitive engine that track per-topic mastery, select weak topics for practice, provide encouraging template-based replies, and export machine-readable learning snapshots while running offline without an LLM dependency.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and education product builders use this skill to add adaptive tutoring behavior that tracks mastery by topic, recommends the weakest topic to practice, and exports student learning state for profiles, reports, or parent-facing views.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Stored learning snapshots and mistake memories may contain student data.

Mitigation: Review where pasm-agents saves state and apply appropriate privacy controls before using the tutor with real learners.

Risk: Installing the tutor brings in the broader PASM dependency stack.

Mitigation: Install only when the PASM dependency stack is acceptable for the target environment.

Risk: Mastery does not automatically decay when a topic is not practiced, and memory recall uses literal matching rather than semantic retrieval.

Mitigation: Treat mastery and recalled mistakes as tutoring signals that should be reviewed or supplemented by the calling application.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-tutor)
- [pasm-agents homepage](https://github.com/arronJack/pasm-agents)
- [pasm-skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)
- [pasm-agents Gitee source install](https://gitee.com/arronzheng/pasm-agents)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration, JSON]

**Output Format:** [Markdown with Python and shell examples, plus JSON-compatible learning snapshots]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Offline-runnable tutor behavior; snapshots include mastery, weakest topic, average, history size, and tier.]

## Skill Version(s):

0.4.11 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
