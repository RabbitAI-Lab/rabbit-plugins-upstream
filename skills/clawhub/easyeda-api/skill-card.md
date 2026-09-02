## Description:

EasyEDA API Skill helps agents look up EasyEDA Pro APIs, generate extension or automation code, and control a running EasyEDA client through a local WebSocket bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to automate EasyEDA Pro sessions, inspect PCB and schematic APIs, build EasyEDA extensions, and work with EasyEDA project, schematic, and PCB source formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can run agent-supplied code against live EasyEDA design projects.

Mitigation: Install only when intentional, keep the bridge limited to localhost, review code before execution, and stop the bridge when finished.

Risk: Agent-driven actions can affect active design work, including delete, rename, order, screenshot/export, and project-switching operations.

Mitigation: Use backed-up or test projects first and require explicit confirmation before these higher-impact actions.

## Reference(s):

- [ClawHub Release Page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [EasyEDA API Reference Index](references/_index.md)
- [EasyEDA API Quick Reference](references/_quick-reference.md)
- [EasyEDA Document Source Format Overview](format/index.md)
- [EasyEDA Extension API Guide](guide/index.md)
- [EasyEDA Extension Development Startup Guide](guide/how-to-start.md)
- [EasyEDA API Invocation Guide](guide/invoke-apis.md)
- [EasyEDA Run API Gateway Extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, JSON API examples, and JavaScript snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute JavaScript against a connected local EasyEDA session through the bridge.]

## Skill Version(s):

1.1.23 (source: ClawHub release metadata; artifact metadata reports 1.1.28)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
