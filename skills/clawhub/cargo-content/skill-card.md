## Description:

Manage Cargo workspace files and knowledge libraries, including uploads, path-based storage, retrieval, and sharing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workspace operators use this skill to upload and organize documents for agent retrieval, manage knowledge libraries, and store, read, or share files by path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Deployment examples may replace an agent's existing tools and capabilities when settings are omitted.

Mitigation: Preserve the agent's existing settings and review the full deployment change before deploying.

Risk: Path writes can overwrite the newest file at that path, and file removal is permanent.

Mitigation: Confirm the active workspace and intended paths before writing or deleting files.

Risk: Signed and public links allow unauthenticated access; uploads may be indexed through OpenAI and mirrored into the context repository.

Mitigation: Share links only when requested, and use put for files that should stay unindexed and unmirrored.

## Reference(s):

- [Cargo Content on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-content)
- [File and library examples](references/examples/files.md)
- [Files as storage](references/objects.md)
- [Content response shapes](references/response-shapes.md)
- [Content troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, JSON]

**Output Format:** [Markdown with shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workspace-changing commands and file-sharing instructions; review before running.]

## Skill Version(s):

1.3.0 (source: release metadata, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
