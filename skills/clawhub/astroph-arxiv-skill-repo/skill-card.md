## Description: <br>
Searches recent astro-ph papers on arXiv and formats titles, authors, dates, abstracts, and links for review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jorgeanais](https://clawhub.ai/user/jorgeanais) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and technical readers use this skill to search recent astrophysics literature on arXiv and receive formatted paper metadata, abstracts, and PDF links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to arXiv's public API and may reveal private research interests or unpublished ideas. <br>
Mitigation: Avoid confidential project details, personal identifiers, or sensitive unpublished concepts in queries unless sharing them with arXiv is acceptable. <br>
Risk: The skill may create a temporary local Python parser script while fetching and formatting results. <br>
Mitigation: Run it in a trusted workspace, review generated commands or scripts before execution, and remove temporary files after use when needed. <br>


## Reference(s): <br>
- [arXiv API query endpoint](https://export.arxiv.org/api/query) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Guidance] <br>
**Output Format:** [Markdown literature-search results with links, author lists, dates, and blockquoted abstracts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to two results when no limit is specified and includes abstract and PDF links for each paper.] <br>

## Skill Version(s): <br>
0.1.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
