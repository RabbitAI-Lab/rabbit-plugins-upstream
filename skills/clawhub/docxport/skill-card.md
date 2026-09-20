## Description:

Docxport guides agents through Markdown, HWP, DOCX, RTF, and Marp document conversion to PDF, PNG, HTML, DOCX, or PPTX with a LibreOffice-first workflow for watermark-free external deliverables.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose safe document conversion paths, check required tools, and produce user-facing deliverables while avoiding watermark leakage, layout loss, and silent text-only fallbacks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Conversion workflows can fetch unpinned remote packages through tools such as npx or uvx.

Mitigation: Use pinned or preinstalled converter versions for trusted workflows, especially in environments that handle sensitive documents.

Risk: Private slide decks can load third-party Mermaid scripts from a CDN.

Mitigation: Use local Mermaid assets instead of CDN scripts when converting private or sensitive decks.

Risk: Document conversion can overwrite or misplace generated files if output paths are not checked.

Mitigation: Confirm output paths before running conversions and report the final generated file paths.

Risk: Watermarked or lossy fallback converters can create unsuitable external deliverables.

Mitigation: Prefer LibreOffice for official outputs, reserve internal-only fallbacks for drafts, and make any text-only fallback explicit.

## Reference(s):

- [ClawHub docxport skill page](https://clawhub.ai/drumrobot/skills/docxport)
- [DOCX conversion guide](docx.md)
- [Marp slide conversion guide](marp.md)
- [Dependency check helper](scripts/check-deps.sh)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown with inline shell commands and conversion procedures]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead the agent to create PDF, PNG, HTML, DOCX, or PPTX files using local conversion tools.]

## Skill Version(s):

0.2.1 (source: release evidence and CHANGELOG, released 2026-09-18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
