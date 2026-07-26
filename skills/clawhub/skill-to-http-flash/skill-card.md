## Description: <br>
Skill To Http Flash compiles a Python-entry agent skill into a standalone HTTP REST API microservice with JSON-to-CLI request mapping, subprocess execution, and a structured response envelope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and platform engineers use this skill to turn argparse-based Python skill entries into standalone FastAPI services for local tools, CI/CD steps, and service-to-service calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated services can expose local skill execution over unauthenticated HTTP when deployed beyond a trusted local interface. <br>
Mitigation: Bind generated servers to localhost or a firewalled interface, require FLASH_API_KEY for any non-local use, and use TLS or a secure reverse proxy. <br>
Risk: Create or recreate can send SKILL.md content to a configured LLM endpoint for parameter schema extraction. <br>
Mitigation: Review the configured LLM endpoint before generation and use fallback or manually edited params.json when that disclosure is not acceptable. <br>
Risk: The generated service runs the target skill as a subprocess and may expose that skill's output or stderr through HTTP responses. <br>
Mitigation: Only flash trusted skills, run generated services as a low-privilege user or container, and review the target skill before exposing /run. <br>


## Reference(s): <br>
- [README](README.md) <br>
- [Standalone Usage Guide](references/standalone-usage.md) <br>
- [Migration From v1](references/migration-from-v1.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/songhonglei/skills/skill-to-http-flash) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with shell commands plus generated Python service files and JSON configuration.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated services return a JSON envelope with success, exit_code, elapsed_ms, and either data or output.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata and artifact documentation) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
