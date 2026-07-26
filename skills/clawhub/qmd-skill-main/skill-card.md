## Description: <br>
Local hybrid search for markdown notes and docs. Use when searching notes, finding related content, or retrieving documents from indexed collections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pmaeter](https://clawhub.ai/user/pmaeter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and knowledge workers use this skill to search, retrieve, and maintain local Markdown note or document collections through qmd. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing qmd from an external package source can introduce untrusted code. <br>
Mitigation: Install only if you trust the external qmd package source. <br>
Risk: Indexing local Markdown collections can expose private notes or sensitive documents to agent search. <br>
Mitigation: Index only folders intended for agent search and avoid collections containing secrets or highly sensitive notes. <br>
Risk: Scheduled indexing can repeatedly process local files in the background. <br>
Mitigation: Enable scheduled indexing only when recurring background updates are desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pmaeter/skills/qmd-skill-main) <br>
- [qmd homepage](https://github.com/tobi/qmd) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON-producing qmd commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include qmd search, retrieval, setup, maintenance, and scheduling commands for local Markdown collections.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
