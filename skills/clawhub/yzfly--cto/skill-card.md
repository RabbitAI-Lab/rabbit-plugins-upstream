## Description:

Startup / AI-startup CTO who is also a top-tier individual contributor. Two modes: (1) greenfield — turn fuzzy business intent into a buildable design (brief.md, arch.md, specs/) through conversation; (2) brownfield — work hands-on inside an existing codebase: investigate, recommend, refactor, write features, debug, ship PRs, update ADRs and plan docs. Trigger when the user wants to build something new ('I want to build', 'help me design', '我想做', '帮我想想这个怎么做'), AND trigger when the user invokes /cto on an existing codebase for architecture work, migrations, refactors, debugging, or any senior-IC task they want CTO-level judgment and execution on. Do NOT trigger for trivial one-off coding questions where no architectural judgment is needed.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yzfly](https://clawhub.ai/user/yzfly)

### License/Terms of Use:

CC BY-NC 4.0

## Use Case:

External developers and founders use this skill to turn early product ideas into practical technical designs, or to get senior engineering investigation and implementation help in an existing codebase.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags host-level privileged commands that can change machine configuration.

Mitigation: Review each proposed command and run only changes needed for the task.

Risk: The security assessment flags guidance that could share or register private code externally.

Mitigation: Keep private source local and obtain approval before sending it to an external service.

Risk: The security assessment flags remote installation and update paths that are not pinned.

Mitigation: Verify the source and prefer a pinned release or commit when installing or updating.

Risk: The assessment has incomplete coverage, so unreported content is not established as safe.

Mitigation: Review relevant files and inspect commands before execution.

## Reference(s):

- [CTO on ClawHub](https://clawhub.ai/yzfly/skills/cto)
- [Repository referenced by the README](https://github.com/yzfly/skills)
- [Reference library overview](references/README.md)
- [Architecture tradeoffs guide](references/runtime/tradeoffs.md)
- [Design artifact templates](references/runtime/templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Files, Code]

**Output Format:** [Conversational guidance and project artifacts such as design documents, plans, code, tests, and pull request changes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The deliverable depends on whether the work is greenfield design or changes to an existing codebase.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
