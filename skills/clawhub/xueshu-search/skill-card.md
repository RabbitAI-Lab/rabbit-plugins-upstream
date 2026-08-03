## Description: <br>
Academic literature search for Chinese and English queries across arXiv, Semantic Scholar, PubMed, CrossRef, and Baidu Scholar, with citation tracking, author search, DOI lookup, BibTeX export, and summary prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fly869](https://clawhub.ai/user/fly869) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to retrieve and synthesize academic literature for Chinese and English queries, including source routing, citation and reference lookup, DOI resolution, BibTeX export, and summary prompt generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search terms are sent to selected external academic providers, and optional provider API keys may be used for Baidu Scholar or Semantic Scholar integrations. <br>
Mitigation: Use organization-approved providers, avoid sensitive internal project names or regulated research topics unless permitted, and configure optional API keys only for intended integrations. <br>
Risk: Provider results can be incomplete, rate-limited, stale, or missing fields, and generated literature summaries may overstate the evidence. <br>
Mitigation: Review source links and DOI records before relying on results, preserve provider attribution, and treat summaries as drafts for human review. <br>


## Reference(s): <br>
- [Commands Reference](references/commands.md) <br>
- [Field Mapping](references/field-mapping.md) <br>
- [Routing Guide](references/routing-guide.md) <br>
- [arXiv API User Manual](https://info.arxiv.org/help/api/user-manual.html) <br>
- [Semantic Scholar Graph API](https://api.semanticscholar.org/api-docs/graph) <br>
- [PubMed E-utilities](https://www.ncbi.nlm.nih.gov/books/NBK25501/) <br>
- [CrossRef API](https://api.crossref.org/swagger-ui/index.html) <br>
- [Baidu Qianfan Baidu Scholar API](https://cloud.baidu.com/doc/qianfan/s/Amkw9qpzd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [JSON search results, BibTeX for DOI export, and Markdown summary prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output can include source, id, title, authors, abstract, year, DOI, URL, PDF URL, citation count, venue, and categories; Baidu Scholar results can include aiAbstract.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
