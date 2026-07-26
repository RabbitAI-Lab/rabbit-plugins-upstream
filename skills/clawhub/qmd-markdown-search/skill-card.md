## Description: <br>
Local hybrid search for markdown notes and docs. Use when searching notes, finding related content, or retrieving documents from indexed collections. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[emcmillan80](https://clawhub.ai/user/emcmillan80) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, researchers, and knowledge workers use this skill to search local Markdown notes, documentation, and knowledge bases, retrieve relevant files, and choose between fast keyword search and slower semantic or hybrid search modes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill installs and relies on the external qmd tool through a Bun-based install path. <br>
Mitigation: Install only when the upstream qmd project and install command are trusted. <br>
Risk: Indexed Markdown collections may contain private or sensitive local files that an agent can search or retrieve. <br>
Mitigation: Index only folders intended for agent-assisted search, and avoid secret-heavy notes or documents. <br>
Risk: Scheduled indexing or embedding updates can repeatedly process selected local collections. <br>
Mitigation: Enable scheduled updates deliberately and scope them to approved collections. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/emcmillan80/skills/qmd-markdown-search) <br>
- [qmd upstream homepage](https://github.com/tobi/qmd) <br>
- [Publisher profile](https://clawhub.ai/user/emcmillan80) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and optional JSON command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce qmd search, retrieval, indexing, update, embedding, and scheduling commands for local Markdown collections.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
