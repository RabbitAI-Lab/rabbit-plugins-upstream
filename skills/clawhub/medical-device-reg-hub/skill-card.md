## Description:

A Chinese-language, document-only regulatory reference skill that helps medical-device registration teams navigate global classification, submission, quality, UDI, labeling, clinical evaluation, and post-market topics using curated official-source links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

External regulatory affairs, product, quality, and market-access teams use this skill to locate official medical-device regulatory references, compare registration pathways, and produce checklists, tables, Markdown summaries, or HTML reference deliverables. It is a reference aid and does not replace formal regulatory, legal, or registration-agent advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat reference output as formal regulatory, legal, or registration-agent advice.

Mitigation: Present the skill as a regulatory reference aid, direct complex filings or disputes to qualified RA professionals or counsel, and avoid final filing conclusions without expert review.

Risk: Regulatory links, deadlines, classifications, fees, and submission templates can change after the bundled references were checked.

Mitigation: Verify time-sensitive information against the official regulator source before filing, submitting, labeling, or making market-access decisions.

Risk: Generic trigger terms may activate the skill outside a medical-device registration context.

Mitigation: Confirm the user is asking about medical-device registration before relying on the skill, and redirect unrelated requests to a general assistant or a more appropriate skill.

Risk: Borderline products may receive misleading classifications if the assistant guesses beyond verified examples.

Mitigation: Mark uncertain products as pending verification and point users to the relevant official classification or regulator inquiry process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/medical-device-reg-hub)
- [MedXpert public knowledge base](https://medxpert.cn/knowledge/)
- [注册工程师资料枢纽](references/注册工程师资料枢纽.md)
- [枢纽总览_全生命周期7阶段纲领](references/枢纽总览_全生命周期7阶段纲领.md)
- [骨科手术器械_全球注册路径汇编](references/骨科手术器械_全球注册路径汇编.md)
- [UDI全球标识枢纽](references/UDI全球标识枢纽.md)
- [技术文件STED撰写枢纽](references/技术文件STED撰写枢纽.md)
- [GMP质量体系与验证枢纽](references/GMP质量体系与验证枢纽.md)
- [临床评价枢纽](references/临床评价枢纽.md)
- [上市后监管枢纽](references/上市后监管枢纽.md)
- [FDA_UDI实施实务](references/FDA_UDI实施实务.md)
- [EU_EUDAMED数据库实务](references/EU_EUDAMED数据库实务.md)
- [EU_MDR上市后监管PMS实务](references/EU_MDR上市后监管PMS实务.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, HTML, Guidance]

**Output Format:** [Chinese Markdown, tables, checklists, and optional HTML reference deliverables with official-source links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should cite relevant official links from the bundled references, mark uncertain classification or pathway items as pending verification, and remind users to check current regulator sources before filing.]

## Skill Version(s):

1.5.0 (source: frontmatter, manifest.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
