## Description:

Guides agents in submitting HTTP requests to a Redis-backed proxy queue, polling for results, and managing queued jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to send requests through an existing proxq instance, poll for delayed responses, and cancel their own jobs when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unauthenticated access can allow anyone who reaches proxq to submit, view, or cancel jobs.

Mitigation: Use authentication or network isolation; never expose the instance directly to the internet.

Risk: Proxq can forward requests from its network position to configured upstreams, including sensitive internal services.

Mitigation: Use only trusted upstreams, avoid internal or administrative targets, and restrict who can submit requests.

Risk: Unpinned container images can change unexpectedly between deployments.

Mitigation: Pin Docker image versions or digests before production use.

## Reference(s):

- [proxq on ClawHub](https://clawhub.ai/psyb0t/skills/proxq)
- [proxq project homepage](https://github.com/psyb0t/docker-proxq)
- [proxq setup and configuration](references/setup.md)
- [asynq](https://github.com/hibiken/asynq)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, API request guidance]

**Output Format:** [Markdown with shell commands and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Job IDs, status responses, and replayed HTTP response guidance when applicable]

## Skill Version(s):

0.11.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
