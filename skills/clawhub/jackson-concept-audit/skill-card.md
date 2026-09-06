## Description:

Audits an existing codebase against its Jackson concept model, covering specification drift, boundaries, criteria, composition, dependencies, and cross-spec validation in a read-only workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering reviewers use this skill to audit an existing repository against Jackson concept specifications and PRDs. It produces a findings report with severity, evidence, systemic patterns, and routing to design, PRD, or implementation follow-up skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read concept specs, PRDs, implementation files, and dependency artifacts across a private repository during audit.

Mitigation: Run it only in repositories whose contents the user is comfortable exposing to the agent, and keep access read-only.

Risk: Audit findings can be incomplete or misleading if specifications are missing, stale, or only partially discovered.

Mitigation: Review the reported scope, skipped dimensions, evidence locations, and severity routing before using findings to plan fixes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agenticweb4/skills/jackson-concept-audit)
- [Publisher profile](https://clawhub.ai/user/agenticweb4)
- [Jackson concept criteria tutorial](https://essenceofsoftware.com/tutorials/concept-basics/criteria/)
- [Concept design overview](https://essenceofsoftware.com/posts/distillation/)
- [Jackson dependency and subset tutorial](https://essenceofsoftware.com/tutorials/concept-basics/dependency/)
- [WYSIWID paper](https://arxiv.org/abs/2508.14511)
- [Beyond Objects paper](https://arxiv.org/abs/2606.27258)
- [WYX upstream reference](https://github.com/jlifyio/wyx)

## Skill Output:

**Output Type(s):** [analysis, markdown, guidance]

**Output Format:** [Markdown audit report with findings tables and ordered repair guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only output; does not modify repository files.]

## Skill Version(s):

0.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
