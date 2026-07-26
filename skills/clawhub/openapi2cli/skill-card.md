## Description: <br>
Generate CLI tools from OpenAPI specs. Built for AI agents who hate writing curl commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[awlevin](https://clawhub.ai/user/awlevin) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and AI agents use this skill to generate command-line clients from OpenAPI or Swagger specifications, making APIs easier to inspect, call, and automate without hand-writing curl commands. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated CLIs are real API clients and may send network requests or mutate remote systems. <br>
Mitigation: Inspect the OpenAPI specification and generated commands before execution, and prefer dry-run mode or staging endpoints for validation. <br>
Risk: API credentials may be exposed or misused when passed directly to generated CLI commands. <br>
Mitigation: Prefer environment variables or a secret manager, and avoid production tokens unless the intended action has been reviewed. <br>


## Reference(s): <br>
- [OpenAPI to CLI ClawHub page](https://clawhub.ai/awlevin/skills/openapi2cli) <br>
- [OpenAPI to CLI PyPI package](https://pypi.org/project/openapi2cli/) <br>
- [OpenAPI to CLI homepage](https://github.com/Olafs-World/openapi2cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Code, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces commands and generated CLI usage patterns for OpenAPI specifications; generated CLIs can emit structured JSON responses.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
