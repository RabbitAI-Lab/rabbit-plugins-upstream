## Description:

EasyEDA API Skill helps AI agents work with EasyEDA for PCB design, schematic editing, footprint and symbol management, extension development, and live debugging through a local bridge to a running EasyEDA client.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to look up EasyEDA APIs, generate or debug EasyEDA extension code, inspect source-format documentation, and execute reviewed code against a connected EasyEDA session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can execute code in a live EasyEDA session and modify real designs.

Mitigation: Run the bridge only during active debugging, review code before execution, and work on copies or backups for production designs.

Risk: High-impact actions such as delete, import, source-edit, ordering, screenshot, profile-data, or external-request operations may affect designs or expose data.

Mitigation: Require explicit user confirmation before these actions and stop the bridge when the task is complete.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [Publisher profile](https://clawhub.ai/user/yanranxiaoxi)
- [EasyEDA API Skill README](README.md)
- [EasyEDA extension development guide](guide/index.md)
- [EasyEDA API quick reference](references/_quick-reference.md)
- [EasyEDA document source format reference](format/index.md)
- [EasyEDA bridge user guide](user-guide/using-extension.md)
- [Run API Gateway extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with inline code, shell commands, API examples, and configuration guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local HTTP requests to the EasyEDA bridge and JavaScript snippets for execution in EasyEDA.]

## Skill Version(s):

1.1.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
