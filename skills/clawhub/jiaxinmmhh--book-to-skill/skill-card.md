## Description:

Turns technical books, PDFs, white papers, design standards, and manuals into reusable AI skill packs that capture procedures, decision rules, templates, anti-patterns, and mental models rather than only retrieving source text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jiaxinmmhh](https://clawhub.ai/user/jiaxinmmhh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, training teams, and content teams use this skill to transform authorized text PDFs or structured documents into importable agent skills. It is intended for cases such as code-review methods, brand-review rules, investment research playbooks, or internal SOPs where an agent should apply a methodology while working.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Source documents may contain confidential, regulated, or copyrighted material.

Mitigation: Use only documents you are authorized to transform, redact sensitive content when needed, and avoid sharing generated skills that expose protected source material.

Risk: Generated skills may encode incomplete or misleading methodology if the distillation is low quality.

Mitigation: Review generated SKILL.md and references before import or distribution, and spot-check coverage against structure.md and high-value source sections.

Risk: Image-only or scanned PDFs can produce missing or poor extraction results.

Mitigation: Check metadata.json for scanned-page warnings and OCR image-only PDFs before distillation.

## Reference(s):

- [Distillation Guide](references/distill-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/jiaxinmmhh/skills/book-to-skill)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and generated skill files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a scaffold with metadata.json, structure.md, sections/*.md, SKILL.md, and references/ content for reviewer-controlled import.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
