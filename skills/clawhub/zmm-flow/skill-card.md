## Description:

Analyzes talking-head and whiteboard scripts beat by beat to identify where viewers may lose the thread, drop off, or need a clearer spoken transition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Solo knowledge creators and their agents use this skill to review short-form video scripts for listener flow, retention risk, and concrete spoken fixes. After diagnosis, it can ask whether to produce a marked revision while preserving the user's original points, examples, numbers, and voice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local vault rules and saved feedback may steer future script reviews without clear user control.

Mitigation: Review the local rules and memory entries before deployment, keep them scoped to the relevant user or project, and remove stale or unwanted entries.

Risk: Private script material or business metrics could be exposed through memory-backed feedback workflows.

Mitigation: Avoid storing sensitive drafts, private metrics, or client material unless maintainers can inspect and delete the resulting memory entries.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-flow)
- [Built-in rule card](artifact/references/规则卡.md)
- [Evaluation README](artifact/evals/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown report with a listener timeline, drop-off findings, suggested spoken fixes, and optional marked-up revision guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May incorporate local zmm vault rules and saved feedback when available; produces human-facing script guidance rather than code or shell commands.]

## Skill Version(s):

0.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
