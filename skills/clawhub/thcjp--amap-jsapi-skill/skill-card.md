## Description: <br>
Amap JSAPI Skill helps developers configure and use AMap JSAPI v2.0 (WebGL) for map lifecycle management, security configuration, 3D view control, overlays, and LBS service integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and enterprise teams use this skill to get AMap JSAPI setup guidance, configuration snippets, map interaction examples, and troubleshooting support for web mapping integrations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests broad read/write/exec authority and describes generic command and file capabilities without clear limits. <br>
Mitigation: Install only in a constrained workspace, grant the minimum permissions needed for the mapping task, and review proposed commands or file changes before execution. <br>
Risk: AMap keys and securityJsCode can be exposed if copied into source code or frontend-only configuration. <br>
Mitigation: Keep AMap credentials out of source control, pass secrets through environment variables or a secret manager, and use a backend proxy for securityJsCode in production. <br>
Risk: The artifact advertises vulnerability scanning and compliance capabilities that are not clearly bounded by the AMap JSAPI use case. <br>
Mitigation: Do not rely on this skill for vulnerability scanning or compliance decisions; use approved scanners and human review for security assurance. <br>


## Reference(s): <br>
- [AMap JSAPI loader](https://webapi.amap.com/loader.js) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/amap-jsapi-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with code blocks and JSON-shaped result examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose AMap JSAPI configuration snippets, troubleshooting guidance, and example commands; review before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata; artifact frontmatter reports 1.1.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
