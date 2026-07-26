## Description: <br>
Cargo Content helps agents guide users through uploading, organizing, syncing, and removing Cargo workspace files and libraries for retrieval-augmented generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cargo-ai](https://clawhub.ai/user/cargo-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace operators use this skill to manage Cargo knowledge files and libraries, including upload, listing, renaming, moving, removal, and connector-backed library setup for RAG resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded files may contain sensitive data and may be indexed for retrieval. <br>
Mitigation: Confirm the workspace, file contents, access permissions, and intended indexing before uploading files or syncing libraries. <br>
Risk: UUID-targeted updates and remove commands can affect the wrong file or library, and deletion reversibility is not documented in the evidence. <br>
Mitigation: List and verify file or library UUIDs before updates or removals, and keep backups of source documents. <br>
Risk: Cargo authentication can use OAuth sessions or API tokens. <br>
Mitigation: Use approved authentication flows, avoid exposing tokens in shell history or shared transcripts, and rotate tokens if exposed. <br>


## Reference(s): <br>
- [Cargo Content on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-content) <br>
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills) <br>
- [File and library examples](references/examples/files.md) <br>
- [Content response shapes](references/response-shapes.md) <br>
- [Content troubleshooting](references/troubleshooting.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands target the cargo-ai CLI and typically return JSON; uploads and removals affect Cargo workspace content.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
