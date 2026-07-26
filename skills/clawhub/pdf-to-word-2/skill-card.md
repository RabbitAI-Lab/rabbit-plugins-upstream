## Description: <br>
Convert PDF to Word (.docx) via Foxit PhantomPDF/PDF Editor keyboard automation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qiaohuaruan](https://clawhub.ai/user/qiaohuaruan) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users use this skill to convert PDFs into DOCX files on Windows by driving Foxit PhantomPDF or Foxit PDF Editor through documented keyboard automation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Desktop automation sends keystrokes to Foxit and temporarily uses the clipboard. <br>
Mitigation: Run the skill only when Foxit is expected to be the active window, avoid interacting with the machine during conversion, and review clipboard handling expectations before use. <br>
Risk: The referenced PowerShell conversion script is not included in the artifact. <br>
Mitigation: Confirm the script is available from the trusted source provenance before attempting automated conversion. <br>
Risk: The workflow depends on Windows and Chinese-language Foxit menu shortcuts. <br>
Mitigation: Use the skill only in a matching Windows/Foxit environment and validate shortcut behavior with a non-sensitive test PDF first. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/qiaohuaruan/skills/tree/main/pdf-to-word) <br>
- [ClawHub skill listing](https://clawhub.ai/qiaohuaruan/skills/pdf-to-word-2) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with PowerShell command examples and workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Windows-focused Foxit automation guidance for Chinese-language menu shortcuts; no executable script is bundled in the artifact.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
