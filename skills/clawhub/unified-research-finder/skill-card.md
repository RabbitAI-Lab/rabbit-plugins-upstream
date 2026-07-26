## Description: <br>
Unified Research Finder helps agents search academic literature across PubMed and Google Scholar-style sources, merge results, deduplicate records, and report only verifiable findings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[georgechou17](https://clawhub.ai/user/georgechou17) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, students, clinicians, and other external users can ask an agent to find scholarly literature, PubMed records, citations, abstracts, DOI links, and available full-text links across biomedical and general academic sources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research queries may be sent to PubMed, Google Scholar, and multiple mirror domains. <br>
Mitigation: Use non-sensitive queries, tell users which external sources are being queried, and prefer a single-source mode when a user needs tighter control over where a query is sent. <br>
Risk: An NCBI API key could be exposed if a user pastes it into chat. <br>
Mitigation: Store the key in a local environment variable or another secret mechanism, avoid echoing it in conversation, and rotate any key that has already been shared. <br>
Risk: Mirror availability, blocking, or anti-bot pages can produce incomplete search coverage. <br>
Mitigation: Report source failures clearly, do not fabricate missing literature, and ask the user whether to retry later or use the documented browser fallback. <br>


## Reference(s): <br>
- [Unified Research Finder release page](https://clawhub.ai/georgechou17/skills/unified-research-finder) <br>
- [Publisher profile](https://clawhub.ai/user/georgechou17) <br>
- [PubMed query syntax](references/pubmed-query-syntax.md) <br>
- [NCBI API key registration guide](references/register-api-key.md) <br>
- [Scholar source technical reference](references/scholar-sources.md) <br>
- [NCBI account signup](https://account.ncbi.nlm.nih.gov/signup/) <br>
- [NCBI account settings](https://www.ncbi.nlm.nih.gov/account/settings/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown summaries with source links and optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results are expected to be based on live PubMed and Scholar-source responses; no result should be fabricated when sources fail or return no matches.] <br>

## Skill Version(s): <br>
v1.1.1 (source: frontmatter and server release evidence, released 2026-07-24) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
