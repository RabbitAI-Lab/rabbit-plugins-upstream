## Description:

HaoLvShi Legal Skill provides legal-service workflows through HaoLvShi APIs for consultation reports, compensation calculators, contract review, complaints, and answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mtcto](https://clawhub.ai/user/mtcto)

### License/Terms of Use:

MIT No Attribution

## Use Case:

External users and agents use this skill to route legal questions, compensation calculations, contract reviews, and litigation-document drafting into guided HaoLvShi workflows. It collects current-task facts and materials, then returns report summaries, legal-document summaries, and links to online reports or Word documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Legal questions, contracts, case materials, and extracted document text may be sent to HaoLvShi remote services.

Mitigation: Use the skill only for matters where remote processing is acceptable, provide only current-task materials needed for the workflow, and remove sensitive local task state with cleanup when finished.

Risk: Broad invocation could route unrelated legal files or facts into a legal-service workflow.

Mitigation: Prefer explicit invocation, keep inputs limited to the current task and matching session, and ask the user before using ambiguous or unrelated materials.

Risk: Windows setup uses PowerShell with ExecutionPolicy Bypass and installer scripts may download a Node.js runtime.

Mitigation: Review the bootstrap commands before running them and use the health command after installation to confirm the expected runtime and service connectivity.

Risk: Generated legal summaries, calculations, and documents may depend on incomplete facts or jurisdiction-specific assumptions.

Mitigation: Treat outputs as legal-service results that require user or professional review, and do not add external legal conclusions beyond the generated report or document.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mtcto/skills/haolvshi-legal-skill)
- [Skill homepage](https://skills.ai.lvpin100.com)
- [Installation documentation](https://skills.ai.lvpin100.com/skills/haolvshi-legal-skill/INSTALL.md)
- [法律咨询报告流程](references/consultation.md)
- [法律计算器流程](references/calculator.md)
- [智能合同审核流程](references/contract-review.md)
- [起诉状和答辩状流程](references/pleading.md)
- [案件材料识别与复用](references/case-materials.md)
- [交互呈现规范](references/interaction.md)
- [错误处理规范](references/errors.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files]

**Output Format:** [JSON workflow responses and Markdown summaries with links to online reports or Word documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses remote HaoLvShi services and stores local temporary task state for up to 24 hours unless cleanup is invoked.]

## Skill Version(s):

1.9.0 (source: server release metadata; artifact frontmatter, metadata, and package.json report 1.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
