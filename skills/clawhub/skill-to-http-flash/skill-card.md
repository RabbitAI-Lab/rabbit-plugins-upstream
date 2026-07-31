## Description: <br>
Compiles a single Python-based agent skill into a standalone HTTP REST API microservice that runs the skill entrypoint by subprocess and returns a structured response envelope. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[songhonglei](https://clawhub.ai/user/songhonglei) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to expose an argparse-based Python skill as a standalone HTTP service for local tools, CI pipelines, cross-service calls, or runtime-neutral deployments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated services can expose local skill execution over a reachable network endpoint. <br>
Mitigation: Bind the service to localhost or a trusted interface, set an API key, restrict CORS, and use HTTPS before cross-host access. <br>
Risk: Optional generation-time schema extraction can send skill documentation to an external LLM endpoint. <br>
Mitigation: Keep LLM schema extraction disabled for skills whose documentation contains secrets or internal details, or review and trust the configured endpoint before enabling it. <br>
Risk: Asynchronous job output and service state can persist as local data. <br>
Mitigation: Treat job logs, generated service files, certificates, API keys, and data directories as sensitive deployment artifacts and manage retention and access accordingly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-to-http-flash) <br>
- [Standalone usage guide](references/standalone-usage.md) <br>
- [Migration from v1](references/migration-from-v1.md) <br>


## Skill Output: <br>
**Output Type(s):** [Code, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell commands and generated FastAPI service files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated services expose synchronous and asynchronous HTTP endpoints and return JSON envelopes containing success, exit_code, data or output, stderr, and truncation metadata.] <br>

## Skill Version(s): <br>
2.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
