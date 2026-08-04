## Description: <br>
Convert Markdown research reports, fact-checks, and scheme proposals into styled PDFs with native CJK font support while keeping Markdown as the editable source of truth. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xcjl](https://clawhub.ai/user/0xcjl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to turn long-form Markdown reports into shareable PDFs while preserving the Markdown file for editing and handoff. It is especially suited to research reports, fact-checks, technical proposals, and mixed Chinese-English documents that need CJK-safe PDF rendering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated PDFs and editable Markdown sources may be uploaded to chat as part of the normal workflow. <br>
Mitigation: For confidential reports, request local-only generation or confirm the exact destination before any upload. <br>
Risk: Multi-platform delivery can send files more broadly than intended if a broad target is used. <br>
Mitigation: Avoid target="all" unless broad delivery is explicitly intended, and confirm the platform and recipient before sending. <br>
Risk: The workflow includes local dependency installation and helper-script execution patterns. <br>
Mitigation: Inspect commands and any referenced /tmp helper script before running them in sensitive environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/0xcjl/skills/md-pdf-report) <br>
- [README](artifact/README.md) <br>
- [PDF engine comparison](artifact/references/pdf-engine-comparison.md) <br>
- [macOS CJK font reference](artifact/references/macos-cjk-fonts.md) <br>
- [weasyprint C library bootstrap recipe](artifact/references/weasyprint-bootstrap.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Files, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown guidance with bash and Python snippets; generated artifacts are Markdown source files and styled PDF files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [PDF rendering uses Markdown-to-HTML-to-PDF conversion with CJK font support; chat delivery may upload both PDF and Markdown artifacts when requested.] <br>

## Skill Version(s): <br>
0.2.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
