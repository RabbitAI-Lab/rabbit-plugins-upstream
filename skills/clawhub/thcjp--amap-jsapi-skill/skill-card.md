## Description: <br>
Amap Jsapi Skill helps agents provide guidance, code, and configuration for GaoDe/AMap JSAPI v2.0 WebGL map integration, including map initialization, secure key handling, 3D view control, overlays, and LBS services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to integrate AMap JSAPI v2.0 into web applications, including setup, map controls, overlay drawing, routing, search, and safe handling of map credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests exec capability and uses broad trigger language that may route it into tasks outside AMap JSAPI/WebGL work. <br>
Mitigation: Use it only for AMap JSAPI/WebGL tasks and review proposed commands or configuration before execution. <br>
Risk: The scanner notes unrelated security-auditing claims in the artifact documentation. <br>
Mitigation: Do not rely on the skill for general security auditing or CVE analysis unless separate evidence supports that use. <br>
Risk: Client-side map integrations can expose production credentials when examples use generic API key placeholders. <br>
Mitigation: Do not paste production credentials into examples; use environment variables and server-side proxy patterns for sensitive AMap security values. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/amap-jsapi-skill) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Skill homepage](https://skillhub.cn) <br>
- [AMap JSAPI loader](https://webapi.amap.com/loader.js) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with JavaScript, JSON, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include AMap configuration snippets, map integration examples, and credential-handling guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
