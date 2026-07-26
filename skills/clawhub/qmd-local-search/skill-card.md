## Description: <br>
qmd Local Search helps agents use the local qmd CLI to search indexed markdown, notes, docs, and code with keyword, semantic, and reranked queries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bheemreddy181](https://clawhub.ai/user/bheemreddy181) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to discover files, search local notes or documentation, gather code context, and retrieve scoped file excerpts from qmd collections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents to index or retrieve local files, which may expose sensitive directories if collections are scoped too broadly. <br>
Mitigation: Limit qmd collections to intended folders, avoid indexing sensitive directories unless necessary, and use line or byte limits when retrieving files. <br>
Risk: The qmd CLI and local model downloads are external runtime dependencies. <br>
Mitigation: Install only when the publisher, qmd CLI, and model download source are trusted. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with qmd CLI command examples and supported result formats.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [qmd results can include file paths, snippets, JSON, Markdown, full documents, or line-limited file extracts depending on the selected command flags.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
