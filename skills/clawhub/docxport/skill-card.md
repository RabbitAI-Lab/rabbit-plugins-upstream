## Description: <br>
Converts Markdown, HWP, DOCX, RTF, and Marp slide files to PDF, PNG, HTML, DOCX, or PPTX using a LibreOffice-first document conversion workflow with internal-only fallbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and document authors use Docxport to convert Markdown, Word/HWP/RTF documents, and Marp decks into PDF, PNG, HTML, DOCX, or PPTX deliverables while preserving layout, tables, images, and review artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Confidential slide content may be exposed when the Mermaid CDN and browser-print workflow is used. <br>
Mitigation: Avoid that workflow for confidential documents or replace it with a local/offline renderer. <br>
Risk: Large local tool installs such as LibreOffice or Chromium-based converters can affect the user's machine and network usage. <br>
Mitigation: Review dependency checks and approve any large installs before conversion begins. <br>
Risk: Official or external PDFs can be unsuitable if an internal-only converter such as Prince adds a non-commercial watermark. <br>
Mitigation: Classify the delivery medium first, use watermark-clean converters for official outputs, and require explicit approval before using internal-only fallbacks. <br>
Risk: Text-only HWP fallback can lose images, tables, and document layout. <br>
Mitigation: Prefer LibreOffice PDF or HTML conversion for rich-format analysis and offer text-only fallback only with a clear loss-of-formatting note. <br>


## Reference(s): <br>
- [Docxport on ClawHub](https://clawhub.ai/drumrobot/skills/docxport) <br>
- [Docxport skill instructions](SKILL.md) <br>
- [DOCX conversion guide](docx.md) <br>
- [Marp slide conversion guide](marp.md) <br>
- [Mermaid CDN module referenced for Marp HTML rendering](https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash, PowerShell, HTML, YAML, and CSS snippets; converted document files when executed.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Expected file outputs include PDF, PNG page images, HTML, DOCX, and PPTX depending on input and flags.] <br>

## Skill Version(s): <br>
0.1.1 (source: server release evidence, target metadata, and CHANGELOG; released 2026-07-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
