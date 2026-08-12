## Description:

AI Delivery Spec helps agents create, change, review, reverse-engineer, and accept requirements, PRDs, prototypes, competitor material, and existing-system changes with traceable outputs from framing through acceptance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[franklinxkk](https://clawhub.ai/user/franklinxkk)

### License/Terms of Use:

Apache 2.0

## Use Case:

Product, engineering, design, testing, compliance, and delivery teams use this skill to turn ideas, existing materials, system changes, and acceptance needs into the smallest complete requirement artifact for the current stage. It supports lightweight changes through governed baselines, change impact analysis, traceability, and acceptance records without taking over scheduling, coding, deployment, or operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated checkpoints, snapshots, custom packs, and requirement artifacts can retain project artifacts or metadata.

Mitigation: Use a private workspace for sensitive projects, keep custom packs local or team-scoped, and avoid placing secrets or raw confidential evidence in generated artifacts.

Risk: The skill is broad and can produce governance artifacts across requirements, prototypes, traceability, and acceptance.

Mitigation: Invoke it deliberately for requirements governance work, keep to the smallest relevant stage slice, and review generated artifacts before sharing or baselining them.

Risk: Language handling can affect visible requirement text and machine-value display outside zh-CN.

Mitigation: Review the document_language field and use the documented language gate options before distributing outputs.

Risk: Local gates and static checks do not prove domain correctness, browser behavior, implementation quality, production safety, or customer acceptance.

Mitigation: Treat static PASS results as structural evidence only and require role review, execution evidence, implementation tests, and customer or domain sign-off where relevant.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/franklinxkk/skills/ai-delivery-spec)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Stages](references/stages.md)
- [Lifecycle](references/lifecycle.md)
- [Specification guidance](references/specify.md)
- [Prototype guidance](references/prototype.md)
- [Change and acceptance guidance](references/change-acceptance.md)
- [Tool adapters](references/tool-adapters.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Human-facing Markdown plus optional YAML/JSON contracts, schemas, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include stage-specific requirement artifacts, PRDs, prototypes, review records, traceability ledgers, change packages, acceptance records, and local validation results.]

## Skill Version(s):

5.4.6 (source: changelog, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
