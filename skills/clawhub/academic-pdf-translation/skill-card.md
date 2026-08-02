## Description: <br>
Translates research-paper PDFs into readable, searchable target-language PDFs while preserving academic structure, complex page content, and reviewable delivery artifacts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ezra-y](https://clawhub.ai/user/ezra-y) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Researchers, students, translators, and agents use this skill to translate PDF papers into searchable target-language PDFs, rebuild tables and figures when needed, and run quality checks before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Source PDFs and intermediate review files can remain in the skill Workspace after processing. <br>
Mitigation: Use a dedicated workspace and remove or prune retained source and review files when they are no longer needed. <br>
Risk: PDF parsing and image processing dependencies may need security updates. <br>
Mitigation: Install the skill in a dedicated virtual environment and keep Pillow and PyMuPDF patched. <br>
Risk: Zotero finalization can touch a local Zotero library. <br>
Mitigation: Use the no-Zotero path when the workflow should not modify Zotero. <br>


## Reference(s): <br>
- [README_EN.md](README_EN.md) <br>
- [Quality Contract](references/quality-contract.md) <br>
- [Document Routing](references/routing.md) <br>
- [Layout and Readability](references/layout-readability.md) <br>
- [Translation Scope](references/translation-scope.md) <br>
- [Semantic Review](references/semantic-review.md) <br>
- [QA and Acceptance](references/qa-acceptance.md) <br>
- [Validation Scope](references/validation.md) <br>
- [Workspace and Output Specification](references/workspace.md) <br>
- [JGLUE Source Example](https://www.jstage.jst.go.jp/article/jnlp/30/1/30_63/_article/-char/en) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with shell commands, workspace files, review reports, and searchable translated PDF outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates per-batch Workspace input, output, and hidden work directories; formal delivery is accepted translated PDFs with paths and hashes.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
