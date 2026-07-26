## Description: <br>
Search, download, and summarize academic papers from arXiv. Built for AI/ML researchers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ractorrr](https://clawhub.ai/user/ractorrr) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Researchers, students, developers, security professionals, and content creators use this skill to search arXiv, retrieve paper metadata, download PDFs, and track reading lists for literature review and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Optional MongoDB tracking stores saved paper metadata and reading status. <br>
Mitigation: Use a dedicated low-privilege database and configure MongoDB only when paper tracking is required. <br>
Risk: PDF downloads write files to a local directory. <br>
Mitigation: Choose the download directory deliberately and review downloaded files before opening or sharing them. <br>
Risk: Unpinned dependency ranges can reduce install reproducibility. <br>
Mitigation: Pin dependency versions in deployment environments that require repeatable builds. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ractorrr/skills/arxiv) <br>
- [arXiv API documentation](https://arxiv.org/help/api) <br>
- [Publisher profile](https://clawhub.ai/user/ractorrr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI examples, plain text summaries, optional JSON responses, and downloaded PDF files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call the arXiv API, write PDFs to a configured local directory, and optionally store paper metadata and reading status in MongoDB.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
