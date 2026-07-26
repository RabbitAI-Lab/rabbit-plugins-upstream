## Description: <br>
Convert Markdown files to PDF, DOCX, or HTML with advanced formatting, Mermaid diagrams, custom fonts, and table of contents support. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuanpmt](https://clawhub.ai/user/tuanpmt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and document authors use Mxe to convert Markdown files or web articles into PDF, DOCX, HTML, or clipboard-ready Markdown with formatting options such as Mermaid diagrams, table of contents, bookmarks, custom fonts, and CSS. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup flow builds and globally links unreviewed local or external Node tooling. <br>
Mitigation: Install only after inspecting and trusting the actual mxe project at the referenced local path, or replace the setup with a reviewed, pinned package. <br>
Risk: URL inputs can trigger outbound web requests. <br>
Mitigation: Use trusted URLs and review network access expectations before running conversions. <br>
Risk: Local images referenced by Markdown may be embedded into exported documents. <br>
Mitigation: Review local image paths and document contents before exporting or sharing generated files. <br>


## Reference(s): <br>
- [Mxe on ClawHub](https://clawhub.ai/tuanpmt/skills/mxe) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide an agent to produce PDF, DOCX, HTML, or clipboard Markdown through the local mxe command.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
