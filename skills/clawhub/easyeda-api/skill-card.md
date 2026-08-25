## Description:

EasyEDA API Skill helps agents work with EasyEDA Pro using API references, extension-development documentation, and a local bridge for live debugging and project operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yanranxiaoxi](https://clawhub.ai/user/yanranxiaoxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to look up EasyEDA APIs, generate or debug extension code, and automate schematic, PCB, library, and project operations in a connected EasyEDA client.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local bridge can execute agent-supplied code in a live EasyEDA session.

Mitigation: Use it only when live EasyEDA control is intended, review generated code before execution, and stop the bridge after the task is complete.

Risk: Bridge exposure beyond localhost could allow unintended control of an EasyEDA session.

Mitigation: Do not expose, proxy, or forward the localhost port range used by the bridge.

Risk: Automation may delete or alter boards, schematics, primitives, exports, images, projects, or manufacturing/order data.

Mitigation: Require explicit user confirmation before destructive, export, project-switching, canvas-capture, or manufacturing/order actions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yanranxiaoxi/skills/easyeda-api)
- [README](artifact/README.md)
- [API reference index](artifact/references/_index.md)
- [API quick reference](artifact/references/_quick-reference.md)
- [EasyEDA extension API guide](artifact/guide/index.md)
- [Invoking the Extension API](artifact/guide/invoke-apis.md)
- [Document source format reference](artifact/format/index.md)
- [Run API Gateway extension](https://jlc-ext.com/item/oshwhub/run-api-gateway)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline JavaScript, JSON, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include executable EasyEDA JavaScript and local curl commands that should be reviewed before use.]

## Skill Version(s):

1.1.20 (source: server release metadata; artifact metadata reports 1.1.25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
