## Description:

moa-engine orchestrates multi-role expert reasoning with structured adversarial review, XML-tagged information flow, intelligent routing, and recursive self-improvement guidance for complex analysis and design tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kiwifruit13](https://clawhub.ai/user/kiwifruit13)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, architects, and AI practitioners use this skill to structure complex cross-domain analysis, architecture review, high-risk decision scrutiny, and multi-perspective solution design through explicit expert, critic, and synthesis roles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow and reference material are primarily Chinese-language, which can make review difficult for teams that cannot read Chinese.

Mitigation: Install only when reviewers can understand the Chinese-language workflow or have translated and reviewed the prompts and references before use.

Risk: The RHI self-improvement material can involve retaining logs, building failure databases, or patching agent behavior as an opt-in design pattern.

Mitigation: Before adopting RHI practices, confirm the storage location, review path, rollback process, and user approval requirements.

Risk: For privacy, finance, medical, security, or compliance tasks, the artifact calls for audit logging and human confirmation around high-risk decisions.

Mitigation: Use the skill's high-risk path only with explicit review checkpoints, decision-chain audit records, and human final confirmation for critical decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kiwifruit13/skills/moa-engine)
- [PROJECT_OVERVIEW.md](references/PROJECT_OVERVIEW.md)
- [moa-system-guide.md](references/moa-system-guide.md)
- [moa-tag-system.md](references/moa-tag-system.md)
- [moa-routing-design.md](references/moa-routing-design.md)
- [moa-meta-prompt.md](references/moa-meta-prompt.md)
- [moa-rhi-guide.md](references/moa-rhi-guide.md)
- [moa-phase-transition.md](references/moa-phase-transition.md)
- [moa-case-study.md](references/moa-case-study.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown guidance with XML-tagged reasoning templates and reference-document navigation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No executable installer or hidden data-access behavior was found in the security evidence.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact SKILL.md frontmatter states 2.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
