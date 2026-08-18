## Description:

EasyEDA API Skill helps agents work with EasyEDA Pro projects, PCB and schematic editing, extension development, API reference lookup, and live debugging through a local WebSocket bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to look up EasyEDA Pro APIs, generate extension or automation code, inspect EasyEDA document source formats, and optionally control a running EasyEDA client for debugging.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can run code inside a live EasyEDA client.

Mitigation: Keep the bridge stopped when not in use, run it only for trusted prompts and projects, and review generated JavaScript before execution.

Risk: Automation may modify or delete design data, switch projects, export files, or open manufacturing and order flows.

Mitigation: Require explicit user confirmation before destructive, project-changing, export, manufacturing, or transaction-oriented actions.

Risk: The bridge is broad and unauthenticated on the local host.

Mitigation: Use it only on trusted local machines and close the bridge after the EasyEDA automation session ends.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [EasyEDA API Reference Index](references/_index.md)
- [EasyEDA API Quick Reference](references/_quick-reference.md)
- [Extension API Guide](guide/index.md)
- [EasyEDA File Format Overview](format/index.md)
- [EasyEDA Bridge Extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON API responses, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute JavaScript in a connected EasyEDA client through a local bridge when the user enables it.]

## Skill Version(s):

1.1.6 (source: server release metadata, skill metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
