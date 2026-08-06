## Description: <br>
Create and operate a local Design System Hub that stores multiple design systems, generates complete entries from screenshots, URLs, or written style descriptions, and exposes browsable documentation, live mocks, copied tokens, DESIGN.md, standalone HTML, and JSON APIs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yofine](https://clawhub.ai/user/yofine) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and designers use this skill to initialize a local React/Vite design-system hub, add systems from screenshots, URLs, or written briefs, and export browsable documentation and agent-readable design artifacts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill starts a local web service that can bind to the network. <br>
Mitigation: Prefer localhost binding unless LAN access is explicitly required, and report the actual port used. <br>
Risk: The bundled npm template has dependency-security concerns. <br>
Mitigation: Run npm audit or update review before use, and review dependency changes before deploying the generated hub. <br>
Risk: Screenshots and private URLs may contain sensitive content. <br>
Mitigation: Avoid supplying sensitive sources unless sanitized derivatives are acceptable, and replace personal or confidential details in generated mocks and exports. <br>


## Reference(s): <br>
- [Design System Hub ClawHub Skill Page](https://clawhub.ai/yofine/skills/design-hub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with generated project files, TypeScript/React code, JSON APIs, DESIGN.md exports, standalone HTML, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local-first design-system documentation and exports; generated entries should sanitize sensitive screenshot or URL content.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
