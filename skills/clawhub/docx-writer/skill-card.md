## Description: <br>
Generates academic-standard Word documents with native footnotes, styled text, tables, and images using bayoo-docx and lxml. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomuiv](https://clawhub.ai/user/tomuiv) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and academic writers use this skill to create Chinese academic Word documents that require strict layout rules, native footnotes, styled headings, tables, and images. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The generated Python workflow writes a Word document to the configured output path and reads template or image paths from local configuration. <br>
Mitigation: Review OUTPUT, TEMPLATE, and FIG_DIR before running the script, and run it only in a workspace where those file reads and writes are intended. <br>
Risk: The security guidance says to install only when the publisher and workflow are trusted. <br>
Mitigation: Review the artifact files and intended document-generation workflow before installation or execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomuiv/skills/docx-writer) <br>
- [Artifact README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>
- [Document generation script](artifact/scripts/build_docx.py) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions, Files] <br>
**Output Format:** [Markdown guidance with Python code examples and generated .docx files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires bayoo-docx, lxml, and a Word template containing native footnote styles.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
