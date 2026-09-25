## Description:

Helps agents index and search local documents, notes, and past agent sessions, and answer questions with citations using GNO.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users with local documents use this skill to guide an agent through indexing files, finding relevant passages, and answering questions with citations. It can also locate evidence from past coding-agent sessions when the user requests it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indexing sensitive folders or importing agent sessions can expose private content to the local index.

Mitigation: Index only folders the user selects and import sessions only on explicit request.

Risk: Remote access, network export, or publishing can share indexed content outside the machine.

Mitigation: Review collection egress policy before remote or non-loopback use and publish only when requested.

Risk: Forced installation, write-enabled tools, daemons, hooks, or schedules can replace edits or make ongoing changes.

Mitigation: Avoid --force and --enable-write, and enable daemons, hooks, or schedules only with the user's approval.

## Reference(s):

- [GNO ClawHub release](https://clawhub.ai/gmickel/skills/gno)
- [GNO CLI reference](artifact/cli-reference.md)
- [GNO MCP reference](artifact/mcp-reference.md)
- [GNO usage examples](artifact/examples.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown responses with citations and optional command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results and answers may cite indexed files or session evidence.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
