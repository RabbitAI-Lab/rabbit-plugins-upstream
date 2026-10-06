## Description:

Helps an agent connect to Everpod, start and check cloud pods, and guide its owner through moving an agent to a pod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everpod](https://clawhub.ai/user/everpod)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their owners use this skill to set up managed OpenClaw or developer pods, check pod status, and move agent state to a new pod when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Everpod API key is stored in OpenClaw settings and permits viewing and starting pods.

Mitigation: Keep the key private, do not repeat it in responses, and revoke it when no longer needed.

Risk: Starting an unpaid pod can lead to a monthly subscription if its owner pays for it.

Mitigation: Start pods only at the owner's request and leave payment to the owner.

Risk: An agent migration archive can include personal workspace, memory, skills, and scheduled-job details.

Mitigation: Migrate only when requested; review the archive and exclude passwords, API keys, configuration, databases, and media before transfer.

## Reference(s):

- [Everpod API documentation](https://everpod.ai/docs/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls]

**Output Format:** [Markdown with links and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pod status and payment links are shared with the owner; payment is completed by the owner.]

## Skill Version(s):

1.1.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
