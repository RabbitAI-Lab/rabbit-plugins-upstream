## Description: <br>
Automatically scrape, process, and generate daily news digests from Chinese news sources, covering industry dynamics, policy updates, economy, technology, energy, and pricing information with source attribution and original links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zigu-creator](https://clawhub.ai/user/zigu-creator) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, developers, and analysts use this skill to configure and run a Chinese news monitoring pipeline that scrapes selected sources, filters and deduplicates articles, optionally summarizes them with an LLM, and writes daily digest outputs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to configured news sites and stores scraped article text in a local SQLite database. <br>
Mitigation: Review and limit configured sources before running the pipeline, set NEWS_DIGEST_DB to an expected local path, and periodically delete or rotate retained database content. <br>
Risk: Optional LLM summarization can send article snippets to an external model endpoint when LLM environment variables are configured. <br>
Mitigation: Leave NEWS_DIGEST_LLM_API_KEY and NEWS_DIGEST_LLM_BASE_URL unset unless external summarization is approved for the articles being processed. <br>
Risk: Digest files are written to the workspace and Desktop, which may expose collected news summaries to local users or syncing tools. <br>
Mitigation: Run the skill in a workspace with appropriate local access controls and review generated digest files before sharing or automating delivery. <br>
Risk: The security evidence notes weakened TLS behavior and a missing stage2_6_fgb module that may affect authenticity checks or scheduled execution. <br>
Mitigation: Test the full pipeline before scheduling it and review the TLS fallback behavior before relying on fetched content authenticity. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text digest files with source titles, summaries, publication dates, and original links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes .news-digest-out.md in the workspace and timestamped Chinese digest text files to the Desktop; optional LLM summaries require NEWS_DIGEST_LLM_API_KEY and NEWS_DIGEST_LLM_BASE_URL.] <br>

## Skill Version(s): <br>
1.0.23 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
