## Description: <br>
Extract management guidance and forward-looking statements from SEC 10-K/10-Q filings. Self-contained by default (fetches from EDGAR, in-memory BM25, Claude/OpenAI). Optional heavy mode delegates to a local RAG pipeline. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tinghao0724](https://clawhub.ai/user/tinghao0724) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent users use this skill to retrieve the latest SEC 10-K or 10-Q for a ticker and extract management guidance, outlook, forward-looking statements, and risk-factor content with citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected SEC filing excerpts and user questions may be sent to Anthropic or OpenAI. <br>
Mitigation: Confirm the data-sharing posture is acceptable before use, and choose the provider and model through approved API credentials and configuration. <br>
Risk: Heavy mode delegates retrieval and answer generation to code loaded from SEC_PIPELINE_DIR. <br>
Mitigation: Set SEC_PIPELINE_DIR only to a trusted local pipeline and review that pipeline before enabling heavy mode. <br>
Risk: The requests dependency is specified as a broad lower bound. <br>
Mitigation: Pin or override requests to a current patched version in production environments. <br>


## Reference(s): <br>
- [sec-guidance on ClawHub](https://clawhub.ai/tinghao0724/skills/sec-guidance) <br>
- [Project homepage](https://github.com/TINGHAO0724/sec-guidance-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [Markdown-style terminal text with inline citation markers and source lists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Caches public filing text locally under ~/.cache/sec-guidance/ for repeat runs.] <br>

## Skill Version(s): <br>
0.2.0 (source: frontmatter, changelog, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
