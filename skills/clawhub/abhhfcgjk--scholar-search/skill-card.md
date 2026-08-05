## Description: <br>
Search academic papers with Semantic Scholar and arXiv, dedupe results, and export JSON plus BibTeX citations for literature reviews, references, or citation gathering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[abhhfcgjk](https://clawhub.ai/user/abhhfcgjk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and agents use this skill to search academic literature via Semantic Scholar and arXiv, deduplicate results, and export JSON and BibTeX citations for literature reviews or reference gathering. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install Python dependencies before use. <br>
Mitigation: Review the dependency list and install in an appropriate Python environment before running the helper script. <br>
Risk: The skill makes outbound requests to Semantic Scholar, arXiv, and doi.org. <br>
Mitigation: Run it only where those network calls are acceptable, and provide SEMANTIC_SCHOLAR_API_KEY only through the environment when higher rate limits are needed. <br>
Risk: The skill writes JSON and BibTeX files to paths chosen in the command. <br>
Mitigation: Choose output paths deliberately and review generated citation files before using them in downstream work. <br>


## Reference(s): <br>
- [Semantic Scholar API](https://www.semanticscholar.org/product/api) <br>
- [Semantic Scholar Graph API paper search](https://api.semanticscholar.org/graph/v1/paper/search) <br>
- [arXiv API query endpoint](https://export.arxiv.org/api/query) <br>
- [DOI content negotiation endpoint](https://doi.org) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, BibTeX] <br>
**Output Format:** [Markdown guidance with shell commands; generated JSON and BibTeX files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes output files to user-selected paths and can optionally use SEMANTIC_SCHOLAR_API_KEY for higher Semantic Scholar rate limits.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
