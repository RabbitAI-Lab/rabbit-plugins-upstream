## Description: <br>
Search markdown knowledge bases efficiently using qmd to find relevant content from Obsidian vaults or markdown collections with minimal token usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anshumanbh](https://clawhub.ai/user/anshumanbh) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use this skill to search local markdown knowledge bases and return relevant snippets before deciding which files to inspect in full. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill guides agents to install and run qmd locally and index user-selected markdown folders. <br>
Mitigation: Verify trust in the qmd repository and global bun install before setup, and only index folders that are appropriate for local search. <br>
Risk: Search results may expose sensitive paths or snippets from local markdown collections. <br>
Mitigation: Review returned file paths and snippets before asking the agent to read full files or use their contents. <br>
Risk: Indexes and embeddings may persist outside the source markdown folders. <br>
Mitigation: Check qmd documentation for index and embedding storage and deletion behavior before indexing sensitive collections. <br>


## Reference(s): <br>
- [qmd GitHub repository](https://github.com/tobi/qmd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with inline shell commands and summarized search results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search output includes relevant snippets, file paths, and context from local markdown collections.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
