## Description: <br>
TaoHtml helps agents turn ideas, Word/PDF files, slides, or HTML into polished offline 16:9 HTML reports and presentation-ready decks with guided structure, visual design, QA, and handoff. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[taogeo](https://clawhub.ai/user/taogeo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents, developers, and report producers use TaoHtml to plan, design, generate, QA, and hand off offline HTML reports and decks from ideas or bound source materials while preserving evidence and verification boundaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local file processing, browser QA, and PDF/image parsing may expose sensitive source material to the installation environment. <br>
Mitigation: Install only in environments where local document processing and browser QA are acceptable, and bind only intended source files. <br>
Risk: Corporate templates or screenshots may be persisted through the TaoHtml profile store. <br>
Mitigation: Review ~/.taohtml or TAOHTML_HOME profile-store behavior before using sensitive corporate templates or screenshots. <br>
Risk: Outdated parsing dependencies can increase exposure when handling untrusted files. <br>
Mitigation: Ensure dependencies, especially Pillow, resolve to patched versions before processing untrusted files. <br>


## Reference(s): <br>
- [TaoHtml Skill Page](https://clawhub.ai/taogeo/skills/taohtml) <br>
- [Runtime Contract](references/runtime-contract.md) <br>
- [Process Playbook](references/process-playbook.md) <br>
- [Visual Systems](references/visual-systems.md) <br>
- [Static Reference VI](references/static-reference-vi.md) <br>
- [Project Handoff](references/project-handoff.md) <br>
- [Content Editor Contract](references/content-editor.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files] <br>
**Output Format:** [Markdown guidance with generated HTML/CSS/JavaScript files, JSON handoff records, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces offline 16:9 HTML report/deck artifacts with QA and verification handoff; may use bundled scripts for validation and packaging.] <br>

## Skill Version(s): <br>
0.5.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
