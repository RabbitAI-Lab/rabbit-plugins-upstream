## Description:

Helps OpenClaw agents and their owners set up and manage Everpod hosting, including moving an existing agent to a private cloud pod.

This skill is ready for commercial/non-commercial use.

## Publisher:

[everpod](https://clawhub.ai/user/everpod)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and agents use this skill to start or check Everpod cloud pods and move an existing agent's workspace, skills, and scheduled-job details to a pod. Owners approve the move, provide their account key, and handle payment themselves.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An Everpod account key gives the agent access to pod information and the ability to start unpaid pods.

Mitigation: Treat the key as sensitive, never repeat it in replies, and revoke it when no longer needed.

Risk: A migration archive may contain private workspace files, memory, skills, and scheduled-job details.

Mitigation: Review the archive before sending it and leave out passwords, API keys, configuration, and databases.

Risk: Starting a pod begins a process that can lead to a paid subscription.

Mitigation: Start a pod only at the owner's request; the owner reviews the price and pays through Everpod.

## Reference(s):

- [Everpod API documentation](https://everpod.ai/docs/api)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and pod links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes pod status explanations and agent-migration steps.]

## Skill Version(s):

1.0.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
