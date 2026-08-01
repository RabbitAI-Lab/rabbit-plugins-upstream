## Description: <br>
Formats, validates, and adds grayscale diagrams to Word .docx consulting reports using configuration-driven layouts for due diligence, risk assessment, tax risk, and financial analysis deliverables. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hiwikibk](https://clawhub.ai/user/hiwikibk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Consultants, analysts, and document-preparation agents use this skill to normalize client-facing Word reports, apply consistent black/gray/white styling, insert supported diagrams, and produce a format compliance checklist before delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The installer can fetch or update code from an external Git repository and install external Python or Node toolchains. <br>
Mitigation: Review the installer before execution, prefer the reviewed artifact over remote installation, and pin Python and npm dependencies in a controlled environment. <br>
Risk: Optional Mermaid diagram rendering relies on a Node/Chromium toolchain and should only process trusted diagram input. <br>
Mitigation: Use the structured Python renderer by default, and reserve Mermaid rendering for trusted diagram specifications when the additional toolchain is explicitly needed. <br>


## Reference(s): <br>
- [Formatting Standards](references/formatting_standards.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/hiwikibk/skills/word-formatter) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Word .docx files, PNG diagrams, Markdown validation checklists, and concise command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces new output files without overwriting the input document by default.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
