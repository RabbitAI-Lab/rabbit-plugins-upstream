## Description: <br>
Local hybrid search for Markdown notes and docs, used to search notes, find related content, and retrieve documents from indexed collections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levineam](https://clawhub.ai/user/levineam) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and knowledge workers use this skill to let an agent search selected local Markdown note, documentation, or knowledge-base collections and retrieve matching documents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can index local Markdown notes that may contain sensitive information. <br>
Mitigation: Add only narrow, intentional Markdown folders as qmd collections, and avoid indexing sensitive notes unless agent search over them is desired. <br>
Risk: The optional re-indexing cron job can keep processing local files in the background. <br>
Mitigation: Enable the cron job only when ongoing background re-indexing is intended, and review the command, schedule, and collection scope before enabling it. <br>
Risk: The skill depends on the upstream qmd command-line tool. <br>
Mitigation: Install and use the qmd tool only when the upstream project is trusted for the target environment. <br>
Risk: Semantic and hybrid search modes may be slow on cold start. <br>
Mitigation: Use BM25 search as the default path, and reserve vsearch or query for cases where keyword search is insufficient and latency is acceptable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/levineam/skills/qmd-external) <br>
- [Publisher profile](https://clawhub.ai/user/levineam) <br>
- [qmd project homepage](https://github.com/tobi/qmd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON-producing command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance favors fast BM25 search first, with slower semantic and hybrid commands only when needed.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
