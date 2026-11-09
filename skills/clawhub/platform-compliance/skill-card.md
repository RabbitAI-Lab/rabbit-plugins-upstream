## Description:

上架前平台合规校验与自动修复。待上架图 → Amazon / TikTok Shop / Temu / Shopee / 淘宝 各平台的通过或驳回风险报告，可一键修成合规图。

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and catalog operators use this skill to check product images against supported marketplace listing requirements and to create corrected image copies for supported size, color, and layout issues.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A confirmed exit-status issue could let unreadable images pass a CI compliance gate.

Mitigation: Review and resolve the exit-status issue, then verify unreadable-image cases fail closed before relying on the skill as a CI gate.

Risk: The security guidance notes undeclared environment and network access, external provider requests, and an unpinned reference.

Mitigation: Review the required environment access, network destinations, provider data sharing, and external reference; restrict permissions and pin the reference where appropriate.

Risk: The security scan inspected only 6 of 10 components fully, leaving the evidence incomplete.

Mitigation: Complete review or scanning of the four partially inspected components before relying on the skill in a production workflow.

## Reference(s):

- [Platform image specifications](references/platform-specs.md)
- [detect-task visual checks](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)
- [item-repair image editing](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/item-repair/skill.md)
- [remove-watermark](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/remove-watermark/skill.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Image files]

**Output Format:** [Human-readable compliance report, optional JSON report, and optional corrected image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports single images and batches; corrected files are saved separately from the originals.]

## Skill Version(s):

1.0.29 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
