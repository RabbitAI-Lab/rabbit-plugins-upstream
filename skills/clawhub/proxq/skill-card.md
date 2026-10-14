## Description:

Helps developers submit HTTP requests to a trusted proxq instance for asynchronous forwarding, then poll results or cancel jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to submit requests to a proxq instance, monitor queued work, retrieve upstream responses, and cancel their own jobs when needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An internet-exposed proxq instance has no built-in authentication or job ownership checks.

Mitigation: Bind it to loopback or an internal network, require authentication or mTLS at the edge, and cancel only jobs you own.

Risk: Submitted requests can reach configured upstreams from the proxy's network position.

Mitigation: Configure only trusted upstreams and submit only requests intended for those services.

Risk: Unpinned container images can change between deployments.

Mitigation: Pin Docker images before production use.

## Reference(s):

- [proxq ClawHub release](https://clawhub.ai/psyb0t/skills/proxq)
- [proxq setup and configuration](references/setup.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, Text]

**Output Format:** [Markdown with shell and YAML examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Job IDs, status, and upstream responses are returned by the configured proxq instance.]

## Skill Version(s):

0.11.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
