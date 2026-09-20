## Description:

OOMOL RAG helps agents use the OOMOL RAG knowledge base through the oomol_rag connector and oo CLI for retrieval, file inspection, upload, download, and deletion workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve relevant text chunks from an OOMOL team's knowledge base and administer source files through list, inspect, download, upload, and deletion actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Install the oo CLI only through a verified package, pinned release, or manually reviewed installer, and do not let an agent run the remote installer automatically.

Risk: The skill can upload files and delete knowledge-base files.

Mitigation: Review write and destructive payloads carefully, confirm the target file and intended effect with the user, and require explicit approval before deletion.

## Reference(s):

- [OOMOL RAG homepage](https://knowledge-base.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-oomol-rag)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include oo CLI commands, connector schemas, JSON payloads, action results, and workflow guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
