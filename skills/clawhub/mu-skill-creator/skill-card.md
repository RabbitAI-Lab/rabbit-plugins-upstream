## Description:

Skill创建与质量门控，含55项10层审计模型。触发词：创建skill、skill创建、skill审计、质量审计。不适用：skill发布、生态体检（用mu-skill-auditor）

This skill is ready for commercial/non-commercial use.

## Publisher:

[muippt](https://clawhub.ai/user/muippt)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use this skill to create, optimize, and audit agent skills through a gated workflow with quality checks, trigger optimization, and handoff guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit script can be mistaken for a complete governance review.

Mitigation: Treat script output as evidence within the full 55-item audit, and require human review for non-scriptable quality and design checks.

Risk: The local audit workflow scans skill directories selected by the user.

Mitigation: Run the audit script only against skill directories intended for inspection.

Risk: The handoff workflow can be mistaken for direct publication.

Mitigation: Treat delivery as packaging and handoff; publish only through the appropriate external platform workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/muippt/skills/mu-skill-creator)
- [README.md](README.md)
- [Quality Gates 质量门控完整指南](references/quality-gates.md)
- [推荐联动指南](references/collaboration-guide.md)
- [Eval examples](evals/evals.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, generated skill files, reference documents, and audit findings]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local creation and audit guidance; delivery is pre-release packaging and handoff, not publication.]

## Skill Version(s):

3.7.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
