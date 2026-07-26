## Description: <br>
TaoHtml turns initial ideas, Word/PDF source material, existing slides, and HTML into polished 16:9 offline HTML reports and presentation-ready decks as a high-design alternative to PPT/PPTX. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[taogeo](https://clawhub.ai/user/taogeo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external creators, and developers use TaoHtml to turn ideas, source documents, existing slides, or HTML into portable offline reports and presentation-ready decks with structured intake, visual-system selection, browser QA, and a verification handoff. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local scripts process supplied documents and images, and browser QA uses Playwright/Chromium. <br>
Mitigation: Run the skill in a trusted workspace, review supplied files before processing, and keep runtime dependencies patched, especially Pillow. <br>
Risk: Reusable corporate-template storage can mix sensitive client branding if shared carelessly. <br>
Mitigation: Set TAOHTML_HOME per client or workspace and archive profiles that should not be reused. <br>
Risk: The Report IR and compiler path is marked as an experimental pilot path in the artifact. <br>
Mitigation: Use direct HTML for normal customer work and enter Report IR only when explicitly authorized. <br>


## Reference(s): <br>
- [TaoHtml Skill Definition](artifact/SKILL.md) <br>
- [Runtime Contract](artifact/references/runtime-contract.md) <br>
- [Content Editor Contract](artifact/references/content-editor.md) <br>
- [PPT-Like Report Building Playbook](artifact/references/process-playbook.md) <br>
- [Production Authorization](artifact/references/production-authorization.md) <br>
- [Project Handoff](artifact/references/project-handoff.md) <br>
- [Visual Systems](artifact/references/visual-systems.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance plus generated HTML/CSS/JavaScript files, JSON handoff or QA records, and shell commands.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces offline 16:9 HTML reports and decks; editor changes export as a new HTML file and may require an accompanying assets package.] <br>

## Skill Version(s): <br>
0.5.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
