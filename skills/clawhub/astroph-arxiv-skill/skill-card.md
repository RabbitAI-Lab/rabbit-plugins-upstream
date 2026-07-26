## Description: <br>
Queries arXiv filtering by astro-ph, extracting full abstracts, authors, and PDF links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jorgeanais](https://clawhub.ai/user/jorgeanais) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to find recent astronomy and astrophysics papers on arXiv for a requested topic, with formatted titles, authors, dates, abstracts, and PDF links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes live network requests to arXiv using the user's research topic. <br>
Mitigation: Tell users that their query terms are sent to arXiv and avoid using sensitive or private topics in searches. <br>
Risk: The generated fetch script relies on a constructed URL for the external request. <br>
Mitigation: Validate that generated requests use the arXiv query endpoint before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jorgeanais/skills/astroph-arxiv-skill) <br>
- [arXiv API Query Endpoint](https://export.arxiv.org/api/query) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, guidance] <br>
**Output Format:** [Markdown-formatted literature search results with generated Python fetch-and-parse code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defaults to two papers when the user does not specify a result count and includes full arXiv summaries, author lists, dates, abstract links, and PDF links.] <br>

## Skill Version(s): <br>
0.1.5 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
