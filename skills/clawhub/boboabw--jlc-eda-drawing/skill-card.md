## Description:

JLC EDA Drawing helps agents design, draw, review, and automate PCB-ready schematics and layouts in EasyEDA/JLC EDA using real library parts and a local EasyEDA API bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[boboabw](https://clawhub.ai/user/boboabw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and electronics engineers use this skill to create or review PCB-ready EasyEDA/JLC EDA designs, including schematic architecture, part selection, net organization, and layout/DRC workflow guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled bridge exposes powerful EasyEDA code execution without adequate access controls.

Mitigation: Review before installing, use only in a trusted local environment, and stop the bridge when the task is complete.

Risk: Exposing or forwarding the bridge port range could allow unintended access to EasyEDA automation.

Mitigation: Do not expose or forward ports 49620-49629; prefer a build that binds to 127.0.0.1, validates browser origins, and requires a per-session token.

Risk: EasyEDA file-system permissions and destructive design actions can affect local files or project state.

Mitigation: Avoid enabling EasyEDA external file-system permissions unless specifically needed, and require confirmation before destructive design or file operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/boboabw/skills/jlc-eda-drawing)
- [Run API Gateway extension page](https://ext.lceda.cn/item/oshwhub/run-api-gateway)
- [EasyEDA API package](https://image.lceda.cn/files/easyeda-api.zip)
- [Bridge and API reference](references/bridge-api.md)
- [Design standards](references/design-standards.md)
- [Parts strategy](references/parts-strategy.md)
- [PCB workflow](references/pcb-workflow.md)
- [EasyEDA API quick reference](references/easyeda-api-reference/_quick-reference.md)
- [EasyEDA API index](references/easyeda-api-reference/_index.md)

## Skill Output:

**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline JavaScript, shell commands, and design guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include EasyEDA bridge setup steps, executable EasyEDA API snippets, part-selection notes, verification results, and electrical assumptions.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
