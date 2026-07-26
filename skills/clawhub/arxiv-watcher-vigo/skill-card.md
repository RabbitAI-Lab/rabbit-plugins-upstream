## Description: <br>
Search and summarize papers from ArXiv for latest research, specific topics, or daily AI paper summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and research-focused agents use this skill to find recent ArXiv papers by query, summarize abstracts, and keep a local log of papers discussed. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may retain paper titles, links, authors, dates, and summaries in a local research log. <br>
Mitigation: Avoid confidential research topics unless this retention is acceptable, and review or clear memory/RESEARCH_LOG.md when needed. <br>
Risk: ArXiv search results and summaries can be incomplete, stale, or unavailable depending on the external API and paper content. <br>
Mitigation: Verify important findings against the linked ArXiv record or PDF before relying on them. <br>


## Reference(s): <br>
- [ArXiv API query endpoint](https://export.arxiv.org/api/query) <br>
- [ClawHub skill page](https://clawhub.ai/rubenfb23/skills/arxiv-watcher-vigo) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Markdown summaries with ArXiv links and optional local research-log entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May append discussed paper title, authors, date, link, and summary to memory/RESEARCH_LOG.md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
