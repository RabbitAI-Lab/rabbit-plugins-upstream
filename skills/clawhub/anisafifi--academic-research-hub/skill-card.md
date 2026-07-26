## Description: <br>
Searches academic papers across arXiv, PubMed, and Semantic Scholar, with options to download PDFs, collect metadata, and export citations or bibliographies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anisafifi](https://clawhub.ai/user/anisafifi) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
Researchers, students, and developers use this skill to search scholarly sources, retrieve paper metadata, download available PDFs, and produce bibliography exports for literature reviews or reference-library workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries are sent to external academic services. <br>
Mitigation: Avoid submitting confidential or sensitive queries unless the user accepts the external-service exposure. <br>
Risk: The skill can download PDFs or write citation and search-result exports to disk. <br>
Mitigation: Use a dedicated project folder and review output paths before running download or export commands. <br>
Risk: Some documented options may not work in the current script version. <br>
Mitigation: Confirm supported flags with the script help output and treat failed options as feature gaps rather than research results. <br>


## Reference(s): <br>
- [Academic Research Hub documentation](references/readme.md) <br>
- [ClawHub skill page](https://clawhub.ai/anisafifi/skills/academic-research-hub) <br>
- [arXiv API](https://arxiv.org/help/api) <br>
- [PubMed API](https://www.ncbi.nlm.nih.gov/books/NBK25501/) <br>
- [Semantic Scholar API](https://api.semanticscholar.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands; generated research results may be text, JSON, BibTeX, RIS, Markdown, or downloaded PDF files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on source availability, selected filters, requested format, and user-directed download or export paths.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
