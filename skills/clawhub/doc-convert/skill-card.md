## Description: <br>
doc-convert guides agents through watermark-aware conversion of Markdown, HWP, DOCX, RTF, and Marp slide files into PDF, PNG, HTML, DOCX, or PPTX outputs using LibreOffice-first workflows and documented fallbacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineers, and document-focused agents use this skill to convert Markdown, HWP, DOCX, RTF, and Marp sources into presentation or document deliverables while preserving layout and avoiding watermark leakage in official outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Marp HTML conversion can permit active HTML or script behavior when processing untrusted Markdown. <br>
Mitigation: Avoid Marp HTML conversion on untrusted Markdown and review source content before enabling HTML-based slide features. <br>
Risk: Dependency checks or fallbacks may trigger npm/npx or system package downloads when tools are missing. <br>
Mitigation: Require user approval before installing LibreOffice, Marp CLI, Chromium-backed tooling, or other missing conversion dependencies. <br>
Risk: Conversion workflows create output files and can overwrite existing artifacts if paths are not reviewed. <br>
Mitigation: Review input and output paths before execution and report produced file paths after conversion. <br>
Risk: Prince can add a non-commercial watermark that is unsuitable for official or external deliverables. <br>
Mitigation: Use LibreOffice or another watermark-clean converter for official outputs, and reserve Prince only for explicitly approved internal drafts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/doc-convert) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>
- [DOCX conversion guide](artifact/docx.md) <br>
- [Marp slide conversion guide](artifact/marp.md) <br>
- [Dependency checker](artifact/scripts/check-deps.sh) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with inline shell and PowerShell command examples; converted files may be produced when an agent executes the workflow.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance emphasizes medium classification, dependency checks, watermark-clean converters for official output, and explicit user approval before large installs or watermarked fallbacks.] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata and target metadata; artifact frontmatter says 0.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
