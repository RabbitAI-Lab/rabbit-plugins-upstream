## Description: <br>
Conduct structured literature reviews with systematic search and synthesis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, and technical writers use this skill to retrieve public academic papers, rank and cluster results, and draft structured literature reviews for a specified research topic. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research topics and retrieved paper metadata are sent to public academic services during search. <br>
Mitigation: Use only non-confidential topics or run the skill in an environment where calls to Semantic Scholar, arXiv, and CrossRef are acceptable. <br>
Risk: Optional LLM polishing can send draft content and paper summaries to the configured LLM provider. <br>
Mitigation: Keep LLM polishing disabled for confidential work unless the configured provider and API endpoint are approved. <br>
Risk: Dependencies are specified with lower bounds rather than a locked set. <br>
Mitigation: Review and pin dependency versions before using the skill in sensitive or production environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/lit-review) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>
- [Semantic Scholar Graph API](https://api.semanticscholar.org/graph/v1/paper/search) <br>
- [arXiv API](http://export.arxiv.org/api/query) <br>
- [CrossRef Works API](https://api.crossref.org/works) <br>
- [README.md](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, files] <br>
**Output Format:** [Markdown review text, optional Markdown and BibTeX files, and command-line status JSON] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs summarize retrieved paper metadata, topic clusters, research trends, and references; optional LLM polishing can change wording when configured.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
