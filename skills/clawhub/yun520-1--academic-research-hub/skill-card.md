## Description: <br>
Searches academic databases such as arXiv, PubMed, and Semantic Scholar to retrieve papers, citations, bibliographies, and research metadata. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yun520-1](https://clawhub.ai/user/yun520-1) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and agents supporting literature reviews use this skill to find papers, download available PDFs, gather metadata, and export citations or bibliographies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to public academic services. <br>
Mitigation: Avoid confidential queries unless disclosure to those services is acceptable. <br>
Risk: Downloaded PDFs or generated citation files may be reused without sufficient review. <br>
Mitigation: Review downloaded files and citations before sharing, publishing, or incorporating them into downstream work. <br>
Risk: Python dependencies and output downloads can affect the local environment. <br>
Mitigation: Install dependencies in a virtual environment, keep them updated or pinned to patched versions, and write outputs to a dedicated workspace folder. <br>


## Reference(s): <br>
- [Academic Research Hub on ClawHub](https://clawhub.ai/yun520-1/skills/academic-research-hub) <br>
- [arXiv API documentation](https://arxiv.org/help/api) <br>
- [PubMed E-utilities documentation](https://www.ncbi.nlm.nih.gov/books/NBK25501/) <br>
- [Semantic Scholar API documentation](https://api.semanticscholar.org/) <br>
- [Skill readme](references/readme.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional text, JSON, BibTeX, RIS, or Markdown research outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save search results, citation files, and downloaded PDFs to user-selected output paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
