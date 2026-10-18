## Description:

Helps agents search and organize local documents and notes, retrieve relevant passages, and answer questions with source citations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask an agent to index and search their local files, retrieve cited evidence, and work with notes or past agent sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing private folders or agent sessions may expose sensitive material to search and retrieval.

Mitigation: Review collections before indexing and prefer dry-run, project-scoped, or read-only workflows.

Risk: Write permissions or automatic session imports can change local knowledge stores without careful review.

Mitigation: Enable write access, force operations, and session automation only when explicitly intended.

Risk: Publishing, exporting, or remote access may disclose indexed content.

Mitigation: Review collection boundaries and destinations before enabling remote access or publish/export flows.

## Reference(s):

- [GNO ClawHub release](https://clawhub.ai/gmickel/skills/gno)
- [GNO CLI reference](artifact/cli-reference.md)
- [GNO MCP reference](artifact/mcp-reference.md)
- [GNO examples](artifact/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with source citations and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Answers may cite local document or session sources.]

## Skill Version(s):

1.2.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
