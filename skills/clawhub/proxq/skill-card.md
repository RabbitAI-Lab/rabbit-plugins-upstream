## Description: <br>
proxq helps agents use a self-run Redis-backed asynchronous HTTP proxy queue to submit requests, poll job status, fetch replayed upstream responses, and cancel jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to interact with a trusted proxq instance when they need fire-and-forget HTTP request handling, webhook relays, retries, queued long-running work, or polling-based response retrieval behind short-timeout clients and reverse proxies. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A reachable proxq instance can submit outbound requests from its network position and expose proxy behavior to callers. <br>
Mitigation: Operate only trusted proxq instances, keep them behind authentication or loopback/internal networking, and configure upstreams only for services you trust. <br>
Risk: Requests may include secrets or sensitive bodies that pass through proxq, Redis storage, and the configured upstream. <br>
Mitigation: Avoid sensitive payloads unless the proxq instance, Redis storage, and upstream are all under appropriate control. <br>


## Reference(s): <br>
- [proxq setup](references/setup.md) <br>
- [proxq skill page](https://clawhub.ai/psyb0t/skills/proxq) <br>
- [asynq](https://github.com/hibiken/asynq) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with curl, Docker, Docker Compose, YAML, HTTP, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance assumes an existing trusted proxq instance identified by PROXQ_URL and may include job submission, polling, content retrieval, cancellation, and setup commands.] <br>

## Skill Version(s): <br>
0.10.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
