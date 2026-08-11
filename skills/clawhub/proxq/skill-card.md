## Description:

proxq helps an agent submit HTTP requests to a trusted Redis-backed async proxy queue, poll job status, fetch completed upstream responses, and provide setup guidance for running proxq with Docker and Redis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with a trusted proxq instance when they need an async facade for slow, unreliable, or long-running HTTP workloads. The skill is useful for submitting requests, polling job results, configuring routing and caching behavior, and understanding safe operating constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: proxq can act as an SSRF surface because it submits outbound HTTP requests from its own network position to configured upstreams.

Mitigation: Operate only trusted proxq instances, configure upstreams only for services you intend proxq to reach, and do not let untrusted callers choose upstream prefixes or URLs.

Risk: proxq has no built-in authentication or authorization for job submission, status, content, or cancellation endpoints.

Mitigation: Place proxq behind authentication such as a reverse proxy, API gateway, or mTLS, or bind it to loopback or a private network.

Risk: Forwarded request headers and bodies can include secrets that reach the configured upstream.

Mitigation: Forward credentials only to trusted upstreams and avoid submitting sensitive data unless the upstream and proxq operator are trusted.

Risk: Job cancellation deletes records and has no ownership check.

Mitigation: Cancel only job IDs submitted by the current user or explicitly identified by the user.

## Reference(s):

- [proxq ClawHub release](https://clawhub.ai/psyb0t/skills/proxq)
- [proxq setup](references/setup.md)
- [docker-proxq project homepage](https://github.com/psyb0t/docker-proxq)
- [asynq](https://github.com/hibiken/asynq)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, Docker Compose, and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include HTTP request examples, job polling loops, Docker commands, and configuration snippets for a trusted proxq deployment.]

## Skill Version(s):

0.10.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
