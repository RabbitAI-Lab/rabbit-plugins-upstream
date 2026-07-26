## Description: <br>
Builds and maintains a global, project-independent knowledge wiki from user-uploaded documents using a no-vector, no-chunk wiki workflow based on single markdown pages, a two-level topic/page index, and wikilinks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[neuhanli](https://clawhub.ai/user/neuhanli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and knowledge workers use this skill to create, update, query, and health-check a local markdown wiki built from uploaded documents. It is intended for structured knowledge-base workflows where source-grounded pages, generated indexes, and controlled update handling matter more than vector retrieval. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded documents are copied into a persistent .wiki-creator directory that may be project-local or in the user's home directory. <br>
Mitigation: Choose the storage location explicitly, add project-local .wiki-creator/ to .gitignore when appropriate, and delete raw files or generated wiki data when they are no longer needed. <br>
Risk: The skill may read stored wiki material when answering later knowledge questions, which can expose private or regulated content to subsequent local workflows. <br>
Mitigation: Use separate wiki roots for different projects or sensitivity levels and avoid installing or using the skill with private material unless persistent local storage is acceptable. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/wiki-creator) <br>
- [Query Mode](references/query-mode.md) <br>
- [Schema Guide](references/schema-guide.md) <br>
- [Cascade Update](references/cascade-update.md) <br>
- [Page Authoring](references/page-authoring.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JSON script output, generated wiki files, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates local .wiki-creator raw and wiki directories; generated indexes, manifests, graph files, backlinks, and health reports may persist until removed.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
