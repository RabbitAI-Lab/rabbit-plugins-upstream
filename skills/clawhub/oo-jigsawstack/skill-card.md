## Description:

JigsawStack (jigsawstack.com). Use this skill for ANY JigsawStack request -- searching and reading data. Whenever a task involves JigsawStack, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate JigsawStack through an OOMOL-connected account for web search, search suggestions, summarization, translation, profanity checks, and spam checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote installer commands that execute downloaded code directly.

Mitigation: Review the installer path before use and prefer a verified package manager or a pinned download with checksum or signature verification.

Risk: Task text is sent through OOMOL and JigsawStack as part of the connector workflow.

Mitigation: Avoid sending sensitive content unless the user's data handling requirements allow processing by those services.

## Reference(s):

- [ClawHub JigsawStack Skill Page](https://clawhub.ai/oomol/skills/oo-jigsawstack)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [JigsawStack Homepage](https://jigsawstack.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the OOMOL oo CLI and return connector JSON responses.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
