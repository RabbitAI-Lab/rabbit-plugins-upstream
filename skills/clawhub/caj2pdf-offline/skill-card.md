## Description: <br>
将知网 CAJ / KDH / NH 文献高保真转换为 PDF（保留文字层可选中 + 目录书签）。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[j-levee](https://clawhub.ai/user/j-levee) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, librarians, and agents assisting them use this skill to convert local CNKI CAJ, KDH, and NH documents into PDF files while preserving the original files. It supports single-file and batch conversion, with fallback guidance when a format cannot be converted reliably. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The converter may create its own Python environment and install dependencies from a third-party PyPI mirror. <br>
Mitigation: Run setup only in an environment where that dependency installation path is acceptable, and review the isolated environment before using it on sensitive documents. <br>
Risk: The skill extracts embedded closed-source Windows DLLs at runtime for document decoding. <br>
Mitigation: Use it only on trusted local systems and documents where the embedded DLL behavior is acceptable. <br>
Risk: Optional context-menu installation can modify Windows registry settings. <br>
Mitigation: Avoid the install/context-menu command unless Windows registry integration is explicitly desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/j-levee/skills/caj2pdf-offline) <br>
- [CNKI](http://cnki.net/) <br>
- [CAJViewer](http://cajviewer.cnki.net/) <br>
- [MuPDF](https://mupdf.com/index.html) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Guidance] <br>
**Output Format:** [PDF files with terminal status summaries and Markdown-style fallback guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Successful conversions create same-name PDF files unless an output directory is specified; failures are reported per input file.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
