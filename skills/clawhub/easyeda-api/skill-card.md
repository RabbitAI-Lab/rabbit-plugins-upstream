## Description:

EasyEDA Pro API skill for AI agents that supports PCB design, schematic editing, footprint and symbol management, project operations, EasyEDA extension development, and live debugging through a local WebSocket bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to look up EasyEDA Pro APIs, generate EasyEDA extension code, inspect document source formats, and debug integrations against a running EasyEDA Pro client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can run arbitrary EasyEDA commands in a live EasyEDA Pro session.

Mitigation: Install only when intentional live EasyEDA control is needed, keep the bridge bound to localhost, and stop it when debugging is complete.

Risk: Generated commands may change or delete project data, export designs, open ordering flows, or use external requests.

Mitigation: Require explicit user confirmation before sensitive or destructive actions and review proposed JavaScript before execution.

Risk: Generated JavaScript from untrusted prompts or files could be unsafe in the EasyEDA client context.

Mitigation: Do not run untrusted generated JavaScript without manual review and scope execution to the intended project and window.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [Agent Skills Standard](https://agentskills.io/)
- [EasyEDA Bridge Extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)
- [API Reference Index](artifact/references/_index.md)
- [API Quick Reference](artifact/references/_quick-reference.md)
- [Document Source Format Overview](artifact/format/index.md)
- [Extension API Guide](artifact/guide/index.md)
- [Using Extensions Guide](artifact/user-guide/using-extension.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JavaScript snippets, API references, and configuration steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce EasyEDA JavaScript intended for execution through a localhost bridge after user review.]

## Skill Version(s):

1.1.17 (source: ClawHub release metadata; artifact metadata/package report 1.1.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
