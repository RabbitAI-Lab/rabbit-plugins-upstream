## Description:

Runs a configurable end-of-session workflow to review work, preserve useful findings, synchronize task records, and prepare a handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and other agent users use this skill at session wrap-up to review mistakes and hooks, preserve discoveries, update checklists, and plan follow-up work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Session content, identifiers, and artifacts may be retained in RAG storage or local queues.

Mitigation: Review and disable unwanted memory or RAG storage; avoid confidential sessions without a retention and deletion plan.

Risk: Broad wrap-up triggers can commit changes or modify task and checklist state unexpectedly.

Mitigation: Review the workflow and disable unwanted auto or Ralph modes, Stop triggers, and hook wrappers before use.

## Reference(s):

- [Cleanup skill listing](https://clawhub.ai/drumrobot/skills/cleanup)
- [Cleanup workflow](artifact/run.md)
- [Configuration guide](artifact/config.md)
- [RAG storage guide](artifact/rag-store.md)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown reports and recommendations, with task and knowledge-record updates when enabled]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can update repository and checklist state or preserve session findings, depending on configuration.]

## Skill Version(s):

0.10.0 (source: ClawHub release and CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
