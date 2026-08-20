## Description:

Provides EasyEDA API references, document-format guidance, and a local WebSocket bridge for AI agents to generate, debug, and execute EasyEDA automation code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to look up EasyEDA APIs, generate or debug EasyEDA extension code, inspect document source formats, and optionally run automation code against an active EasyEDA client through a local bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can give an AI agent broad local execution power over a live EasyEDA session through the disclosed bridge.

Mitigation: Use it on copies or test projects first, and review generated code before sending it to the bridge.

Risk: Bridge-driven actions can affect active EasyEDA projects, including project-opening, save, delete, manufacturing, ordering, or external-request workflows.

Mitigation: Require explicit user confirmation before those actions and verify the selected EasyEDA window and project before execution.

Risk: Leaving the bridge running after work is finished increases the window for unintended local execution.

Mitigation: Stop the bridge when finished and run it only during active EasyEDA automation or debugging sessions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [EasyEDA API reference index](references/_index.md)
- [EasyEDA API quick reference](references/_quick-reference.md)
- [EasyEDA document source format reference](format/index.md)
- [EasyEDA extension startup guide](guide/how-to-start.md)
- [EasyEDA extension user guide](user-guide/using-extension.md)
- [EasyEDA API gateway extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JavaScript and shell command snippets; bridge responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, CLAUDE_SKILL_DIR, and an EasyEDA client with extension support when live bridge execution is used.]

## Skill Version(s):

1.1.11 (source: server release metadata; artifact metadata reports 1.1.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
