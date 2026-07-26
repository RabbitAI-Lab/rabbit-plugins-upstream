## Description: <br>
Translates research-paper PDFs into readable, searchable PDFs in another language while rebuilding layout, tables, diagrams, captions, notes, and figure text needed for comprehension. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ezra-y](https://clawhub.ai/user/ezra-y) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use this skill to convert academic PDFs into readable, searchable translated PDFs. It supports full-text translation workflows with automated checks, source-output review, consolidated repair, and optional Zotero finalization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The broad Pillow dependency range can accept vulnerable image-processing versions. <br>
Mitigation: Pin Pillow to a patched current version and run dependency scanning before installation. <br>
Risk: Workspace/.work keeps source PDFs and intermediate processing files. <br>
Mitigation: Use a protected workspace for sensitive papers and remove intermediate files when retention is not needed. <br>
Risk: Zotero finalization changes Zotero attachments. <br>
Mitigation: Confirm Zotero finalization is desired and back up or review the target Zotero library before running that step. <br>


## Reference(s): <br>
- [README_EN.md](README_EN.md) <br>
- [Workspace and Output Specification](references/workspace.md) <br>
- [Document Routing](references/routing.md) <br>
- [Translation Scope](references/translation-scope.md) <br>
- [Quality Contract](references/quality-contract.md) <br>
- [Layout and Readability](references/layout-readability.md) <br>
- [Semantic Review](references/semantic-review.md) <br>
- [QA and Acceptance](references/qa-acceptance.md) <br>
- [Language Profiles](references/language-profiles.md) <br>
- [Zotero Finalization](references/zotero-finalization.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON configuration, workspace files, and translated searchable PDF outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates batch workspaces with source PDFs in input/, hidden intermediate files in .work/, and accepted translated PDFs in output/.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
