## Description: <br>
Extract management guidance and forward-looking statements from SEC 10-K/10-Q filings using a local RAG pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinghao0724](https://clawhub.ai/user/tinghao0724) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and analysts use this skill to query indexed SEC 10-K/10-Q filings for management guidance, outlook, risk factors, and forward-looking statements with cited source files, pages, and filing dates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper imports and executes modules from the SEC_PIPELINE_DIR location. <br>
Mitigation: Set SEC_PIPELINE_DIR only to a local SEC RAG pipeline directory that you trust and maintain. <br>
Risk: The external pipeline may download, index, and store SEC filings locally. <br>
Mitigation: Use storage locations and retention practices appropriate for the filings and analysis environment. <br>
Risk: Generated guidance answers may be incomplete or misleading if retrieval or generation misses filing context. <br>
Mitigation: Review the cited source files, pages, and filing dates before relying on extracted guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tinghao0724/skills/sec-guidance) <br>
- [Project homepage](https://github.com/TINGHAO0724/sec-guidance-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown-style guidance with inline bash commands; extractor output is plain text with numbered citations and source lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SEC_PIPELINE_DIR and a trusted local SEC RAG pipeline with an indexed Elasticsearch corpus.] <br>

## Skill Version(s): <br>
0.1.0 (source: frontmatter and changelog, released 2026-07-26) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
