## Description:

A local Python orchestration skill for coordinating multi-agent workflows through a shared blackboard, permission gating, token budget scripts, and persistent project context.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jovancoding](https://clawhub.ai/user/jovancoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent orchestrators use it to coordinate multi-agent work in one trusted workspace, manage shared task state, apply advisory permission scoring and budget checks, and maintain project context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Concurrent Windows use can lose blackboard updates because file locking may not protect simultaneous writes.

Mitigation: Avoid concurrent Windows use until locking is corrected, or serialize commands externally.

Risk: Local coordination state and audit logs can contain sensitive information, and permission grant tokens are advisory rather than authentication.

Mitigation: Keep secrets and personal data out of context and logs, restrict access to local state, and require separate authentication and approval for sensitive operations.

## Reference(s):

- [Network-AI homepage](https://network-ai.org)
- [Network-AI ClawHub release](https://clawhub.ai/jovancoding/skills/network-ai)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Guidance]

**Output Format:** [JSON status and result data, plus local JSON and Markdown coordination files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts also print command-line status; coordination state persists locally under the project directory.]

## Skill Version(s):

5.17.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
