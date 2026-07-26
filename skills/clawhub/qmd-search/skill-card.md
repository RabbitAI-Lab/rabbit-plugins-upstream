## Description: <br>
Fast local search for markdown files, notes, and docs using the qmd CLI, combining keyword search, semantic search, and reranking on local collections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bheemreddy181](https://clawhub.ai/user/bheemreddy181) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, engineers, and documentation-heavy teams use this skill to find files, code, notes, and relevant snippets in qmd-indexed local collections before answering questions or making changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can index and retrieve local files, which may expose sensitive files, secrets, or private repository content through search results. <br>
Mitigation: Install qmd only from a trusted source, keep qmd collections narrowly scoped, and exclude sensitive directories or files before indexing and searching. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bheemreddy181/skills/qmd-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline qmd shell commands and references to qmd text, markdown, or JSON results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include local file paths, scores, snippets, full document content, or line-specific excerpts depending on qmd flags.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
