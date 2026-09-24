## Description:

GNO helps agents index and search local documents, notes, and knowledge bases with keyword, vector, hybrid, and cited-answer workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gmickel](https://clawhub.ai/user/gmickel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, knowledge workers, and agent users use GNO to set up local document retrieval, query indexed files, capture provenance-aware notes, and produce cited answers from selected local sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run local `gno` commands over selected documents and folders.

Mitigation: Index only folders intended for agent retrieval, and avoid broad confidential directories unless that exposure is deliberate.

Risk: Write, overwrite, administration, daemon, and publishing commands can change local configuration, stored notes, indexes, or exported artifacts.

Mitigation: Review `--force`, `--enable-write`, `reset`, `cleanup`, `daemon`, and publishing commands before allowing them to run.

Risk: Remote serving, model calls, exports, or publishing may move data outside the local machine when explicitly enabled.

Mitigation: Keep remote and export policies local-only unless the user intentionally authorizes data to leave the machine.

## Reference(s):

- [GNO skill instructions](SKILL.md)
- [GNO CLI reference](cli-reference.md)
- [GNO MCP reference](mcp-reference.md)
- [GNO examples](examples.md)
- [ClawHub listing](https://clawhub.ai/gmickel/skills/gno)
- [GNO agent instructions](https://gno.sh/docs/agents-install)
- [GNO MCP documentation](https://www.gno.sh/docs/MCP)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON-oriented command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on local GNO CLI state, indexed user-selected files, and enabled MCP or serving modes.]

## Skill Version(s):

1.2.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
