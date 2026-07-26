## Description: <br>
proxq helps agents operate a Go, Redis-backed async HTTP proxy queue by submitting HTTP requests as jobs, polling status, fetching replayed upstream responses, and canceling named jobs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to interact with a proxq instance they control: submit async HTTP proxy jobs, poll job status, retrieve completed upstream responses, and cancel jobs the user identified. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: proxq can make outbound requests from its own network position and has no built-in authentication. <br>
Mitigation: Operate only a proxq instance you control, keep it behind authentication or loopback/internal networking, and configure upstreams only to trusted services. <br>
Risk: Headers and bodies submitted through proxq may be forwarded to configured upstreams. <br>
Mitigation: Avoid sending secrets to untrusted destinations and verify the upstream target before submitting a job. <br>
Risk: Job cancellation is best-effort, has no undo, and has no built-in ownership check. <br>
Mitigation: Cancel only jobs you submitted or jobs the user explicitly named. <br>


## Reference(s): <br>
- [proxq setup](references/setup.md) <br>
- [proxq ClawHub page](https://clawhub.ai/psyb0t/skills/proxq) <br>
- [asynq](https://github.com/hibiken/asynq) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, HTTP examples, and YAML configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PROXQ_URL for job operations; setup examples also use curl, Docker, and Docker Compose.] <br>

## Skill Version(s): <br>
0.10.3 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
