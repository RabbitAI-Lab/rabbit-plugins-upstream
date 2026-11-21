## Description:

A language-agnostic seven-step debugging workflow with offline tools that turn reproduction, log triage, environment checks, and regression results into verifiable evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to investigate software errors systematically, document reproducible cases, identify likely fault layers, and verify fixes with regression evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation terms and differences between claimed and assessed capabilities may make the skill a poor fit for some workflows.

Mitigation: Review its activation terms and advertised capabilities against the intended debugging use before enabling it.

Risk: The reported environment access and local tool scope may expose more context than expected.

Mitigation: Review local commands and environment fields before running the tools, and inspect and redact generated environment details before sharing them.

## Reference(s):

- [Evidence-first debugging](artifact/references/evidence-first.md)
- [Worked debugging example](artifact/references/worked-example.md)
- [ClawHub release page](https://clawhub.ai/zhaoxinghua09-cell/skills/debug-pro)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, JSON, Shell commands]

**Output Format:** [Markdown guidance with shell commands and optional JSON or Markdown diagnostic reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local, offline workflow; included tools use the Python standard library.]

## Skill Version(s):

2.1.5 (source: SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
