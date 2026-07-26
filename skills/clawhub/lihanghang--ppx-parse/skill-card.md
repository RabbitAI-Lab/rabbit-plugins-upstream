## Description: <br>
Parse PDFs and images into Markdown/JSON using the `ppx` CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lihanghang](https://clawhub.ai/user/lihanghang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to run local PPX document parsing on user-selected PDFs and images, including OCR for scanned files and table extraction when needed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: PPX may process user-selected documents that contain sensitive content. <br>
Mitigation: Run parsing only on documents the user chooses and prefer the local default pipeline when backend processing is not required. <br>
Risk: LLM table parsing can send document content to a configured backend or use an API key. <br>
Mitigation: Review backend URLs and API keys before enabling LLM table parsing, and use the default table mode unless higher table fidelity is requested. <br>
Risk: Python package installation can affect the active runtime environment. <br>
Mitigation: Install PPX and related dependencies in a dedicated Python 3.12 or newer virtual environment. <br>
Risk: Parsing failures or partial output can lead to incomplete extraction results. <br>
Mitigation: Validate that the output directory contains doc.md, doc.json, and pages/, and report partial results explicitly. <br>
Risk: The version-sync maintenance script edits skill package metadata. <br>
Mitigation: Use the version-sync script only when maintaining the skill package itself. <br>


## Reference(s): <br>
- [PPX project homepage](https://github.com/memect/memect-ppx) <br>
- [CLI Options](references/cli-options.md) <br>
- [Backend Config](references/backend-config.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and file path references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports the absolute output directory and identifies whether results came from doc.md, doc.json, or page-level files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
