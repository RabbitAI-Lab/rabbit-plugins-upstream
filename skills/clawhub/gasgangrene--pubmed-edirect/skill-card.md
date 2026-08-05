## Description: <br>
Search and retrieve literature from PubMed using NCBI's EDirect command-line tools. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and analysts use this skill to search PubMed and other NCBI databases, retrieve records, extract structured literature metadata, and build repeatable command-line research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Manual EDirect installation may execute external installer code, modify PATH, and require local dependencies. <br>
Mitigation: Download installers from the official NCBI source, review scripts before execution, avoid piping remote scripts directly to a shell, and validate installation in a dedicated workspace or test environment. <br>
Risk: EDirect commands contact NCBI services and can write local research outputs. <br>
Mitigation: Run examples from a dedicated workspace, use explicit output filenames, monitor API/network usage, and configure NCBI_API_KEY and NCBI_EMAIL according to NCBI usage expectations. <br>
Risk: Batch searches can hit rate limits or create retained local copies of sensitive research results. <br>
Mitigation: Use result limits, delays, and approved API keys where appropriate, and clean or relocate generated files when results should not be retained. <br>


## Reference(s): <br>
- [ClawHub skill release](https://clawhub.ai/gasgangrene/skills/pubmed-edirect) <br>
- [NCBI EDirect official documentation](https://www.ncbi.nlm.nih.gov/books/NBK179288/) <br>
- [NCBI EDirect installer script](https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh) <br>
- [PubMed Help](https://pubmed.ncbi.nlm.nih.gov/help/) <br>
- [NCBI E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) <br>
- [MeSH Database](https://www.ncbi.nlm.nih.gov/mesh/) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Code, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown with inline bash code blocks and file-output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to run local EDirect commands that produce text, XML, CSV, RIS, TSV, or per-record output files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
