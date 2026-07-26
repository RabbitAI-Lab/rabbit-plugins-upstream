## Description: <br>
Local hybrid search for markdown notes and docs. Use when searching notes, finding related content, or retrieving documents from indexed collections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[lifecoacher](https://clawhub.ai/user/lifecoacher) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use this skill to search local Markdown notes, documentation, and knowledge bases with qmd keyword, semantic, and hybrid search commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can index local Markdown content, including private notes if broad folders are added. <br>
Mitigation: Add only narrow Markdown folders that are intended for search, and avoid indexing broad private directories. <br>
Risk: Semantic search may download local model files on first use. <br>
Mitigation: Use semantic search only when acceptable for the environment, and prefer qmd search for routine keyword lookup. <br>
Risk: Cron or scheduler examples can create ongoing background re-indexing. <br>
Mitigation: Enable scheduled qmd update or embed commands only when continuous indexing is desired. <br>


## Reference(s): <br>
- [Qmd GitHub repository](https://github.com/tobi/qmd) <br>
- [Qmd ClawHub skill page](https://clawhub.ai/lifecoacher/skills/qmd-skill-2) <br>
- [lifecoacher ClawHub publisher profile](https://clawhub.ai/user/lifecoacher) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON-producing qmd commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides the agent to prefer fast BM25 search, use semantic search selectively, retrieve Markdown files, and maintain qmd indexes.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
