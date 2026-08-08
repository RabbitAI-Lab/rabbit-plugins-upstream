## Description:

skill-audit helps agents inspect OpenClaw skill folders against the ClawHub publishing checklist and return a scored pass/fail report with concrete fixes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kimmyplusli](https://clawhub.ai/user/kimmyplusli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill publishers use this skill before publishing or installing OpenClaw skills to review security, metadata, declaration consistency, and discoverability. It produces an evidence-based audit report that flags blockers and concrete fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads and analyzes folders named by the user, so an overly broad path could expose unrelated local files to the audit process.

Mitigation: Name the exact skill folder or inspected third-party skill files that should be reviewed.

Risk: Optional dependency, homepage, or discoverability checks can run local CLI tools or network reachability checks when requested.

Mitigation: Run those checks only in a controlled environment and review proposed commands before execution.

Risk: The audit report is advisory and can miss semantic prompt-injection behavior that requires human judgment.

Mitigation: Review the audited skill's prose and scanner findings before publishing or installing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kimmyplusli/skills/skill-audit)
- [OpenClaw](https://openclaw.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown scored audit report with findings, declaration diff, and concrete fixes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses local inspection of user-named skill folders and may propose optional CLI checks for dependencies, homepage reachability, or discoverability.]

## Skill Version(s):

0.2.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
