## Description: <br>
proxq helps an agent use a Go, Redis-backed async HTTP proxy queue by submitting HTTP requests, returning job IDs, polling replayed upstream responses, and cancelling jobs against a trusted running instance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to submit, poll, inspect, and cancel proxq jobs for slow backends, webhook relays, large uploads, or long-running processing behind short-timeout reverse proxies. It assumes the proxq service is already deployed and trusted. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: proxq can proxy requests from its own network position, creating SSRF exposure if untrusted callers or upstreams are allowed. <br>
Mitigation: Use only trusted upstreams, keep the service behind loopback, an internal network, or an authenticated reverse proxy, and do not let untrusted callers choose upstream URLs or prefixes. <br>
Risk: The proxq service has no built-in authentication or per-job ownership checks. <br>
Mitigation: Protect the service with external authentication or network isolation, and only poll or cancel job IDs supplied by the user or returned from the current workflow. <br>
Risk: Requests may forward sensitive headers or bodies to configured upstreams. <br>
Mitigation: Send credentials and payloads only when the configured upstream is intended to receive them, and avoid exposing bare proxq endpoints to untrusted clients. <br>


## Reference(s): <br>
- [proxq setup](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/proxq) <br>
- [asynq](https://github.com/hibiken/asynq) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with curl, Docker, Docker Compose, YAML, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses PROXQ_URL and requires curl and Docker for the documented workflows.] <br>

## Skill Version(s): <br>
0.10.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
