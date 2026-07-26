## Description: <br>
Search and summarize papers from ArXiv. Use when the user asks for the latest research, specific topics on ArXiv, or a daily summary of AI papers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rubenfb23](https://clawhub.ai/user/rubenfb23) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Researchers, developers, and other external users use this skill to find recent ArXiv papers by topic, author, category, or paper ID, summarize abstracts, and maintain a local research log of discussed papers. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill records titles, authors, links, and summaries of papers discussed in memory/RESEARCH_LOG.md, which may expose sensitive research interests if the log is shared. <br>
Mitigation: Review the research log before sharing the workspace and clear entries for sensitive topics. <br>
Risk: The search helper performs shell-based network access to the ArXiv API. <br>
Mitigation: Inspect scripts/search_arxiv.sh and run the skill only in environments where outbound access to export.arxiv.org is acceptable. <br>


## Reference(s): <br>
- [ArXiv API endpoint](https://export.arxiv.org/api/query) <br>
- [ClawHub skill page](https://clawhub.ai/rubenfb23/skills/arxiv-watcher) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, files, guidance] <br>
**Output Format:** [Markdown research summaries and RESEARCH_LOG.md entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query the ArXiv API through a shell script and fetch PDF details when requested.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
