## Description:

Orchestrates a multi-role expert team through structured critique, logical synthesis, XML-tagged information flow, intelligent routing, and recursive self-improvement for complex analysis and design tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, product teams, and reviewers use this skill to structure multi-perspective analysis, architecture review, high-risk decision scrutiny, and cross-domain solution design. It is best suited to complex tasks where planning, expert-role reasoning, critique, and synthesized recommendations are useful.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may keep and reuse performance signals across runs, which can influence future agent behavior without clear user controls.

Mitigation: Confirm where signal and audit outputs are stored, set retention and access controls, and disable or gate profile updates when persistent learning is not desired.

Risk: Sensitive privacy, financial, medical, legal, compliance, or security work may expose sensitive context through audit outputs or signal files.

Mitigation: Use the skill on sensitive work only after confirming storage behavior, limiting sensitive inputs, and requiring human review for high-risk conclusions.

Risk: Prompt or harness evolution can change how future runs behave.

Mitigation: Require approval before generated enhancement instructions or patches alter production workflows, and keep rollback criteria for behavior changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiwifruit13/skills/moa-engine)
- [MoA system guide](references/moa-system-guide.md)
- [MoA tag system](references/moa-tag-system.md)
- [MoA routing design](references/moa-routing-design.md)
- [MoA meta prompt](references/moa-meta-prompt.md)
- [Architecture overview](references/architecture-overview.md)
- [RHI guide](references/moa-rhi-guide.md)
- [Fitness function](references/fitness-function.md)
- [Patch specification](references/patch-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, JSON, XML-tagged analysis, shell commands, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce structured intermediate outputs for task classification, expert matching, red-team prompts, fitness scoring, and harness improvement; review outputs before applying changes.]

## Skill Version(s):

1.0.2 (source: server release metadata; artifact frontmatter describes MoA engine protocol version 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
