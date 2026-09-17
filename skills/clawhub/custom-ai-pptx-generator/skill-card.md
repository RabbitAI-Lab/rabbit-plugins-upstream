## Description:

Custom AI PPTX Generator helps agents turn requirement notes, source materials, and user-approved design decisions into native editable PowerPoint decks with structured storyboards, visual prototypes, rendered previews, and delivery notes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kenzje228](https://clawhub.ai/user/kenzje228)

### License/Terms of Use:

MIT

## Use Case:

Employees, consultants, trainers, project managers, sales and marketing teams, educators, and other presentation authors use this skill to convert prompts, documents, email, tables, images, and other source material into content-driven editable PPTX presentations. The workflow emphasizes human confirmation of structure, visual direction, and final previews before native PowerPoint generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user presentation materials and may route preview-generation work through cloud image-generation services.

Mitigation: Use approved data only, avoid sensitive materials with cloud image tools unless authorized, and keep original content and approved storyboards as the source of truth.

Risk: The authoritative security scan reports that some bundled helper scripts can silently overwrite local output files despite no-overwrite claims.

Mitigation: Run the workflow in a dedicated empty output folder and review or patch overwrite behavior before using cutout.py or export_png_template.ps1 on important files.

Risk: Visual prototype tools can alter text, numbers, labels, dates, or page order before final PPTX reconstruction.

Mitigation: Compare generated previews against the approved ASCII storyboard and source materials, then include a page mapping and content-difference note with delivery.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kenzje228/skills/custom-ai-pptx-generator)
- [README](README.md)
- [千题千境 AI-PPT 工作流 · 项目经验总结](references/千题千境_项目经验总结.md)
- [千题千境 PPT skill — 6 页提示词包](references/prompts/千题千境_6页提示词.md)
- [千题千境 PPT skill — 童趣版 6 页提示词（单 block 一键复制版）](references/prompts/千题千境_单block提示词.txt)
- [SSC 自动化项目汇总报告 · 6 页样图提示词（单 block 版）](references/prompts/SSC自动化_单block提示词.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with storyboards, prompts, Python or PowerShell command examples, and generated PPTX/PNG file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce editable PPTX files, rendered PNG previews, visual prompt packs, and delivery notes when the required local tools are available.]

## Skill Version(s):

1.0.1 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
