## Description: <br>
Local-first, event-driven RAG for commercial real estate audit and investigation case folders, with case and stage filtering plus page-level citations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jack4world](https://clawhub.ai/user/jack4world) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Audit and investigation teams use this skill to organize local case folders, build a searchable evidence index, and query mixed document sets with case, stage, and page-level citations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local manifests, converted PDFs, and index files can contain sensitive audit or investigation text. <br>
Mitigation: Keep case folders and output directories private, and do not commit generated artifacts to source control. <br>
Risk: Processing untrusted Office or PDF documents can expose the local environment to parser and converter risks. <br>
Mitigation: Run the skill in an isolated virtual environment and sandbox LibreOffice or PDF parsing when documents are untrusted. <br>
Risk: Unpinned dependencies and embedding model downloads can reduce reproducibility or introduce supply-chain exposure. <br>
Mitigation: Pin dependencies with a lockfile and pre-provision embedding model files for offline or controlled use. <br>


## Reference(s): <br>
- [Audit Case Folder Template](references/case-folder-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/jack4world/skills/audit-case-rag) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, plus local manifest and index files when the helper script is run.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Query output includes ranked evidence snippets and source citations; local outputs may contain sensitive audit text.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
