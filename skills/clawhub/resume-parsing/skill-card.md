## Description: <br>
Parses PDF/DOCX resumes (CV, \u7b80\u5386) into structured JSON Resume standard data using the pdfmuse deterministic extraction engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[casperkwok](https://clawhub.ai/user/casperkwok) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, recruiting operations teams, and agents use this skill to convert one resume or a folder of resumes into structured JSON Resume data, human-readable summaries, and batch candidate indexes. It supports English and Chinese resumes and keeps parser traceability for layout warnings and source files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The extraction script installs the latest pdfmuse package on first run, which may change behavior over time. <br>
Mitigation: Use a controlled environment and preinstall a reviewed, pinned pdfmuse version before processing resumes. <br>
Risk: Resume parsing writes extracted Markdown, JSON sidecars, JSON Resume files, summaries, and CSV indexes that can contain sensitive personal data. <br>
Mitigation: Process only resumes with appropriate consent, restrict output directory access, and apply a clear retention and deletion policy. <br>
Risk: Multi-column resumes or parser warnings can scramble reading order and affect timeline mapping. <br>
Mitigation: Review the sidecar warnings and cross-check affected resumes against the source document before using the parsed candidate data. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/casperkwok/skills/resume-parsing) <br>
- [Publisher profile](https://clawhub.ai/user/casperkwok) <br>
- [JSON Resume](https://jsonresume.org) <br>
- [pdfmuse](https://pypi.org/project/pdfmuse/) <br>
- [JSON Resume schema and mapping rules](reference/schema.md) <br>
- [Mapping examples](examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON Resume files, Markdown summaries, CSV batch indexes, extraction sidecar JSON, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include local files containing resume personal data; batch runs produce one row per candidate in index.csv.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
